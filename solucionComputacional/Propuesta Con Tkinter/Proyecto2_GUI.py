import tkinter as tk
import tkinter.messagebox
from tkinter.filedialog import askopenfilename
from datetime import datetime

#Listas para guardar los valores tokenizados
articulos=[]
preposiciones=[]
pronombres=[]
verbos=[]
numeros=[]
sinClasificar=[]
cadenaTexto=""

#-----------------------------------------------------------------------------------------------------------#
def obtenerFechaActual():
    now = datetime.now()
    fechaFormato=str(now.day)+"-"+str(now.month)+"-"+str(now.year)+"-"+str(now.hour)+"-"+str(now.minute)+"-"+str(now.second)

    return fechaFormato
#-----------------------------------------------------------------------------------------------------------#
def generarHTML():
    cadena = cadenaTexto

    nombreArchivo ="Análisis-"+obtenerFechaActual()+".html"

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
def leerArchivoTxt(rutaArchivo):
    txt_file = open(rutaArchivo,"r")
    cadena = txt_file.read()
    txt_file.close()
    return cadena

#-----------------------------------------------------------------------------------------------------------#
def eliminarSimbolos(cadena):
    abcValido = "abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ1234567890áéíúóüÁÉÍÓÚÜ. "
    cadenaResultante = ""
    for caracter in cadena:
        if(abcValido.find(caracter)!=-1):
            cadenaResultante = cadenaResultante + caracter

    return cadenaResultante

#-----------------------------------------------------------------------------------------------------------#
def buscarElemento(lista, palabra):
    indice = 0

    while (indice != len(lista)):
        if (lista[indice] == palabra):
            return indice
        indice += 1

    return -1

#-----------------------------------------------------------------------------------------------------------#
def esNumero(n):
    try:
        resultado = float(n)
        return True
    except:
        return False

#-----------------------------------------------------------------------------------------------------------#
def esVerbo(palabra):
    if (palabra[-2:]=="ar" or palabra[-2:]=="er" or palabra[-2:]=="ir"):
        return 1
    elif (palabra[-4:]=="ando" or palabra[-4:]=="endo"):
        return 2
    elif (palabra[-3:]=="ado" or palabra[-3:]=="ido" or palabra[-2:]=="to" or palabra[-3:]=="cho" or palabra[-2:]=="so"):
        return 3
    else:
        return -1

#-----------------------------------------------------------------------------------------------------------#
def ordenarLista(lista):
    
    for k in range(len(lista)):
        for m in range(len(lista)-1):
            if lista[m]>lista[m+1]:
                lista[m],lista[m+1] = lista[m+1],lista[m]

    return lista

#-----------------------------------------------------------------------------------------------------------#
#**************************************************Falta Revisar********************************************#
def eliminarDuplicados(lista):
    nuevaLista = []
    indice=0

    while(indice1 < len(lista)):
      if(lista[indice1] not in nuevaLista):
        nuevaLista=nuevaLista+[lista[indice1]]

      indice+=1

      #lista = list(set())

    return nuevaLista

#-----------------------------------------------------------------------------------------------------------#
def tokenizarCadena():
    #Listas para de valores posibles para los elementos
    listaArticulos=["el", "la", "los", "las", "un", "una", "unos", "unas", "lo", "al", "del"]
    listaPreposiciones=["a", "ante", "bajo", "cabe", "con", "contra", "de", "desde", "durante", "en", "entre", "hacia", "hasta", "mediante", "para", "por", "según", "sin", "so", "sobre", "tras", "versus", "vía"]
    listaPronombres=["yo", "me", "mí", "conmigo", "nosotros", "nosotras", "nos", "tú", "te", "ti", "contigo", "vosotros", "vosotras", "vos", "él", "ella", "se", "consigo", "le", "les","mío", "mía", "míos", "mías", "nuestro", "nuestra", "nuestros", "nuestras", "tuyo", "tuya", "tuyos", "vuestro", "vuestra", "vuestros", "vuestras", "suyo", "suya", "suyos", "suyas"]

    cadenaTexto = txtDocumento.get(1.0, tk.END)

    try:
        #Lista con las palabras de la cadena separadas, y sin símbolos
        listaTokenizada = eliminarSimbolos(cadenaTexto).lower().split()

        #Recorrer los elemntos de la lista tokenizada y agregarlos a la
        #lista que corresponda cada uno.
        for elemento in listaTokenizada:
            if(buscarElemento(listaArticulos, elemento)!=-1):
                articulos.append(elemento)

            elif(buscarElemento(listaPreposiciones, elemento)!=-1):
                preposiciones.append(elemento)

            elif(buscarElemento(listaPronombres, elemento)!=-1):
                pronombres.append(elemento)

            elif(esNumero(elemento)):
                numeros.append(elemento)

            elif(esVerbo(elemento)!=-1):
                verbos.append(elemento)

            else:
                sinClasificar.append(elemento)

        # articulos = eliminarDuplicados(articulos)
        # preposiciones = eliminarDuplicados(preposiciones)
        # pronombres = eliminarDuplicados(pronombres)
        # verbos = eliminarDuplicados(verbos)
        # sinClasificar = eliminarDuplicados(sinClasificar)
        
        return 1

    except:
        
        return -1
    

