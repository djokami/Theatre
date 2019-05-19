# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fct_partie3_3.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_fct_partie3_3(object):
    def setupUi(self, fct_partie3_3):
        fct_partie3_3.setObjectName("fct_partie3_3")
        fct_partie3_3.resize(410, 263)
        self.verticalLayout = QtWidgets.QVBoxLayout(fct_partie3_3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_fct_partie3_3_enonce = QtWidgets.QLabel(fct_partie3_3)
        self.label_fct_partie3_3_enonce.setAlignment(QtCore.Qt.AlignCenter)
        self.label_fct_partie3_3_enonce.setWordWrap(True)
        self.label_fct_partie3_3_enonce.setObjectName("label_fct_partie3_3_enonce")
        self.verticalLayout.addWidget(self.label_fct_partie3_3_enonce)
        self.table_fct_partie3_3 = QtWidgets.QTableWidget(fct_partie3_3)
        self.table_fct_partie3_3.setObjectName("table_fct_partie3_3")
        self.table_fct_partie3_3.setColumnCount(3)
        self.table_fct_partie3_3.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table_fct_partie3_3.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_fct_partie3_3.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_fct_partie3_3.setHorizontalHeaderItem(2, item)
        self.table_fct_partie3_3.horizontalHeader().setVisible(True)
        self.table_fct_partie3_3.horizontalHeader().setCascadingSectionResizes(False)
        self.table_fct_partie3_3.horizontalHeader().setDefaultSectionSize(150)
        self.table_fct_partie3_3.horizontalHeader().setHighlightSections(True)
        self.table_fct_partie3_3.horizontalHeader().setMinimumSectionSize(40)
        self.table_fct_partie3_3.horizontalHeader().setSortIndicatorShown(False)
        self.table_fct_partie3_3.horizontalHeader().setStretchLastSection(True)
        self.table_fct_partie3_3.verticalHeader().setVisible(False)
        self.table_fct_partie3_3.verticalHeader().setCascadingSectionResizes(False)
        self.table_fct_partie3_3.verticalHeader().setSortIndicatorShown(False)
        self.table_fct_partie3_3.verticalHeader().setStretchLastSection(False)
        self.verticalLayout.addWidget(self.table_fct_partie3_3)
        self.label_fct_partie3_3_erreur = QtWidgets.QLabel(fct_partie3_3)
        self.label_fct_partie3_3_erreur.setText("")
        self.label_fct_partie3_3_erreur.setObjectName("label_fct_partie3_3_erreur")
        self.verticalLayout.addWidget(self.label_fct_partie3_3_erreur)

        self.retranslateUi(fct_partie3_3)
        QtCore.QMetaObject.connectSlotsByName(fct_partie3_3)

    def retranslateUi(self, fct_partie3_3):
        _translate = QtCore.QCoreApplication.translate
        fct_partie3_3.setWindowTitle(_translate("fct_partie3_3", "Nombre places réservées (ver 2) "))
        self.label_fct_partie3_3_enonce.setText(_translate("fct_partie3_3", "Pour chaque spectacle, donner ses représentations et le nombre de places réservées."))
        self.table_fct_partie3_3.setSortingEnabled(False)
        item = self.table_fct_partie3_3.horizontalHeaderItem(0)
        item.setText(_translate("fct_partie3_3", "nomSpec"))
        item = self.table_fct_partie3_3.horizontalHeaderItem(1)
        item.setText(_translate("fct_partie3_3", "dateRep"))
        item = self.table_fct_partie3_3.horizontalHeaderItem(2)
        item.setText(_translate("fct_partie3_3", "nbPlacesReserves"))

