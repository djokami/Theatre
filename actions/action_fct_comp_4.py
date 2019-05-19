
import sqlite3
from utils import display
from gui.fct_comp_4 import Ui_fct_comp_4
from PyQt5.QtWidgets import QDialog, QTableWidgetItem

# Classe permettant d'afficher la fonction à compléter 4
class AppFctComp4(QDialog):

    ui = Ui_fct_comp_4()

    # Constructeur
    def __init__(self, data:sqlite3.Connection):
        super(QDialog, self).__init__()
        self.ui.setupUi(self)
        self.data = data

        #Selectionne tout les numéro de dossiers
        cursor = self.data.cursor()
        result = cursor.execute("SELECT noDos FROM LesDossiers_base")

        for noDos in result:
            self.ui.comboBox_4_noDos.addItem(str(noDos[0]))


    # A chaque fois qu'on change de dossier on recharge les catégories
    def refreshCat(self):
        #Supprime les catégories qui sont dans la sélection
        self.ui.comboBox_4_categorie.clear()

        try:
            #On récupère les catégories correspondant au dossier courant
            cursor = self.data.cursor()
            result = cursor.execute("SELECT distinct catZone from LesTickets natural join LesPlaces natural join LesZones where noDos = ?",
            self.ui.comboBox_4_noDos.currentText())

            #On les affiche
            for cat in result:
                self.ui.comboBox_4_categorie.addItem(cat[0])

        except Exception as e:
            display.refreshLabel(self.ui.label_fct_comp_4, "Impossible d'afficher les résultats : " + repr(e))


    # Fonction de mise à jour de l'affichage
    def refreshResult(self):
        # TODO 4 Fait : fonction à modifier pour que le numéro de dossier ne puisse être choisi que parmi ceux présents dans la base et que la catégorie ne propose que des valeurs possibles pour le dossier choisi, une fois le fichier ui correspondant mis à jour
        try:
            display.refreshLabel(self.ui.label_fct_comp_4, "")
            cursor = self.data.cursor()

            result = cursor.execute(
                "SELECT * FROM LesTickets NATURAL JOIN LesPlaces NATURAL JOIN LesZones WHERE noDos = ? AND catZone=?",
                [self.ui.comboBox_4_noDos.currentText(),self.ui.comboBox_4_categorie.currentText()]
            )
            i = display.refreshGenericData(self.ui.table_fct_comp_4, result)
            if i == 0:
                display.refreshLabel(self.ui.label_fct_comp_4, "Aucun résultat")

        except Exception as e:
            display.refreshLabel(self.ui.label_fct_comp_4, "Impossible d'afficher les résultats : " + repr(e))
