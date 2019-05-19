# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fct_comp_3.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_fct_comp_3(object):
    def setupUi(self, fct_comp_3):
        fct_comp_3.setObjectName("fct_comp_3")
        fct_comp_3.resize(400, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(fct_comp_3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(fct_comp_3)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(fct_comp_3)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.selectCategorie_fct_comp_3 = QtWidgets.QComboBox(fct_comp_3)
        self.selectCategorie_fct_comp_3.setObjectName("selectCategorie_fct_comp_3")
        self.horizontalLayout.addWidget(self.selectCategorie_fct_comp_3)
        self.pushButton = QtWidgets.QPushButton(fct_comp_3)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.table_fct_comp_3 = QtWidgets.QTableWidget(fct_comp_3)
        self.table_fct_comp_3.setObjectName("table_fct_comp_3")
        self.table_fct_comp_3.setColumnCount(3)
        self.table_fct_comp_3.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table_fct_comp_3.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_fct_comp_3.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_fct_comp_3.setHorizontalHeaderItem(2, item)
        self.table_fct_comp_3.horizontalHeader().setMinimumSectionSize(50)
        self.table_fct_comp_3.horizontalHeader().setStretchLastSection(True)
        self.table_fct_comp_3.verticalHeader().setVisible(False)
        self.verticalLayout.addWidget(self.table_fct_comp_3)
        self.label_fct_comp_3 = QtWidgets.QLabel(fct_comp_3)
        self.label_fct_comp_3.setText("")
        self.label_fct_comp_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_fct_comp_3.setObjectName("label_fct_comp_3")
        self.verticalLayout.addWidget(self.label_fct_comp_3)

        self.retranslateUi(fct_comp_3)
        self.pushButton.clicked.connect(fct_comp_3.refreshResult)
        QtCore.QMetaObject.connectSlotsByName(fct_comp_3)

    def retranslateUi(self, fct_comp_3):
        _translate = QtCore.QCoreApplication.translate
        fct_comp_3.setWindowTitle(_translate("fct_comp_3", "Liste des places d\'une catégorie (version 2)"))
        self.label.setText(_translate("fct_comp_3", "Travail à réaliser : améliorez l\'interface afin de proposer une liste des catégories possibles (issues de la base de données)."))
        self.label_2.setText(_translate("fct_comp_3", "Saisissez une catégorie :"))
        self.pushButton.setText(_translate("fct_comp_3", "Valider"))
        item = self.table_fct_comp_3.horizontalHeaderItem(0)
        item.setText(_translate("fct_comp_3", "noPlace"))
        item = self.table_fct_comp_3.horizontalHeaderItem(1)
        item.setText(_translate("fct_comp_3", "noRang"))
        item = self.table_fct_comp_3.horizontalHeaderItem(2)
        item.setText(_translate("fct_comp_3", "noZone"))

