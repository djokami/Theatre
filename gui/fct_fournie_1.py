# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fct_fournie_1.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_fct_fournie_1(object):
    def setupUi(self, fct_fournie_1):
        fct_fournie_1.setObjectName("fct_fournie_1")
        fct_fournie_1.resize(561, 601)
        self.verticalLayout = QtWidgets.QVBoxLayout(fct_fournie_1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.table_fct_fournie_1 = QtWidgets.QTableWidget(fct_fournie_1)
        self.table_fct_fournie_1.setObjectName("table_fct_fournie_1")
        self.table_fct_fournie_1.setColumnCount(2)
        self.table_fct_fournie_1.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table_fct_fournie_1.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_fct_fournie_1.setHorizontalHeaderItem(1, item)
        self.table_fct_fournie_1.horizontalHeader().setDefaultSectionSize(200)
        self.table_fct_fournie_1.horizontalHeader().setMinimumSectionSize(50)
        self.table_fct_fournie_1.horizontalHeader().setStretchLastSection(True)
        self.table_fct_fournie_1.verticalHeader().setVisible(False)
        self.verticalLayout.addWidget(self.table_fct_fournie_1)
        self.label_fct_fournie_1 = QtWidgets.QLabel(fct_fournie_1)
        self.label_fct_fournie_1.setText("")
        self.label_fct_fournie_1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_fct_fournie_1.setObjectName("label_fct_fournie_1")
        self.verticalLayout.addWidget(self.label_fct_fournie_1)

        self.retranslateUi(fct_fournie_1)
        QtCore.QMetaObject.connectSlotsByName(fct_fournie_1)

    def retranslateUi(self, fct_fournie_1):
        _translate = QtCore.QCoreApplication.translate
        fct_fournie_1.setWindowTitle(_translate("fct_fournie_1", "Liste des représentations de \"How to be a parisian ?\""))
        item = self.table_fct_fournie_1.horizontalHeaderItem(0)
        item.setText(_translate("fct_fournie_1", "nomSpec"))
        item = self.table_fct_fournie_1.horizontalHeaderItem(1)
        item.setText(_translate("fct_fournie_1", "dateRep"))

