
import sqlite3
from utils import display
from gui.tablesData import Ui_tablesData
from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import pyqtSlot

# Classe permettant d'afficher la fenêtre de visualisation des données
class AppTablesData(QDialog):

    ui = Ui_tablesData()

    # Constructeur
    def __init__(self, data:sqlite3.Connection):
        super(QDialog, self).__init__()
        self.ui.setupUi(self)
        self.data = data

        # On met à jour l'affichage avec les données actuellement présentes dans la base
        self.refreshAllTables()

    ####################################################################################################################
    # Méthodes permettant de rafraichir les différentes tables
    ####################################################################################################################

    # Fonction de mise à jour de l'affichage d'une seule table
    def refreshTable(self, label, table, query):
        display.refreshLabel(label, "")
        try:
            cursor = self.data.cursor()
            result = cursor.execute(query)
            display.refreshGenericData(table, result)
        except Exception as e:
            display.refreshLabel(label, "Impossible d'afficher les données de la table : " + repr(e))

    # Fonction permettant de mettre à jour toutes les tables
    @pyqtSlot()
    def refreshAllTables(self):
        # TODO 1b Fait : modifier les ui et les requêtes pour affichage des vues LesDossiers et LesRepresentations
        self.refreshTable(self.ui.label_spectacles, self.ui.tableSpectacles, "SELECT noSpec, nomSpec FROM LesSpectacles")
        self.refreshTable(self.ui.label_zones, self.ui.tableZones, "SELECT noZone, catZone, prixZone  FROM LesZones")
        self.refreshTable(self.ui.label_representations, self.ui.tableRepresentations, "SELECT noSpec, dateRep FROM LesRepresentations_base")
        self.refreshTable(self.ui.label_places, self.ui.tablePlaces, "SELECT noPlace, noRang, noZone FROM LesPlaces")
        self.refreshTable(self.ui.label_dossiers, self.ui.tableDossiers, "SELECT noDos FROM LesDossiers_base")
        self.refreshTable(self.ui.label_tickets, self.ui.tableTickets, "SELECT noSpec, dateRep, noPlace, noRang, dateEmTick, noDos FROM LesTickets")
        self.refreshTable(self.ui.label_vueDossier, self.ui.tableVueLesDossiers, "SELECT noDOs, montant FROM LesDossiers")
        self.refreshTable(self.ui.label_vueLesRepresentations, self.ui.tableVueLesRepresentations, "SELECT noSpec,dateRep,nbPlaces FROM LesRepresentations")
