# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fct_comp_2.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_fct_comp_2(object):
    def setupUi(self, fct_comp_2):
        fct_comp_2.setObjectName("fct_comp_2")
        fct_comp_2.resize(400, 300)
        fct_comp_2.setWindowOpacity(9.0)
        self.verticalLayout = QtWidgets.QVBoxLayout(fct_comp_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(fct_comp_2)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtWidgets.QLabel(fct_comp_2)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.selectCategorie_fct_comp_2 = QtWidgets.QComboBox(fct_comp_2)
        self.selectCategorie_fct_comp_2.setObjectName("selectCategorie_fct_comp_2")
        self.selectCategorie_fct_comp_2.addItem("")
        self.selectCategorie_fct_comp_2.addItem("")
        self.horizontalLayout.addWidget(self.selectCategorie_fct_comp_2)
        self.pushButton_fct_comp_2 = QtWidgets.QPushButton(fct_comp_2)
        self.pushButton_fct_comp_2.setObjectName("pushButton_fct_comp_2")
        self.horizontalLayout.addWidget(self.pushButton_fct_comp_2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.table_fct_comp_2 = QtWidgets.QTableWidget(fct_comp_2)
        self.table_fct_comp_2.setObjectName("table_fct_comp_2")
        self.table_fct_comp_2.setColumnCount(3)
        self.table_fct_comp_2.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table_fct_comp_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_fct_comp_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_fct_comp_2.setHorizontalHeaderItem(2, item)
        self.table_fct_comp_2.horizontalHeader().setMinimumSectionSize(50)
        self.table_fct_comp_2.horizontalHeader().setStretchLastSection(True)
        self.table_fct_comp_2.verticalHeader().setVisible(False)
        self.verticalLayout.addWidget(self.table_fct_comp_2)
        self.label_fct_comp_2 = QtWidgets.QLabel(fct_comp_2)
        self.label_fct_comp_2.setText("")
        self.label_fct_comp_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_fct_comp_2.setObjectName("label_fct_comp_2")
        self.verticalLayout.addWidget(self.label_fct_comp_2)

        self.retranslateUi(fct_comp_2)
        self.pushButton_fct_comp_2.clicked.connect(fct_comp_2.refreshResult)
        QtCore.QMetaObject.connectSlotsByName(fct_comp_2)

    def retranslateUi(self, fct_comp_2):
        _translate = QtCore.QCoreApplication.translate
        fct_comp_2.setWindowTitle(_translate("fct_comp_2", "Liste des places d\'une catégorie (version 1)"))
        self.label.setText(_translate("fct_comp_2", "Travail à réaliser : améliorez l\'interface afin de proposer une liste des catégories possibles (saisies en dur)."))
        self.label_3.setText(_translate("fct_comp_2", "Saisissez une catégorie :"))
        self.selectCategorie_fct_comp_2.setItemText(0, _translate("fct_comp_2", "balcon"))
        self.selectCategorie_fct_comp_2.setItemText(1, _translate("fct_comp_2", "orchestre"))
        self.pushButton_fct_comp_2.setText(_translate("fct_comp_2", "Valider"))
        item = self.table_fct_comp_2.horizontalHeaderItem(0)
        item.setText(_translate("fct_comp_2", "noPlace"))
        item = self.table_fct_comp_2.horizontalHeaderItem(1)
        item.setText(_translate("fct_comp_2", "noRang"))
        item = self.table_fct_comp_2.horizontalHeaderItem(2)
        item.setText(_translate("fct_comp_2", "noZone"))

