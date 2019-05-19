# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fct_comp_1.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_fct_comp_1(object):
    def setupUi(self, fct_comp_1):
        fct_comp_1.setObjectName("fct_comp_1")
        fct_comp_1.resize(576, 318)
        self.verticalLayout = QtWidgets.QVBoxLayout(fct_comp_1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(fct_comp_1)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.table_fct_comp_1 = QtWidgets.QTableWidget(fct_comp_1)
        self.table_fct_comp_1.setObjectName("table_fct_comp_1")
        self.table_fct_comp_1.setColumnCount(6)
        self.table_fct_comp_1.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table_fct_comp_1.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_fct_comp_1.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_fct_comp_1.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_fct_comp_1.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_fct_comp_1.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_fct_comp_1.setHorizontalHeaderItem(5, item)
        self.table_fct_comp_1.horizontalHeader().setDefaultSectionSize(100)
        self.table_fct_comp_1.horizontalHeader().setMinimumSectionSize(50)
        self.table_fct_comp_1.horizontalHeader().setStretchLastSection(True)
        self.table_fct_comp_1.verticalHeader().setVisible(False)
        self.verticalLayout.addWidget(self.table_fct_comp_1)
        self.label_fct_comp_1 = QtWidgets.QLabel(fct_comp_1)
        self.label_fct_comp_1.setText("")
        self.label_fct_comp_1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_fct_comp_1.setObjectName("label_fct_comp_1")
        self.verticalLayout.addWidget(self.label_fct_comp_1)

        self.retranslateUi(fct_comp_1)
        QtCore.QMetaObject.connectSlotsByName(fct_comp_1)

    def retranslateUi(self, fct_comp_1):
        _translate = QtCore.QCoreApplication.translate
        fct_comp_1.setWindowTitle(_translate("fct_comp_1", "Afficher les détails des tickets"))
        self.label_2.setText(_translate("fct_comp_1", "Travail à réaliser : ajouter la date d\'émission des tickets ainsi que leur numéro de dossier."))
        item = self.table_fct_comp_1.horizontalHeaderItem(0)
        item.setText(_translate("fct_comp_1", "noSpec"))
        item = self.table_fct_comp_1.horizontalHeaderItem(1)
        item.setText(_translate("fct_comp_1", "dateRep"))
        item = self.table_fct_comp_1.horizontalHeaderItem(2)
        item.setText(_translate("fct_comp_1", "noPlace"))
        item = self.table_fct_comp_1.horizontalHeaderItem(3)
        item.setText(_translate("fct_comp_1", "noRang"))
        item = self.table_fct_comp_1.horizontalHeaderItem(4)
        item.setText(_translate("fct_comp_1", "dateEmTicket"))
        item = self.table_fct_comp_1.horizontalHeaderItem(5)
        item.setText(_translate("fct_comp_1", "noDos"))

