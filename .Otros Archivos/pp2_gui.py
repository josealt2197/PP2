# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pp2_gui.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!
import sys
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(728, 557)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(20, 60, 461, 401))
        self.textEdit.setObjectName("textEdit")
        self.treeView = QtWidgets.QTreeView(self.centralwidget)
        self.treeView.setGeometry(QtCore.QRect(500, 60, 201, 401))
        self.treeView.setObjectName("treeView")
        self.btnLimpiarTexto = QtWidgets.QPushButton(self.centralwidget)
        self.btnLimpiarTexto.setGeometry(QtCore.QRect(300, 470, 86, 27))
        self.btnLimpiarTexto.setObjectName("btnLimpiarTexto")
        self.btnAbrirArchivo = QtWidgets.QPushButton(self.centralwidget)
        self.btnAbrirArchivo.setGeometry(QtCore.QRect(120, 20, 101, 31))
        self.btnAbrirArchivo.setObjectName("btnAbrirArchivo")
        self.btnAbrirArchivo_2 = QtWidgets.QPushButton(self.centralwidget)
        self.btnAbrirArchivo_2.setGeometry(QtCore.QRect(390, 470, 86, 27))
        self.btnAbrirArchivo_2.setObjectName("btnAbrirArchivo_2")
        self.btnGenerarHTML = QtWidgets.QPushButton(self.centralwidget)
        self.btnGenerarHTML.setGeometry(QtCore.QRect(595, 470, 101, 31))
        self.btnGenerarHTML.setObjectName("btnGenerarHTML")
        self.lblTituloCampotexto = QtWidgets.QLabel(self.centralwidget)
        self.lblTituloCampotexto.setGeometry(QtCore.QRect(30, 30, 81, 16))
        self.lblTituloCampotexto.setObjectName("lblTituloCampotexto")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(500, 30, 111, 16))
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 728, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btnLimpiarTexto.setText(_translate("MainWindow", "Limpiar"))
        self.btnAbrirArchivo.setText(_translate("MainWindow", "Abrir Archivo"))
        self.btnAbrirArchivo_2.setText(_translate("MainWindow", "Tokenizar"))
        self.btnGenerarHTML.setText(_translate("MainWindow", "Generar HTML"))
        self.lblTituloCampotexto.setText(_translate("MainWindow", "Documento:"))
        self.label_2.setText(_translate("MainWindow", "Estructura de Listas"))

