import sqlite3
from utils import display
from gui.fct_gererTicket import Ui_fct_gererTicket
from PyQt5.QtWidgets import QDialog, QTableWidgetItem
from datetime import datetime



class AppFctGererTicket(QDialog):
    ui = Ui_fct_gererTicket()

    # Constructeur
    def __init__(self, data:sqlite3.Connection):
        super(QDialog, self).__init__()
        self.ui.setupUi(self)
        self.data = data

        self.panier = [] #Contient les places ajoutées
        self.maintenant = datetime.now()

        cursor = self.data.cursor()
        self.noDos = cursor.execute("SELECT max(noDos)+1 from LesDossiers_base").fetchone()[0]
        cursor.execute("INSERT INTO LesDossiers_base (noDos) VALUES (?)",[self.noDos])


        self.genererSpectacle()


    def genererSpectacle(self):
        cursor = self.data.cursor()
        # On ajoute les spectacles dans le comboBox
        spectacles = cursor.execute("SELECT nomSpec FROM LesSpectacles")
        self.ui.comboBox_gererTicket_spectacle.clear()
        for spec in spectacles:
            self.ui.comboBox_gererTicket_spectacle.addItem(str(spec[0]))


    # A chaque fois qu'on choisit un spectacle on affiche les représentations
    def genererRepresentation(self):
        try:
            cursor = self.data.cursor()

            cursor.execute("SELECT dateRep FROM LesRepresentations NATURAL JOIN LesSpectacles where nomSpec = ? and nbPlaces > 0",[self.ui.comboBox_gererTicket_spectacle.currentText()])
            result = cursor.fetchall()

            # On régénère la liste des représentations
            self.ui.comboBox_gererTicket_representation.clear()
            for res in result:
                dateRepTab = res[0].split(' ')[0].split('/') #Récupère jours/mois/année
                now = datetime.now()

                # On ne peut pas acheter des tickets pour des représetations passées
            #    if now.year<int(dateRepTab[2]) or (now.year==int(dateRepTab[2]) and (now.month<int(dateRepTab[1]) or (now.month==int(dateRepTab[1]) and now.day<=int(dateRepTab[0])))) :
                self.ui.comboBox_gererTicket_representation.addItem(str(res[0]))

        except Exception as e:
            display.refreshLabel(self.ui.label_gererRepresentation_res, "Impossible d'afficher les résultats : " + repr(e))
            self.ui.label_gererTicket_res.setStyleSheet("color:rgb(10, 120, 10)")


    # A chaque fois qu'on choisit une représentation on met à jour les rangs disponibles
    def genererNumRang(self):
        try:
            cursor = self.data.cursor()
            self.ui.comboBox_gererTicket_rang.clear()
            cursor.execute("SELECT distinct noRang from (SELECT noPlace,noRang FROM LesPlaces EXCEPT SELECT noPlace, noRang FROM LesTickets where dateRep = ?) order by noRang"
            ,[self.ui.comboBox_gererTicket_representation.currentText()])
            rang = cursor.fetchall()

            for r in rang:
                self.ui.comboBox_gererTicket_rang.addItem(str(r[0]))

        except Exception as e:
            display.refreshLabel(self.ui.label_gererRepresentation_res, "Impossible d'afficher les résultats : " + repr(e))
            self.ui.label_gererTicket_res.setStyleSheet("color:rgb(10, 120, 10)")



    # A chaque fois qu'on choisit une représentation on met à jour les places disponibles
    def genererNumPlace(self):
        try:
            cursor = self.data.cursor()
            self.ui.comboBox_gererTicket_place.clear()
            cursor.execute("SELECT distinct noplace from (SELECT noPlace,noRang FROM LesPlaces EXCEPT SELECT noPlace, noRang FROM LesTickets where dateRep = ?) where  noRang = ?"
            ,[self.ui.comboBox_gererTicket_representation.currentText(), self.ui.comboBox_gererTicket_rang.currentText()])
            place = cursor.fetchall()

            for p in place:
                self.ui.comboBox_gererTicket_place.addItem(str(p[0]))

        except Exception as e:
            display.refreshLabel(self.ui.label_gererRepresentation_res, "Impossible d'afficher les résultats : " + repr(e))
            self.ui.label_gererTicket_res.setStyleSheet("color:rgb(120, 10, 10)")


    # Permet d'ajouter une place au panier
    def ajouterPlace(self):
        cursor = self.data.cursor()
        ticket = []
        ticket.append(self.ui.comboBox_gererTicket_spectacle.currentText())
        ticket.append(self.ui.comboBox_gererTicket_representation.currentText())
        ticket.append(self.ui.comboBox_gererTicket_rang.currentText())
        ticket.append(self.ui.comboBox_gererTicket_place.currentText())

        # Récupère le prix du ticket
        cursor.execute("SELECT prixZone from LesPlaces natural join LesZones where noPlace= ? and noRang = ?",[ticket[3],ticket[2]])
        ticket.append(int(cursor.fetchone()[0]))
        self.panier.append(ticket)

        cursor.execute("SELECT noSpec from LesSpectacles where nomSpec = ?",[ticket[0]])
        noSpec = cursor.fetchone()[0]
        cursor.execute("INSERT INTO LesTickets (noSpec,dateRep,noRang,noPlace,dateEmTick,noDos) values (?,?,?,?,?,?)",
        [noSpec,ticket[1],ticket[2],ticket[3],self.maintenant,self.noDos])

        cursor.execute("SELECT Montant from LesDossiers where noDos = ?",[self.noDos])
        display.refreshLabel(self.ui.label_prixTotal,"Prix total: "+str(cursor.fetchone()[0]) )

        self.affichagePanier()
        #Enlève le numéro de place sélectionné
        self.ui.comboBox_gererTicket_place.removeItem(self.ui.comboBox_gererTicket_place.currentIndex())
        #Enlève le num rang s'il n'y a plus de place
        if self.ui.comboBox_gererTicket_place.count() == 0:
            self.ui.comboBox_gererTicket_rang.removeItem(self.ui.comboBox_gererTicket_rang.currentIndex())
        #Enlève la représentation s'il n'y a plus de rang
        if self.ui.comboBox_gererTicket_rang.count() == 0:
            self.ui.comboBox_gererTicket_representation.removeItem(self.ui.comboBox_gererTicket_representation.currentIndex())
        #Enlève le spectacle s'il n'y a plus de représentation
        if self.ui.comboBox_gererTicket_representation.count() == 0:
            self.ui.comboBox_gererTicket_spectacle.removeItem(self.ui.comboBox_gererTicket_spectacle.currentIndex())

    # Mise à jour de l'affichage du panier
    def affichagePanier(self):
        display.refreshGenericData(self.ui.table_fct_gererTicket, self.panier)

    # Valide toutes les transactions
    def validerPanier(self):
        # Nouvelle date et numéro de dossier
        if len(self.panier)!=0: #Seulement si on
            self.data.commit()
            self.maintenant = datetime.now()
            self.noDos = self.data.cursor().execute("SELECT max(noDos)+1 from LesDossiers_base").fetchone()[0]
            self.data.cursor().execute("INSERT INTO LesDossiers_base (noDos) VALUES (?)",[self.noDos])

            #Regénère l'affichage
            self.genererRepresentation()
            self.panier=[]
            self.affichagePanier()
            self.genererNumRang()
            self.genererNumPlace()

            display.refreshLabel(self.ui.label_gererTicket_res, "Achat réalisé avec succés!")
            self.ui.label_gererTicket_res.setStyleSheet("color:rgb(10, 120, 10)")

        else :
            display.refreshLabel(self.ui.label_gererTicket_res, "Merci de n'avoir rien acheté!")
            self.ui.label_gererTicket_res.setStyleSheet("color:rgb(10, 120, 10)")

    # Valide toutes les transactions
    def annulerPanier(self):
        self.panier=[]
        self.affichagePanier()
        self.data.rollback()
        self.genererSpectacle()
        self.genererRepresentation()
        self.genererNumRang()
        self.genererNumPlace()
        display.refreshLabel(self.ui.label_gererTicket_res, "Panier vidé avec succés!")
        self.ui.label_gererTicket_res.setStyleSheet("color:rgb(10, 120, 10)")

    # Force un rollback si l'utilisateur ferme la fenêtre sans annuler ou valider
    def closeEvent(self, event):
        self.data.rollback()
