
import sqlite3
from utils import display
from gui.fct_comp_2 import Ui_fct_comp_2
from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import pyqtSlot

# Classe permettant d'afficher la fonction à compléter 2
class AppFctComp2(QDialog):

    ui = Ui_fct_comp_2()

    # Constructeur
    def __init__(self, data:sqlite3.Connection):
        super(QDialog, self).__init__()
        self.ui.setupUi(self)
        self.data = data

    # Fonction de mise à jour de l'affichage
    @pyqtSlot()
    def refreshResult(self):
        # TODO 2 Fait : fonction à modifier pour remplacer la zone de saisie par une liste de valeurs prédéfinies dans l'interface une fois le fichier ui correspondant mis à jour
        try:
            display.refreshLabel(self.ui.label_fct_comp_2, "")
            cursor = self.data.cursor()

            result = cursor.execute(
                "SELECT noPlace, noRang, noZone, prixZone FROM LesZones NATURAL JOIN LesPlaces WHERE catZone = ?",
                [self.ui.selectCategorie_fct_comp_2.currentText()])
            i = display.refreshGenericData(self.ui.table_fct_comp_2, result)
            if i == 0:
                display.refreshLabel(self.ui.label_fct_comp_2, "Aucun résultat")

        except Exception as e:
            display.refreshLabel(self.ui.label_fct_comp_2, "Impossible d'afficher les résultats : " + repr(e))
