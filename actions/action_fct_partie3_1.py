import sqlite3
from utils import display
from gui.fct_partie3_1 import Ui_fct_partie3_1
from PyQt5.QtWidgets import QDialog, QTableWidgetItem


class AppFctPartie3_1(QDialog):
    ui = Ui_fct_partie3_1()

    # Constructeur
    def __init__(self, data:sqlite3.Connection):
        super(QDialog, self).__init__()
        self.ui.setupUi(self)
        self.data = data

        self.refreshResult()


    # Fonction de mise à jour de l'affichage
    def refreshResult(self):
        try:
            cursor = self.data.cursor()
            result = cursor.execute("SELECT nomSpec,dateRep from LesRepresentations NATURAL JOIN LesSpectacles where nbPlaces in (select count(*) from LesPlaces)")
            i = display.refreshGenericData(self.ui.table_fct_partie3_1, result)
            if i == 0:
                display.refreshLabel(self.ui.label_fct_partie3_1_erreur, "Aucun résultat")

        except Exception as e:
            display.refreshLabel(self.ui.label_fct_partie3_1_erreur, "Impossible d'afficher les résultats : " + repr(e))
