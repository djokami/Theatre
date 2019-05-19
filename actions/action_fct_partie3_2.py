import sqlite3
from utils import display
from gui.fct_partie3_2 import Ui_fct_partie3_2
from PyQt5.QtWidgets import QDialog, QTableWidgetItem


class AppFctPartie3_2(QDialog):
    ui = Ui_fct_partie3_2()

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

            # Récupère les spectacles, représentations
            cursor.execute("SELECT noSpec,nomSpec,dateRep FROM LesRepresentations NATURAL JOIN LesSpectacles")
            representaions = cursor.fetchall()
            result=[]
            # Pour chaque représentation
            for repre in representaions:
                cursor.execute("SELECT nomSpec,dateRep,count(noPlace) as nbPlacesReservee FROM LesRepresentations NATURAL JOIN LesSpectacles NATURAL LEFT OUTER JOIN LesTickets\
                GROUP BY nomSpec,dateRep HAVING nomSpec=? and dateRep =?" ,(repre[1],repre[2]))
                result.append(cursor.fetchone())

            i = display.refreshGenericData(self.ui.table_fct_partie3_2, result)
            if i == 0:
                display.refreshLabel(self.ui.table_fct_partie3_2, "Aucun résultat")

        except Exception as e:
            display.refreshLabel(self.ui.label_fct_partie3_2_erreur, "Impossible d'afficher les résultats : " + repr(e))
