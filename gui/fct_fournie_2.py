# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fct_fournie_2.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_fct_fournie_2(object):
    def setupUi(self, fct_fournie_2):
        fct_fournie_2.setObjectName("fct_fournie_2")
        fct_fournie_2.resize(478, 325)
        self.verticalLayout = QtWidgets.QVBoxLayout(fct_fournie_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(fct_fournie_2)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(fct_fournie_2)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.pushButton = QtWidgets.QPushButton(fct_fournie_2)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.table_fct_fournie_2 = QtWidgets.QTableWidget(fct_fournie_2)
        self.table_fct_fournie_2.setObjectName("table_fct_fournie_2")
        self.table_fct_fournie_2.setColumnCount(4)
        self.table_fct_fournie_2.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table_fct_fournie_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_fct_fournie_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_fct_fournie_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_fct_fournie_2.setHorizontalHeaderItem(3, item)
        self.table_fct_fournie_2.horizontalHeader().setDefaultSectionSize(70)
        self.table_fct_fournie_2.horizontalHeader().setMinimumSectionSize(50)
        self.table_fct_fournie_2.horizontalHeader().setStretchLastSection(True)
        self.table_fct_fournie_2.verticalHeader().setVisible(False)
        self.verticalLayout.addWidget(self.table_fct_fournie_2)
        self.label_fct_fournie_2 = QtWidgets.QLabel(fct_fournie_2)
        self.label_fct_fournie_2.setText("")
        self.label_fct_fournie_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_fct_fournie_2.setObjectName("label_fct_fournie_2")
        self.verticalLayout.addWidget(self.label_fct_fournie_2)

        self.retranslateUi(fct_fournie_2)
        self.pushButton.clicked.connect(fct_fournie_2.refreshResult)
        QtCore.QMetaObject.connectSlotsByName(fct_fournie_2)

    def retranslateUi(self, fct_fournie_2):
        _translate = QtCore.QCoreApplication.translate
        fct_fournie_2.setWindowTitle(_translate("fct_fournie_2", "Liste et prix des places d\'une zone"))
        self.label.setText(_translate("fct_fournie_2", "Saisissez une catégorie :"))
        self.pushButton.setText(_translate("fct_fournie_2", "Valider"))
        item = self.table_fct_fournie_2.horizontalHeaderItem(0)
        item.setText(_translate("fct_fournie_2", "noPlace"))
        item = self.table_fct_fournie_2.horizontalHeaderItem(1)
        item.setText(_translate("fct_fournie_2", "noRang"))
        item = self.table_fct_fournie_2.horizontalHeaderItem(2)
        item.setText(_translate("fct_fournie_2", "noZone"))
        item = self.table_fct_fournie_2.horizontalHeaderItem(3)
        item.setText(_translate("fct_fournie_2", "prixZone"))

