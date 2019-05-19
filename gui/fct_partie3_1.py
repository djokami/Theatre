# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fct_partie3_1.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_fct_partie3_1(object):
    def setupUi(self, fct_partie3_1):
        fct_partie3_1.setObjectName("fct_partie3_1")
        fct_partie3_1.resize(400, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(fct_partie3_1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_fct_partie3_1_enonce = QtWidgets.QLabel(fct_partie3_1)
        self.label_fct_partie3_1_enonce.setObjectName("label_fct_partie3_1_enonce")
        self.verticalLayout.addWidget(self.label_fct_partie3_1_enonce)
        self.table_fct_partie3_1 = QtWidgets.QTableWidget(fct_partie3_1)
        self.table_fct_partie3_1.setAcceptDrops(False)
        self.table_fct_partie3_1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.table_fct_partie3_1.setLineWidth(1)
        self.table_fct_partie3_1.setCornerButtonEnabled(True)
        self.table_fct_partie3_1.setObjectName("table_fct_partie3_1")
        self.table_fct_partie3_1.setColumnCount(2)
        self.table_fct_partie3_1.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table_fct_partie3_1.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_fct_partie3_1.setHorizontalHeaderItem(1, item)
        self.table_fct_partie3_1.horizontalHeader().setMinimumSectionSize(50)
        self.table_fct_partie3_1.horizontalHeader().setSortIndicatorShown(False)
        self.table_fct_partie3_1.horizontalHeader().setStretchLastSection(True)
        self.table_fct_partie3_1.verticalHeader().setVisible(False)
        self.verticalLayout.addWidget(self.table_fct_partie3_1)
        self.label_fct_partie3_1_erreur = QtWidgets.QLabel(fct_partie3_1)
        self.label_fct_partie3_1_erreur.setText("")
        self.label_fct_partie3_1_erreur.setObjectName("label_fct_partie3_1_erreur")
        self.verticalLayout.addWidget(self.label_fct_partie3_1_erreur)

        self.retranslateUi(fct_partie3_1)
        QtCore.QMetaObject.connectSlotsByName(fct_partie3_1)

    def retranslateUi(self, fct_partie3_1):
        _translate = QtCore.QCoreApplication.translate
        fct_partie3_1.setWindowTitle(_translate("fct_partie3_1", "Représentations sans places réservées"))
        self.label_fct_partie3_1_enonce.setText(_translate("fct_partie3_1", "Les représentations sans places réservées."))
        self.table_fct_partie3_1.setSortingEnabled(False)
        item = self.table_fct_partie3_1.horizontalHeaderItem(0)
        item.setText(_translate("fct_partie3_1", "NomSpectacle"))
        item = self.table_fct_partie3_1.horizontalHeaderItem(1)
        item.setText(_translate("fct_partie3_1", "dateReprésentation"))

