import sys
from PyQt5 import uic, QtWidgets
from tkinter import filedialog
from tkinter import *

qtCreatorFile = "pp2_gui.ui" 

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class Tokenization(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        
        self.btnAbrirArchivo.clicked.connect(self.leerArchivoTxt)
        self.btnLimpiarTexto.clicked.connect(self.limpiarCampoTexto)
        self.btnTokenizar.clicked.connect(self.leerArchivoTxt)

    def leerArchivoTxt(self):
        rutaArchivo= filedialog.askopenfilename(initialdir = "/",
                                      title = "Select file",
                                      filetypes = (("Text files", 
                                                    "*.txt*"), 
                                                   ("all files", 
                                                    "*.*"))) 
        txt_file = open(rutaArchivo,"r")
        cadena = txt_file.read()
        txt_file.close()
        self.textEdit.setText(cadena)

    def limpiarCampoTexto(self):
        cadena = ""
        self.textEdit.setText(cadena)

if __name__ == "__main__":
    app =  QtWidgets.QApplication(sys.argv)
    window = Tokenization()
    window.show()
    sys.exit(app.exec_())
