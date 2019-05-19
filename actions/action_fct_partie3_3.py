import sqlite3
from utils import display
from gui.fct_partie3_3 import Ui_fct_partie3_3
from PyQt5.QtWidgets import QDialog, QTableWidgetItem


class AppFctPartie3_3(QDialog):
    ui = Ui_fct_partie3_3()

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

            #Nombre Total de places
            placeTotal = cursor.execute("SELECT count(*)as placesTotal from LesPlaces")
            placeTotal =  placeTotal.fetchone()[0]

            # Récupère les représentations et le nombre de places réservée pour le spectacle choisi
            result = cursor.execute("SELECT nomSpec, dateRep, ? - nbPlaces FROM LesRepresentations NATURAL JOIN LesSpectacles",[placeTotal])


            i = display.refreshGenericData(self.ui.table_fct_partie3_3, result)
            if i == 0:
                display.refreshLabel(self.ui.label_fct_partie3_3_erreur, "Aucun résultat")

        except Exception as e:
            display.refreshLabel(self.ui.label_fct_partie3_3_erreur, "Impossible d'afficher les résultats : " + repr(e))
