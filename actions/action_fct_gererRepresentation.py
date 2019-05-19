import sqlite3
from utils import display
from gui.fct_gererRepresentation import Ui_fct_gererRepresentation
from PyQt5.QtWidgets import QDialog, QTableWidgetItem
from datetime import datetime
import threading

class AppFctGererRepresentation(QDialog):
    ui = Ui_fct_gererRepresentation()

    # Constructeur
    def __init__(self, data:sqlite3.Connection):
        super(QDialog, self).__init__()
        self.ui.setupUi(self)
        self.data = data

        # On ajoute les spectacles dans le comboBox
        cursor = self.data.cursor()
        spectacles = cursor.execute("SELECT nomSpec FROM LesSpectacles")

        for spec in spectacles:
            self.ui.comboBox_gererRepresentation.addItem(str(spec[0]))

        # Ajoute une date minimum = date aujourd'hui
        now = datetime.now()
        self.ui.dateTimeEdit_gererRepresentation.setMinimumDate(now)
        self.ui.dateTimeEdit_gererRepresentation_modification.setMinimumDate(now)


    def ViderLabel_Aux(self,label):
        display.refreshLabel(label, "")

    #Permet de vider un label de son texte au bout de t secondes
    def ViderLabel(self,t,label):
        timer = threading.Timer(t, self.ViderLabel_Aux, args=[label])
        timer.start()



    # A chaque fois qu'on choisit un spectacle on affiche les représentations
    def refreshResult(self):
        try:
            cursor = self.data.cursor()

            cursor.execute("SELECT dateRep FROM LesRepresentations NATURAL JOIN LesSpectacles where nomSpec = ?",[self.ui.comboBox_gererRepresentation.currentText()])
            result = cursor.fetchall()

            # On régénère la liste des représentations
            self.ui.comboBox_2_gererRepresentation.clear()
            self.ui.comboBox_gererRepresentation_modification.clear()
            for res in result:
                dateRepTab = res[0].split(' ')[0].split('/') #Récupère jours/mois/année
                now = datetime.now()

                # On peut modifier/supprimer les spectacles qui n'ont pas encore eu lieus
                if now.year<int(dateRepTab[2]) or (now.year==int(dateRepTab[2]) and (now.month<int(dateRepTab[1]) or (now.month==int(dateRepTab[1]) and now.day<=int(dateRepTab[0])))) :
                    self.ui.comboBox_2_gererRepresentation.addItem(str(res[0]))
                    self.ui.comboBox_gererRepresentation_modification.addItem(str(res[0]))


            cursor.execute("SELECT dateRep,nomSpec FROM LesRepresentations NATURAL JOIN LesSpectacles order by dateRep")
            result = cursor.fetchall()
            i = display.refreshGenericData(self.ui.table_fct_gererRepresentation, result)
            if i == 0:
                display.refreshLabel(self.ui.label_gererRepresentation_res, "Aucun résultat")

        except Exception as e:
            display.refreshLabel(self.ui.label_gererRepresentation_res, "Impossible d'afficher les résultats : " + repr(e))


    #test si on peut ejouter modifier une représentation
    def TestAjouterRepresentation(self,dateRepAjouter):
        cursor = self.data.cursor()
        cursor.execute("SELECT noSpec from LesSpectacles where nomSpec = ?",[self.ui.comboBox_gererRepresentation.currentText()])
        noSpec =cursor.fetchone()[0]

        dateRepAjouterTab = dateRepAjouter.split('/')
        insertionPossible = 1

        # Il ne peut pas y avoir 2 fois le même spectacle en une journée
        cursor.execute("SELECT dateRep from LesRepresentations_base where noSpec = ? ", [str(noSpec)] )
        test = cursor.fetchall()
        #Pour chaque date récupérée
        for dateRep in test:
            dateRepTab = dateRep[0].split(' ')[0].split('/') #Récupère jours/mois/année
            if(dateRepTab[0]==dateRepAjouterTab[0] and dateRepTab[1]==dateRepAjouterTab[1] and dateRepTab[2]==dateRepAjouterTab[2] ):
                insertionPossible = 0

        # Il doit y avoir 4 heures entre le début d'un spectacle et le début du prochain spectacle
        cursor.execute("SELECT dateRep from LesRepresentations_base")
        test = cursor.fetchall()
        for dateRep in test:
            dateRepTab = dateRep[0].split(' ')[0].split('/') #Récupère jours/mois/année
            dateRepTab.extend(dateRep[0].split(' ')[1].split(':')) #Récupère heurs/minute
            if((abs(datetime(int(dateRepAjouterTab[2]),int(dateRepAjouterTab[1]),int(dateRepAjouterTab[0]),int(dateRepAjouterTab[3]),int(dateRepAjouterTab[4])) -
            datetime(int(dateRepTab[2]),int(dateRepTab[1]),int(dateRepTab[0]),int(dateRepTab[3]),int(dateRepTab[4]))).total_seconds()) < 3600*4 ):
                insertionPossible = -1

        return insertionPossible

    # On ajoute une représentation
    def AjouterRepresentation(self):
        try:
            cursor = self.data.cursor()
            cursor.execute("SELECT noSpec from LesSpectacles where nomSpec = ?",[self.ui.comboBox_gererRepresentation.currentText()])
            noSpec =cursor.fetchone()[0]

            dateRepAjouter = self.ui.dateTimeEdit_gererRepresentation.dateTime().toString("dd/MM/yyyy/hh/mm")

            insertionPossible = self.TestAjouterRepresentation(dateRepAjouter) #Vérifie si on peut insérer la représentation

            # Insertion possible
            if insertionPossible==1:
                cursor.execute("INSERT INTO LesRepresentations_base (noSpec,dateRep) VALUES( ?, ?)",
                [str(noSpec), self.ui.dateTimeEdit_gererRepresentation.dateTime().toString("dd/MM/yyyy hh:mm")])
                display.refreshLabel(self.ui.label_gererRepresentation_res, "Donnée ajoutée")
                self.ui.label_gererRepresentation_res.setStyleSheet("color:rgb(10, 120, 10)")
                self.AppliquerModification()
                self.refreshResult()
                self.ViderLabel(3,self.ui.label_gererRepresentation_res)
            elif insertionPossible==0:
                display.refreshLabel(self.ui.label_gererRepresentation_res, "Impossible d'ajouter: une représentation pour le même spectacle existe déjà ce jour-ci.")
                self.ui.label_gererRepresentation_res.setStyleSheet("color:rgb(120, 10, 10)")
            elif insertionPossible==-1:
                display.refreshLabel(self.ui.label_gererRepresentation_res, "Impossible d'ajouter: un spectacle est trop proche de celui que vous voulez ajouter.")
                self.ui.label_gererRepresentation_res.setStyleSheet("color:rgb(120, 10, 10)")

        except Exception as e:
            display.refreshLabel(self.ui.label_gererRepresentation_res, "Impossible d'ajouter " + repr(e))
            self.ui.label_gererRepresentation_res.setStyleSheet("color:rgb(120, 10, 10)")

    # Supprimer une représentation
    def SupprimerRepresentation(self):
        try:
            cursor = self.data.cursor()
            cursor.execute("SELECT noSpec from LesSpectacles where nomSpec = ?",[self.ui.comboBox_gererRepresentation.currentText()])
            noSpec =cursor.fetchone()[0]
            cursor.execute("DELETE from LesRepresentations_base WHERE dateRep = ? and noSpec = ? ",
            [self.ui.comboBox_2_gererRepresentation.currentText(), str(noSpec)])

            self.SupprimerTickets() # Supprime les tickets liées à la représentation, s'il y en a
            display.refreshLabel(self.ui.label_gererRepresentation_res, "Donnée supprimée")
            self.ui.label_gererRepresentation_res.setStyleSheet("color:rgb(10, 120, 10)")
            self.AppliquerModification()
            self.refreshResult()
            self.ViderLabel(3,self.ui.label_gererRepresentation_res)


        except Exception as e:
            display.refreshLabel(self.ui.label_gererRepresentation_res, "Impossible de supprimer " + repr(e))
            self.ui.label_gererRepresentation_res.setStyleSheet("color:rgb(120, 10, 10)")


    #Affiche le nombre de tickets qui seront supprimés
    def NombreTicketSupprimer(self):
        cursor = self.data.cursor()
        # Nombre de tickets pour la représentation
        cursor.execute("SELECT count() as nbPlaces from LesTickets where dateRep = ?",[self.ui.comboBox_2_gererRepresentation.currentText()])
        nbPlace = cursor.fetchone()[0]
        if int(nbPlace)==0:
            display.refreshLabel(self.ui.label_gererRepresentation_ticket, "0 ticket pour cette repésentation.")
            self.ui.label_gererRepresentation_ticket.setStyleSheet("color:rgb(10, 120, 10)")
        if int(nbPlace)==1:
            display.refreshLabel(self.ui.label_gererRepresentation_ticket, "Attention "+str(nbPlace)+" place sera supprimée")
            self.ui.label_gererRepresentation_ticket.setStyleSheet("color:rgb(120, 10, 10)")
        elif int(nbPlace)>1:
            display.refreshLabel(self.ui.label_gererRepresentation_ticket, "Attention "+str(nbPlace)+" places seront supprimées")
            self.ui.label_gererRepresentation_ticket.setStyleSheet("color:rgb(120, 10, 10)")

    #Affiche le nombre de tickets qui seront modifiés
    def NombreTicketModifier(self):
        cursor = self.data.cursor()
        # Nombre de tickets pour la représentation
        cursor.execute("SELECT count() as nbPlaces from LesTickets where dateRep = ?",[self.ui.comboBox_gererRepresentation_modification.currentText()])
        nbPlace = cursor.fetchone()[0]
        if int(nbPlace)==0:
            display.refreshLabel(self.ui.label_gererRepresentation_ticket, "0 ticket pour cette repésentation.")
            self.ui.label_gererRepresentation_ticket.setStyleSheet("color:rgb(10, 120, 10)")
        if int(nbPlace)==1:
            display.refreshLabel(self.ui.label_gererRepresentation_ticket, "Attention "+str(nbPlace)+" place sera modifée")
            self.ui.label_gererRepresentation_ticket.setStyleSheet("color:rgb(120, 10, 10)")
        elif int(nbPlace)>1:
            display.refreshLabel(self.ui.label_gererRepresentation_ticket, "Attention "+str(nbPlace)+" places seront modifiées")
            self.ui.label_gererRepresentation_ticket.setStyleSheet("color:rgb(120, 10, 10)")


    # Supprimer les tickets liées a la représentation
    # Bien évidemment on ne rembourse pas les tickets :)
    def SupprimerTickets(self):
        try:
            cursor = self.data.cursor()
            # Les tickets qu'on doit supprimer
            cursor.execute("SELECT dateRep,noPlace,noRang,noDos from LesTickets where dateRep = ?",[self.ui.comboBox_2_gererRepresentation.currentText()])
            tickets = cursor.fetchall()

            #S'il y a des tickets à supprimer
            if len(tickets)!=0:
                for ticket in tickets:
                    cursor.execute("DELETE FROM LesTickets WHERE dateRep = ? and noPlace = ? and noRang = ?",[ticket[0],ticket[1],ticket[2]])
            cursor.execute("DELETE FROM LesDossiers_base WHERE noDos = ?",[ticket[3]]) #Supprime le dossier correspondant
        except Exception as e:
            display.refreshLabel(self.ui.label_gererRepresentation_res, "Impossible de supprimer des tickets " + repr(e))
            self.ui.label_gererRepresentation_res.setStyleSheet("color:rgb(120, 10, 10)")



    #test si on peut modifier une représentation
    def TestModifierRepresentation(self,dateAModifier,dateRepAjouter):
        cursor = self.data.cursor()
        cursor.execute("SELECT noSpec from LesSpectacles where nomSpec = ?",[self.ui.comboBox_gererRepresentation.currentText()])
        noSpec =cursor.fetchone()[0]

        dateRepAjouterTab = dateRepAjouter.split('/')
        insertionPossible = 1

        # Il ne peut pas y avoir 2 fois le même spectacle en une journée,
        cursor.execute("SELECT dateRep from LesRepresentations_base where noSpec = ? and dateRep != ?", [str(noSpec),dateAModifier] )
        test = cursor.fetchall()
        #Pour chaque date récupérée
        for dateRep in test:
            dateRepTab = dateRep[0].split(' ')[0].split('/') #Récupère jours/mois/année
            if(dateRepTab[0]==dateRepAjouterTab[0] and dateRepTab[1]==dateRepAjouterTab[1] and dateRepTab[2]==dateRepAjouterTab[2] ):
                insertionPossible = 0

        # Il doit y avoir 4 heures entre le début d'un spectacle et le début du prochain spectacle
        cursor.execute("SELECT dateRep from LesRepresentations_base where dateRep != ?",[dateAModifier])
        test = cursor.fetchall()
        for dateRep in test:
            dateRepTab = dateRep[0].split(' ')[0].split('/') #Récupère jours/mois/année
            dateRepTab.extend(dateRep[0].split(' ')[1].split(':')) #Récupère heurs/minute
            if((abs(datetime(int(dateRepAjouterTab[2]),int(dateRepAjouterTab[1]),int(dateRepAjouterTab[0]),int(dateRepAjouterTab[3]),int(dateRepAjouterTab[4])) -
            datetime(int(dateRepTab[2]),int(dateRepTab[1]),int(dateRepTab[0]),int(dateRepTab[3]),int(dateRepTab[4]))).total_seconds()) < 3600*4 ):
                insertionPossible = -1

        return insertionPossible


    # Modifier la repésentation
    def ModifierRepresentation(self):
        try:
            #Vérifie si on peut faire la modification
            dateRepAjouter = self.ui.dateTimeEdit_gererRepresentation_modification.dateTime().toString("dd/MM/yyyy/hh/mm")
            dateRepBase = self.ui.comboBox_gererRepresentation_modification.currentText()
            modiPossible = self.TestModifierRepresentation(dateRepBase,dateRepAjouter) #Vérifie si on peut insérer la représentation

            # modification possible
            if modiPossible==1:
                cursor = self.data.cursor()
                cursor.execute("SELECT noSpec from LesSpectacles where nomSpec = ?",[self.ui.comboBox_gererRepresentation.currentText()])
                noSpec =cursor.fetchone()[0]
                cursor.execute("UPDATE LesRepresentations_base SET dateRep = ? WHERE dateRep = ? and noSpec = ? ",
                [self.ui.dateTimeEdit_gererRepresentation_modification.dateTime().toString("dd/MM/yyyy hh:mm"),
                self.ui.comboBox_gererRepresentation_modification.currentText(), str(noSpec)] )

                self.ModifierTickets() # Modifie les tickets liées à la représentation, s'il y en a
                display.refreshLabel(self.ui.label_gererRepresentation_res, "Donnée modifiée")
                self.ui.label_gererRepresentation_res.setStyleSheet("color:rgb(10, 120, 10)")
                self.AppliquerModification()
                self.refreshResult()
            elif modiPossible==0:
                display.refreshLabel(self.ui.label_gererRepresentation_res, "Impossible de modifier: une représentation pour le même spectacle existe déjà ce jour-ci.")
                self.ui.label_gererRepresentation_res.setStyleSheet("color:rgb(120, 10, 10)")
            elif modiPossible==-1:
                display.refreshLabel(self.ui.label_gererRepresentation_res, "Impossible de modifier: un spectacle est trop proche de celui que vous voulez ajouter.")
                self.ui.label_gererRepresentation_res.setStyleSheet("color:rgb(120, 10, 10)")

        except Exception as e:
            display.refreshLabel(self.ui.label_gererRepresentation_res, "Impossible de modifier " + repr(e))
            self.ui.label_gererRepresentation_res.setStyleSheet("color:rgb(120, 10, 10)")

    # Modifie les tickets liées a la représentation
    # Bien évidemment on ne prévient pas les gens de la modification :)
    def ModifierTickets(self):
        try:
            cursor = self.data.cursor()
            # Les tickets qu'on doit modifier
            cursor.execute("SELECT dateRep,noPlace,noRang from LesTickets where dateRep = ?",[self.ui.comboBox_2_gererRepresentation.currentText()])
            tickets = cursor.fetchall()

            #S'il y a des tickets à modifier
            if tickets!=None:
                for ticket in tickets:
                    cursor.execute("UPDATE LesTickets set dateRep=? WHERE dateRep=? and noPlace=? and noRang=?",
                    [self.ui.dateTimeEdit_gererRepresentation_modification.dateTime().toString("dd/MM/yyyy hh:mm"),ticket[0],ticket[1],ticket[2]])
        except Exception as e:
            display.refreshLabel(self.ui.label_gererRepresentation_res, "Impossible de supprimer des tickets " + repr(e))
            self.ui.label_gererRepresentation_res.setStyleSheet("color:rgb(120, 10, 10)")

    #Commit les résultats
    def AppliquerModification(self):
        self.data.commit()