#-----------------------------------------------------------------------------------------------------------#
def reiniciarValores():
    articulos=[]
    preposiciones=[]
    pronombres=[]
    verbos=[]
    numeros=[]
    sinClasificar=[]
    cadenaTexto=""
    txtDocumento.delete(1.0, tk.END)
    txtTokens.delete(1.0, tk.END)

#-----------------------------------------------------------------------------------------------------------#
def confirmarGenerarHTML():
    result=tk.messagebox.askquestion('Crear HTML','¿Esta seguro de generar el archivo HTML? \nEste proceso eliminará el texto ingresado')

    if result=='yes':

        if(generarHTML()!=-1):
            tkinter.messagebox.showinfo("Generar HTML","Archivo HTML creado exitosamente.")
            reiniciarValores()           
        else:
            tkinter.messagebox.showerror("Generar HTML","Ha ocurrido un error.\nEl archivo HTML NO se ha generado.")

#-----------------------------------------------------------------------------------------------------------# 
def confirmarTokenizar():
    result=tk.messagebox.askquestion("Tokenizar Documento","¿Esta seguro de tokenizar el texto ingresado?")

    if result=='yes':

        if(tokenizarCadena()!=-1):
            txtTokens.delete(1.0, tk.END)
            listasConcatenadas = "-->Articulos:\n"+str(ordenarLista(articulos))+"\n-->Preposiciones:\n"+str(ordenarLista(preposiciones))+"\n-->Pronombres:\n"+str(ordenarLista(pronombres))+"\n-->Verbos:\n"+str(ordenarLista(verbos))+"\n-->Numero:\n"+str(ordenarLista(numeros))+"\n-->Sin Clasificar:\n"+str(ordenarLista(sinClasificar))
            txtTokens.insert(tk.END, listasConcatenadas)
        else:
            tkinter.messagebox.showerror("Tokenizar Documento","Ha ocurrido un error.\nEl texto nose ha tokenizado.")

#-----------------------------------------------------------------------------------------------------------#
def leerArchivo():
    """Open a file for editing."""
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return

    txtDocumento.delete(1.0, tk.END)
    with open(filepath, "r") as input_file:
        text = input_file.read()
        txtDocumento.insert(tk.END, text)

#-----------------------------------------------------------------------------------------------------------#
# def ventanaPrincipal():

tokenizacion = tk.Tk()
tokenizacion.title("Tokenizacion de Caracteres")
tokenizacion.geometry("950x550")
tokenizacion.config(bg="gray99")
tokenizacion.resizable(False,False)

frCompleto = tk.Frame(tokenizacion, bg="gray99")
frBtnArchivo = tk.Frame(frCompleto, padx=5, pady=5, bg="gray99")

label1 = tk.Label(frCompleto, text="Documento: ", bg="gray99", fg="#006BE5", font=("Calibri", 12))
label2 = tk.Label(frCompleto, text="Estructura de Listas: ", bg="gray99", fg="#006BE5", font=("Calibri", 12))

txtTokens = tk.Text(frCompleto, width="30",font=("Calibri", 11), relief=tk.SUNKEN )  
txtDocumento = tk.Text(frCompleto, width="80", font=("Calibri", 11) )

btnAbrir = tk.Button(frBtnArchivo, text="Abrir Archivo", command=leerArchivo, bg="#0288d1", fg="#ffffff", relief=tk.GROOVE, font=("Calibri", 12) )
btnLimpiar = tk.Button(frBtnArchivo, text="Limpiar", command=reiniciarValores, bg="#0288d1", fg="#ffffff", relief=tk.GROOVE, font=("Calibri", 12)  )
btnAbrir.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btnLimpiar.grid(row=0, column=1, sticky="ew", padx=5)

btnTokenizar = tk.Button(frCompleto, text="Tokenizar", command=confirmarTokenizar, bg="#0288d1", fg="#ffffff", relief=tk.GROOVE, font=("Calibri", 12)  )
btnHtml = tk.Button(frCompleto, text="Generar HTML", command=confirmarGenerarHTML, bg="#0288d1", fg="#ffffff", relief=tk.GROOVE, font=("Calibri", 12)  )

label1.grid(row=0,column=0, sticky="w", padx=5)
txtDocumento.grid(row=1, column=0, sticky="w", padx=10)
frBtnArchivo.grid(row=2, column=0, sticky="se", padx=5, pady=10)
label2.grid(row=0, column=1, sticky="w", padx=5)
txtTokens.grid(row=1, column=1, sticky="e", padx=5)
btnTokenizar.grid(row=2, column=1, sticky="e", padx=5, pady=10)
btnHtml.grid(row=1, column=2, sticky="n", padx=5)

frCompleto.grid(row=0, column=0, padx=15, pady=15)

tokenizacion.mainloop()

#ventanaPrincipal()