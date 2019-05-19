
import sqlite3
from utils import display
from gui.fct_comp_1 import Ui_fct_comp_1
from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import pyqtSlot

# Classe permettant d'afficher la fonction à compléter 1
class AppFctComp1(QDialog):

    ui = Ui_fct_comp_1()

    # Constructeur
    def __init__(self, data:sqlite3.Connection):
        super(QDialog, self).__init__()
        self.ui.setupUi(self)
        self.data = data
        self.refreshResult()

    # Fonction de mise à joru de l'affichage
    @pyqtSlot()
    def refreshResult(self):

        try:
            display.refreshLabel(self.ui.label_fct_comp_1, "")
            cursor = self.data.cursor()
            # TODO 1 Fait : mettre à jour la requête et changer aussi le fichier ui correspondant
            result = cursor.execute("SELECT noSpec, dateRep, noPlace, noRang, dateEmTick, noDos FROM LesTickets")
            display.refreshGenericData(self.ui.table_fct_comp_1, result)
        except Exception as e:
            display.refreshLabel(self.ui.label_fct_comp_1, "Impossible d'afficher les résultats : " + repr(e))
