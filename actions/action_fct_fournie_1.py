
import sqlite3
from utils import display
from gui.fct_fournie_1 import Ui_fct_fournie_1
from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import pyqtSlot

# Classe permettant d'afficher la fonction fournie 1
class AppFctFournie1(QDialog):

    ui = Ui_fct_fournie_1()

    # Constructeur
    def __init__(self, data:sqlite3.Connection):
        super(QDialog, self).__init__()
        self.ui.setupUi(self)
        self.data = data
        self.refreshResult()

    # Fonction de mise à jour de l'affichage
    @pyqtSlot()
    def refreshResult(self):

        display.refreshLabel(self.ui.label_fct_fournie_1, "")

        try:
            cursor = self.data.cursor()
            result = cursor.execute("SELECT nomSpec, dateRep FROM LesSpectacles NATURAL JOIN LesRepresentations_base WHERE noSpec = 1")
            display.refreshGenericData(self.ui.table_fct_fournie_1, result)
        except Exception as e:
            display.refreshLabel(self.ui.label_fct_fournie_1, "Impossible d'afficher les résultats : " + repr(e))
