import sys
from PyQt5 import uic, QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QFileDialog, QMessageBox
from PyQt5.QtGui import QIcon 
# from tkinter import filedialog
from datetime import datetime

qtCreatorFile = "pp2_gui.ui" 

#Listas para guardar los valores tokenizados
articulos=[]
preposiciones=[]
pronombres=[]
verbos=[]
numeros=[]
sinClasificar=[]
cadena=""

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class Tokenization(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        
        self.btnAbrirArchivo.clicked.connect(self.leerArchivoTxt)
        self.btnLimpiarTexto.clicked.connect(self.limpiarCampoTexto)
        self.btnTokenizar.clicked.connect(self.tokenizar)
        self.btnGenerarHTML.clicked.connect(self.confirmarGenerarHTML)

    #-----------------------------------------------------------------------------------------------------------#
    def leerArchivoTxt(self):
        global cadena
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        rutaArchivo, _ = QFileDialog.getOpenFileName(self,"Abrir archivo de texto", "","Text files (*.txt);;All Files (*)", options=options)
        txt_file = open(rutaArchivo,"r")
        cadena = txt_file.read()
        txt_file.close()
        self.limpiarCampoTexto()
        self.reiniciarValores()
        self.textEdit.setText(cadena)

    #-----------------------------------------------------------------------------------------------------------#
    def limpiarCampoTexto(self):
        cadena = ""
        self.textEdit.setText(cadena)

    #-----------------------------------------------------------------------------------------------------------#
    def reiniciarValores(self):
        articulos=[]
        preposiciones=[]
        pronombres=[]
        verbos=[]
        numeros=[]
        sinClasificar=[]
        cadena=""
    #-----------------------------------------------------------------------------------------------------------#
    def obtenerFechaActual(self):
        now = datetime.now()
        fechaFormato=str(now.day)+"-"+str(now.month)+"-"+str(now.year)+"-"+str(now.hour)+"-"+str(now.minute)+"-"+str(now.second)

        return fechaFormato

    #-----------------------------------------------------------------------------------------------------------#
    def generarHTML(self):
        global cadena
        nombreArchivo ="Análisis-"+self.obtenerFechaActual()+".html"

        textoHTML = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
          <title>Clasificacion de Elementos</title>
          <meta charset="utf-8">
          <meta name="viewport" content="width=device-width, initial-scale=1">
          <style>
            *{
              box-sizing: border-box;
            }

            body {
              font-family: Arial, Helvetica, sans-serif;
            }

            table {
              border-collapse: collapse;
              width: 100%;
            }

            td, th {
              border: 1px solid #000;
              text-align: center;
              padding: 8px;
            }

            th {
              background-color: #0288d1;
              color: #fff;
            }

            header{
              background-color: #0288d1;
              padding: 5px;
              text-align: center;
              font-size: 15px;
              color: white;
              width: 100%;
            }

            article {
              background-color: #fff;
              padding-left: 10px
              width: 90%;
             
            }

          </style>
        </head>
        <body>
          <header>
            <h2>Tokenizacion de Cadenas</h2>
            <h4>Segundo Proyecto Programado</h4>
            <p>Estudiantes:</p>
            <p>Jose Altamirano Salazar</p>
            <p>Josue Brenes Alfaro</p>
          </header>
          <center>
          <section>
            <article>
              <h1>Contenido Analizado</h1>
              <p>
        """
        textoHTML = textoHTML + cadena
        textoHTML = textoHTML + """ 
            </p>
            <hr>
            <h1>Analisis del documento</h1>
            <table>
              <tr>
                <th>Articulos</th>
                <th>Preposiciones</th>
                <th>Pronombres</th>
                <th>Verbos</th>
                <th>Numeros</th>
                <th>Sin Clasificar</th>
              </tr>
            """
        indice=0
        finArticulos=False
        finPreposiciones=False
        finPronombres=False
        finVerbos=False
        finNumeros=False
        finSinClasificar=False

        while(True):
          textoHTML=textoHTML+"<tr>"
          
          if(indice<len(articulos)):
            textoHTML=textoHTML+"<td><p>"+str(articulos[indice])+"</p></td>"
          else:
            textoHTML=textoHTML+"<td></td>"
            finArticulos=True

          if(indice<len(preposiciones)):
            textoHTML=textoHTML+"<td><p>"+str(preposiciones[indice])+"</p></td>"
          else:
            textoHTML=textoHTML+"<td></td>"
            finPreposiciones=True

          if(indice<len(pronombres)):
            textoHTML=textoHTML+"<td><p>"+str(pronombres[indice])+"</p></td>"
          else:
            textoHTML=textoHTML+"<td></td>"
            finPronombres=True

          if(indice<len(verbos)):
            textoHTML=textoHTML+"<td><p>"+str(verbos[indice])+"</p></td>"
          else:
            textoHTML=textoHTML+"<td></td>"
            finVerbos=True

          if(indice<len(numeros)):
            textoHTML=textoHTML+"<td><p>"+str(numeros[indice])+"</p></td>"
          else:
            textoHTML=textoHTML+"<td></td>"
            finNumeros=True

          if(indice<len(sinClasificar)):
            textoHTML=textoHTML+"<td><p>"+str(sinClasificar[indice])+"</p></td>"
          else:
            textoHTML=textoHTML+"<td></td>"
            finSinClasificar=True

          textoHTML=textoHTML+"</tr>"
          indice+=1

          if (finArticulos==True and finPreposiciones==True and finPronombres==True and finVerbos==True and finNumeros==True and finSinClasificar==True):
            break

          finArticulos=False
          finPreposiciones=False
          finPronombres=False
          finVerbos=False
          finNumeros=False
          finSinClasificar=False

        textoHTML = textoHTML + """ 
            </table>

            <h1>Analisis del documento</h1>
            <table>
              <tr>
                <th>Articulos</th>
                <th>Preposiciones</th>
                <th>Pronombres</th>
                <th>Verbos</th>
              </tr>
            """

        indice=0
        finArticulos=False
        finPreposiciones=False
        finPronombres=False
        finVerbos=False

        while(True):
          textoHTML=textoHTML+"<tr>"
          
          if(indice<len(articulos)):
            textoHTML=textoHTML+"<td><p>"+str(articulos[indice])+"</p></td>"
          else:
            textoHTML=textoHTML+"<td></td>"
            finArticulos=True

          if(indice<len(preposiciones)):
            textoHTML=textoHTML+"<td><p>"+str(preposiciones[indice])+"</p></td>"
          else:
            textoHTML=textoHTML+"<td></td>"
            finPreposiciones=True

          if(indice<len(pronombres)):
            textoHTML=textoHTML+"<td><p>"+str(pronombres[indice])+"</p></td>"
          else:
            textoHTML=textoHTML+"<td></td>"
            finPronombres=True

          if(indice<len(verbos)):
            textoHTML=textoHTML+"<td><p>"+str(verbos[indice])+"</p></td>"
          else:
            textoHTML=textoHTML+"<td></td>"
            finVerbos=True

          textoHTML=textoHTML+"</tr>"
          indice+=1

          if (finArticulos==True and finPreposiciones==True and finPronombres==True and finVerbos==True):
            break

          finArticulos=False
          finPreposiciones=False
          finPronombres=False
          finVerbos=False

        textoHTML = textoHTML +  """        
          </table>

          </article>
          </section>
          </center>
          </body>
          </html>
          """

        try:
            Html_file = open(nombreArchivo,"x")
            Html_file.write(textoHTML)
            Html_file.close()
            return 1
        except:
            return -1

    #-----------------------------------------------------------------------------------------------------------#
    def confirmarGenerarHTML(self):
        eleccion = QtWidgets.QMessageBox.question(self, 'Generar HTML',
                                            "¿Esta seguro de generar el archivo HTML? \nEste proceso eliminará el texto ingresado",
                                            QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        
        if (eleccion == QtWidgets.QMessageBox.Yes):
            
            if(self.generarHTML()!=-1):

              informacion = QtWidgets.QMessageBox.information(self, 'Generar HTML',
                                            "Archivo HTML creado exitosamente.")
              self.limpiarCampoTexto()
              self.reiniciarValores()
        else:
            advertencia = QtWidgets.QMessageBox.critical(self, 'Generar HTML',
                                            "Ha ocurrido un error.\nEl archivo HTML NO se ha generado.")
    #-----------------------------------------------------------------------------------------------------------#
    def tokenizar(self):
        global cadena
        self.tokenizarCadena()

        listasConcatenadas = str(self.ordenarLista(articulos))+"\n"+str(self.ordenarLista(preposiciones))+"\n"+str(self.ordenarLista(pronombres))+"\n"+str(self.ordenarLista(verbos))+"\n"+str(self.ordenarLista(numeros))+"\n"+str(self.ordenarLista(sinClasificar))

        self.textEdit.setText(listasConcatenadas)
    #-----------------------------------------------------------------------------------------------------------#
    def eliminarSimbolos(self):
        global cadena
        abcValido = "abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ1234567890. áéíúóüÁÉÍÓÚÜ"
        cadenaResultante = ""
        for caracter in cadena:
            if(abcValido.find(caracter)!=-1):
                cadenaResultante = cadenaResultante + caracter
        return cadenaResultante

    #-----------------------------------------------------------------------------------------------------------#
    def buscarElemento(self, lista, palabra):
        indice = 0

        while (indice != len(lista)):
            if (lista[indice] == palabra):
                return indice
            indice += 1

        return -1
    #-----------------------------------------------------------------------------------------------------------#
    def esNumero(self, n):
        try:
            resultado = float(n)
            return True
        except:
            return False
    #-----------------------------------------------------------------------------------------------------------#
    def esVerbo(self, palabra):
        if (palabra[-2:]=="ar" or palabra[-2:]=="er" or palabra[-2:]=="ir"):
            return 1
        elif (palabra[-4:]=="ando" or palabra[-4:]=="endo"):
            return 2
        elif (palabra[-3:]=="ado" or palabra[-3:]=="ido" or palabra[-2:]=="to" or palabra[-3:]=="cho" or palabra[-2:]=="so"):
            return 3
        else:
            return -1
    #-----------------------------------------------------------------------------------------------------------#
    def ordenarLista(self, lista):
        
        for indice in range(len(lista)):
            for elemento in range(len(lista)-1):
                if (lista[elemento]>lista[elemento+1]):
                    lista[elemento],lista[elemento+1] = lista[elemento+1],lista[elemento]

        return lista

    #-----------------------------------------------------------------------------------------------------------#
    def tokenizarCadena(self):
        global cadena
        #Listas para almacenar valores posibles para los elementos
        listaArticulos=["el", "la", "los", "las", "un", "una", "unos", "unas", "lo", "al", "del"]
        listaPreposiciones=["a", "ante", "bajo", "cabe", "con", "contra", "de", "desde", "durante", "en", "entre", "hacia", "hasta", "mediante", "para", "por", "según", "sin", "so", "sobre", "tras", "versus", "vía"]
        listaPronombres=["yo", "me", "mí", "conmigo", "nosotros", "nosotras", "nos", "tú", "te", "ti", "contigo", "vosotros", "vosotras", "vos", "él", "ella", "se", "consigo", "le", "les","mío", "mía", "míos", "mías", "nuestro", "nuestra", "nuestros", "nuestras", "tuyo", "tuya", "tuyos", "vuestro", "vuestra", "vuestros", "vuestras", "suyo", "suya", "suyos", "suyas"]

        #Lista con las palabras de la cadena separadas, y sin símbolos
        listaTokenizada = self.eliminarSimbolos().lower().split()

        #Recorrer los elemntos de la lista tokenizada y agregarlos a la
        #lista que corresponda cada uno.
        for elemento in listaTokenizada:
            if(self.buscarElemento(listaArticulos, elemento)!=-1):
                articulos.append(elemento)

            elif(self.buscarElemento(listaPreposiciones, elemento)!=-1):
                preposiciones.append(elemento)

            elif(self.buscarElemento(listaPronombres, elemento)!=-1):
                pronombres.append(elemento)

            elif(self.esNumero(elemento)):
                numeros.append(elemento)

            elif(self.esVerbo(elemento)!=-1):
                verbos.append(elemento)

            else:
                sinClasificar.append(elemento)

if __name__ == "__main__":
    app =  QtWidgets.QApplication(sys.argv)
    window = Tokenization()
    window.setWindowIcon(QtGui.QIcon("icon.png"))
    window.setWindowTitle("Tokenizacion de Texto")
    window.show()
    sys.exit(app.exec_())
