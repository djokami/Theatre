# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fct_partie3_2.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_fct_partie3_2(object):
    def setupUi(self, fct_partie3_2):
        fct_partie3_2.setObjectName("fct_partie3_2")
        fct_partie3_2.resize(595, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(fct_partie3_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_fct_partie3_2_enonce = QtWidgets.QLabel(fct_partie3_2)
        self.label_fct_partie3_2_enonce.setAlignment(QtCore.Qt.AlignCenter)
        self.label_fct_partie3_2_enonce.setWordWrap(True)
        self.label_fct_partie3_2_enonce.setObjectName("label_fct_partie3_2_enonce")
        self.verticalLayout.addWidget(self.label_fct_partie3_2_enonce)
        self.table_fct_partie3_2 = QtWidgets.QTableWidget(fct_partie3_2)
        self.table_fct_partie3_2.setObjectName("table_fct_partie3_2")
        self.table_fct_partie3_2.setColumnCount(3)
        self.table_fct_partie3_2.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table_fct_partie3_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_fct_partie3_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_fct_partie3_2.setHorizontalHeaderItem(2, item)
        self.table_fct_partie3_2.horizontalHeader().setMinimumSectionSize(50)
        self.table_fct_partie3_2.horizontalHeader().setSortIndicatorShown(False)
        self.table_fct_partie3_2.horizontalHeader().setStretchLastSection(True)
        self.table_fct_partie3_2.verticalHeader().setVisible(False)
        self.table_fct_partie3_2.verticalHeader().setCascadingSectionResizes(False)
        self.verticalLayout.addWidget(self.table_fct_partie3_2)
        self.label_fct_partie3_2_erreur = QtWidgets.QLabel(fct_partie3_2)
        self.label_fct_partie3_2_erreur.setText("")
        self.label_fct_partie3_2_erreur.setObjectName("label_fct_partie3_2_erreur")
        self.verticalLayout.addWidget(self.label_fct_partie3_2_erreur)

        self.retranslateUi(fct_partie3_2)
        QtCore.QMetaObject.connectSlotsByName(fct_partie3_2)

    def retranslateUi(self, fct_partie3_2):
        _translate = QtCore.QCoreApplication.translate
        fct_partie3_2.setWindowTitle(_translate("fct_partie3_2", "Nombre places réservées (ver 1) "))
        self.label_fct_partie3_2_enonce.setText(_translate("fct_partie3_2", "Pour chaque spectacle, donner ses représentations et le nombre de places réservées."))
        item = self.table_fct_partie3_2.horizontalHeaderItem(0)
        item.setText(_translate("fct_partie3_2", "nomSpec"))
        item = self.table_fct_partie3_2.horizontalHeaderItem(1)
        item.setText(_translate("fct_partie3_2", "dateRep"))
        item = self.table_fct_partie3_2.horizontalHeaderItem(2)
        item.setText(_translate("fct_partie3_2", "nbPlacesReserves"))

