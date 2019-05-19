
import sqlite3
from utils import display
from gui.fct_comp_3 import Ui_fct_comp_3
from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import pyqtSlot

# Classe permettant d'afficher la fonction à compléter 3
class AppFctComp3(QDialog):

    ui = Ui_fct_comp_3()

    # Constructeur
    def __init__(self, data:sqlite3.Connection):
        super(QDialog, self).__init__()
        self.ui.setupUi(self)
        self.data = data


        # Recherche toutes les catégorie disponibles
        cursor = self.data.cursor()
        result = cursor.execute("SELECT DISTINCT catZone FROM LesZones")

        # Pour chaque catégorie on l'ajoute au combo box
        for cat in result:
            self.ui.selectCategorie_fct_comp_3.addItem(cat[0])



    # Fonction de mise à jour de l'affichage
    @pyqtSlot()
    def refreshResult(self):
        # TODO 3 Fait: fonction à modifier pour remplacer la zone de saisie par une liste de valeurs issues de la BD une fois le fichier ui correspondant mis à jour
        try:
            display.refreshLabel(self.ui.label_fct_comp_3, "")

            cursor = self.data.cursor()
            result = cursor.execute(
                "SELECT noPlace, noRang, noZone, prixZone FROM LesZones NATURAL JOIN LesPlaces WHERE catZone = ?",
                [self.ui.selectCategorie_fct_comp_3.currentText()])
            i = display.refreshGenericData(self.ui.table_fct_comp_3, result)
            if i == 0:
                display.refreshLabel(self.ui.label_fct_comp_3, "Aucun résultat")

        except Exception as e:
            display.refreshLabel(self.ui.label_fct_comp_3, "Impossible d'afficher les résultats : " + repr(e))
