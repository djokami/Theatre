
import sqlite3
from utils import display
from gui.fct_fournie_2 import Ui_fct_fournie_2
from PyQt5.QtWidgets import QDialog

# Classe permettant d'afficher la fonction fournie 2
class AppFctFournie2(QDialog):

    ui = Ui_fct_fournie_2()

    #Constructeur
    def __init__(self, data:sqlite3.Connection):
        super(QDialog, self).__init__()
        self.ui.setupUi(self)
        self.data = data

    # Fonction de mise à jour de l'affichage
    def refreshResult(self):

        display.refreshLabel(self.ui.label_fct_fournie_2, "")

        try:
            if not self.ui.lineEdit.text().strip():
                display.refreshLabel(self.ui.label_fct_fournie_2, "Veuillez indiquer un nom de catégorie")
            else:
                cursor = self.data.cursor()
                result = cursor.execute("SELECT noPlace, noRang, noZone, prixZone FROM LesZones NATURAL JOIN LesPlaces WHERE catZone = ?", [self.ui.lineEdit.text().strip()])
                i = display.refreshGenericData(self.ui.table_fct_fournie_2, result)
                if i == 0:
                    display.refreshLabel(self.ui.label_fct_fournie_2, "Aucun résultat")

        except Exception as e:
            display.refreshLabel(self.ui.label_fct_fournie_2, "Impossible d'afficher les résultats : " + repr(e))