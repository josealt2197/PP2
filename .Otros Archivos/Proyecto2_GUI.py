import tkinter as tk
import tkinter.messagebox
from tkinter import ttk
from tkinter.filedialog import askopenfilename
from datetime import datetime
from translate import Translator

#Listas para guardar los valores tokenizados (En Español)
articulos=[]
preposiciones=[]
pronombres=[]
verbos=[]
numeros=[]
sinClasificar=[]

#Listas para guardar los valores tokenizados (En Inglés)
articles=[]
prepositions=[]
pronouns=[]
verbs=[]

#Cadena para almacenar texto ingresado en la ventana principal
cadenaTexto=""

#Caracteres y signos de puntuación permitidos
abcValido = "abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ1234567890áéíúóüÁÉÍÓÚÜ.,;: "

#-----------------------------------------------------------------------------------------------------------#
'''
Entradas: Una lista con todos sus elementos en español
Salidas: Otra lista con los valores de la lista recibida traducidos de español a ingles
Restricciones:No valida restricciones
'''
def traducirLista(listaEspanol):
    listaIngles=[]

    tradutor = Translator(from_lang="Spanish",to_lang="English")

    for elemento in listaEspanol:
      listaIngles.append(tradutor.translate(elemento))

    return listaIngles

#-----------------------------------------------------------------------------------------------------------#
'''
Entradas:Una palabra en español
Salidas:La palabra de entrada, traducida a ingles
Restricciones:No valida restricciones
'''
def traducirPalabra(palabra):
    tradutor = Translator(from_lang="Spanish",to_lang="English")
    traduccion = tradutor.translate(palabra)
    
    return traduccion

#-----------------------------------------------------------------------------------------------------------#
'''
Entradas:Ninguna
Salidas:Los datos de la fecha y hora actual en el formato dd-mm-aa-hh-mm-ss
Restricciones:Ninguna
'''
def obtenerFechaActual():
    now = datetime.now()
    fechaFormato=str(now.day)+"-"+str(now.month)+"-"+str(now.year)+"-"+str(now.hour)+"-"+str(now.minute)+"-"+str(now.second)

    return fechaFormato
    
#-----------------------------------------------------------------------------------------------------------#
'''
Entradas:Una cadena de texto 
Salidas:Un archivo HTML fon un formato establecido por la funcion 
Restricciones:No valida restricciones
'''
def generarHTML():
    cadena = cadenaTexto
    filasHTML = ""

    articles = eliminarDuplicados(traducirLista(articulos))
    prepositions = eliminarDuplicados(traducirLista(preposiciones))
    pronouns = eliminarDuplicados(traducirLista(pronombres))
    verbs = eliminarDuplicados(traducirLista(verbos))

    nombreArchivo ="Análisis-"+obtenerFechaActual()+".html"

    textoHTML = """
    <!DOCTYPE html>
    <head>
      <title>Clasificación de Elementos</title>
      <meta charset="utf-8">
      <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
      <style>
        *{
          box-sizing: border-box;
        }

        body {
          font-family: Arial, Helvetica, sans-serif;
          background-color: #fff;
          width: 100%;
        }

        table{
          width: 80%;
        }

        table, th, td {
          border: 1px solid black;
          border-collapse: collapse; 
        }

        th, td {
          text-align: center;
          padding: 15px;
        }

        th {
          background-color: #0288d1;
          color: #fff;
        }

        tr:nth-child(even){
          background-color: #b3e5fc;
        }

      </style>
    </head>
    <body>
      <center>
          <h1>Contenido Analizado</h1>
          <p>
    """
    textoHTML = textoHTML + cadena
    textoHTML = textoHTML + """ 
        </p>
        <hr>
        <h1>Analisis del documento (traduccion)</h1>
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
      filasHTML=filasHTML+"<tr>"
      
      if(indice<len(articulos)):
        filasHTML=filasHTML+"<td><p>"+str(articulos[indice])+"</p></td>"
      else:
        filasHTML=filasHTML+"<td></td>"
        finArticulos=True

      if(indice<len(preposiciones)):
        filasHTML=filasHTML+"<td><p>"+str(preposiciones[indice])+"</p></td>"
      else:
        filasHTML=filasHTML+"<td></td>"
        finPreposiciones=True

      if(indice<len(pronombres)):
        filasHTML=filasHTML+"<td><p>"+str(pronombres[indice])+"</p></td>"
      else:
        filasHTML=filasHTML+"<td></td>"
        finPronombres=True

      if(indice<len(verbos)):
        filasHTML=filasHTML+"<td><p>"+str(verbos[indice])+"</p></td>"
      else:
        filasHTML=filasHTML+"<td></td>"
        finVerbos=True

      if(indice<len(numeros)):
        filasHTML=filasHTML+"<td><p>"+str(numeros[indice])+"</p></td>"
      else:
        filasHTML=filasHTML+"<td></td>"
        finNumeros=True

      if(indice<len(sinClasificar)):
        filasHTML=filasHTML+"<td><p>"+str(sinClasificar[indice])+"</p></td>"
      else:
        filasHTML=filasHTML+"<td></td>"
        finSinClasificar=True

      filasHTML=filasHTML+"</tr>"
      indice+=1

      if (finArticulos==True and finPreposiciones==True and finPronombres==True and finVerbos==True and finNumeros==True and finSinClasificar==True):
        break

      finArticulos=False
      finPreposiciones=False
      finPronombres=False
      finVerbos=False
      finNumeros=False
      finSinClasificar=False

    textoHTML = textoHTML + filasHTML[:-63] + """ 
        </table>

        <h1>Analisis del documento</h1>
        <table>
          <tr>
            <th>Articles</th>
            <th>Prepositions</th>
            <th>Pronouns</th>
            <th>Verbs</th>
          </tr>
        """
    filasHTML=""
    indice=0
    finArticulos=False
    finPreposiciones=False
    finPronombres=False
    finVerbos=False

# Primera Ejecucion (Para listas con = tamaño)
#     funcionRecursiva --> recursos[1] --> recursos(0,0)=recursos[articulos[0]]
#     funcionRecursiva --> recursos[2] --> recursos(1,0)=recursos[preposiciones[0]]
#     funcionRecursiva --> recursos[3] --> recursos(2,0)=recursos[pronombres[0]]
#     funcionRecursiva --> recursos[4] --> recursos(3,0)=recursos[verbos[0]]
#     funcionRecursiva --> recursos[5] --> recursos(4,0)=recursos[numeros[0]]
#     funcionRecursiva --> recursos[6] --> recursos(5,0)=recursos[sinClasificar[0]]

# Segunda Ejecucion
#     funcionRecursiva --> recursos[1] --> recursos(0,1)=recursos[articulos[1]]
#     funcionRecursiva --> recursos[2] --> recursos(1,1)=recursos[preposiciones[1]]
#     funcionRecursiva --> recursos[3] --> recursos(2,1)=recursos[pronombres[1]]
#     funcionRecursiva --> recursos[4] --> recursos(3,1)=recursos[verbos[1]]
#     funcionRecursiva --> recursos[5] --> recursos(4,1)=recursos[numeros[1]]
#     funcionRecursiva --> recursos[6] --> recursos(6,1)=recursos[sinClasificar[1]]


# generafilas(filas="", x=0, y=0):
#   global recursos
#   filas=filas+"<tr>"

#   return generafilas(filas="")


    while(True):
      filasHTML=filasHTML+"<tr>"
      
      if(indice<len(articles)):
        filasHTML=filasHTML+"<td><p>"+str(articles[indice])+"</p></td>"
      else:
        filasHTML=filasHTML+"<td></td>"
        finArticulos=True

      if(indice<len(prepositions)):
        filasHTML=filasHTML+"<td><p>"+str(prepositions[indice])+"</p></td>"
      else:
        filasHTML=filasHTML+"<td></td>"
        finPreposiciones=True

      if(indice<len(pronouns)):
        filasHTML=filasHTML+"<td><p>"+str(pronouns[indice])+"</p></td>"
      else:
        filasHTML=filasHTML+"<td></td>"
        finPronombres=True

      if(indice<len(verbs)):
        filasHTML=filasHTML+"<td><p>"+str(verbs[indice])+"</p></td>"
      else:
        filasHTML=filasHTML+"<td></td>"
        finVerbos=True

      filasHTML=filasHTML+"</tr>"
      indice+=1

      if (finArticulos==True and finPreposiciones==True and finPronombres==True and finVerbos==True):
        break

      finArticulos=False
      finPreposiciones=False
      finPronombres=False
      finVerbos=False

    textoHTML = textoHTML + filasHTML[:-63] +  """        
      </table>
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
'''
Entradas:Una cadena de caracteres 
Salidas:La misma cadena eliminandole los simbolos que no aparescan en la variable local abcValido
Restricciones:No valida restricciones
'''
def eliminarSimbolos(cadena=cadenaTexto,cadenaResultante=""):
    
    if(cadena==""):
      return cadenaResultante
    else:
        if(abcValido.find(cadena[0])!=-1):
            return eliminarSimbolosRecursivo(cadena[1:], cadenaResultante+cadena[0])
        else:
            return eliminarSimbolosRecursivo(cadena[1:], cadenaResultante)
    return cadenaResultante

#-----------------------------------------------------------------------------------------------------------#
'''
Entradas: Una lista con varios elementos y una cadena de caracteres (palabra)
Salidas: En caso de que se encuentre la palabra buscada dentro de la lista se retorna el valor numerico de la 
         posicion en la que esta se encuentra, caso contrario la funcion retorna el valor numerico -1
Restricciones: Los valores de la lista deben corresponder con tipo del valor ingresado para la palabra del 
               segundo parámetro.
'''
# def buscarElemento(lista, palabra, posicion=(-1), contador=0):
#     if(posicion!=-1):
#       return posicion
#     elif(contador>=len(lista)):
#       return -1   
#     else:
#         if(lista[contador]==palabra):
#             return buscarElementoRecusivo(lista, palabra, posicion=contador, contador=contador+1)
#         else:
#             return buscarElementoRecusivo(lista, palabra, posicion, contador=contador+1)

def buscarElemento(lista, palabra):
    indice = 0

    while (indice != len(lista)):
        if (lista[indice] == palabra):
            return indice
        indice += 1

    return -1

#-----------------------------------------------------------------------------------------------------------#
'''
Entradas:Un caracter 
Salidas:True si el caracter es un numero o False si el caracter no es un numero
Restricciones:No valida restricciones
'''
def esNumero(n):
    try:
        resultado = float(n)
        return True
    except:
        return False

#-----------------------------------------------------------------------------------------------------------#
'''
Entradas: Una cadena de caracteres
Salidas: 1, 2 o 3 en caso de que la cadena ingresada pueda clasificarse como un verbo infinitivo, gerundio
         o participio
Restricciones: Ninguna
'''
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
'''
Entradas:Una lista.
Salidas:Una lista acomodada de forma acendente.
Restricciones:No valida restricciones
'''
def ordenarLista(lista):
    
    for indice in range(len(lista)):
        for elemento in range(len(lista)-1):
            if (lista[elemento]>lista[elemento+1]):
                lista[elemento],lista[elemento+1] = lista[elemento+1],lista[elemento]

    return lista

#-----------------------------------------------------------------------------------------------------------#
'''
Entradas: Una lista con elementos de un mismo tipo
Salidas:La lista ingresada como parametro, omitiendo los valores que estuvieran repetidos dentro de esta.
Restricciones:Ninguna
'''
def eliminarDuplicados(lista,nuevaLista=[]):
    if (lista==[]):
        return nuevaLista
    else:
        if (buscarElemento(nuevaLista,lista[0])==-1):
            return eliminarDuplicados(lista[1:],nuevaLista+[lista[0]])
        else:
            return eliminarDuplicados(lista[1:],nuevaLista)

#-----------------------------------------------------------------------------------------------------------#
# '''
# Entradas: Una lista con elementos de un mismo tipo
# Salidas:La lista ingresada como parametro, omitiendo los valores que estuvieran repetidos dentro de esta.
# Restricciones:Ninguna
# '''
# def clasificarElemento(listaClasificacion):
    

#-----------------------------------------------------------------------------------------------------------#
'''
Entradas:Los valores ingresados en el cuadro de texto 
Salidas:Se rellenan los valores de las listas globales con los elementos ingresados dentro del cuadro de texto según su tipo. 
Restricciones:No valida restricciones
'''
def tokenizarCadena():
    global cadenaTexto

    #Listas para de valores posibles para los elementos
    listaArticulos=["el", "la", "los", "las", "un", "una", "unos", "unas", "lo", "al", "del"]
    listaPreposiciones=["a", "ante", "bajo", "cabe", "con", "contra", "de", "desde", "durante", "en", "entre", "hacia", "hasta", "mediante", "para", "por", "según", "sin", "so", "sobre", "tras", "versus", "vía"]
    listaPronombres=["yo", "me", "mí", "conmigo", "nosotros", "nosotras", "nos", "tú", "te", "ti", "contigo", "vosotros", "vosotras", "vos", "él", "ella", "se", "consigo", "le", "les","mío", "mía", "míos", "mías", "nuestro", "nuestra", "nuestros", "nuestras", "tuyo", "tuya", "tuyos", "vuestro", "vuestra", "vuestros", "vuestras", "suyo", "suya", "suyos", "suyas"]

    cadenaTexto = txtDocumento.get(1.0, tk.END)

    try:
        #Lista con las palabras de la cadena separadas, y sin símbolos
        eliminarSimbolos()
        cadenaSinSimbolos = cadenaTexto.lower().replace('\n', ' ')
        listaTokenizada = cadenaSinSimbolos.split(" ")

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
'''
Entradas:Ninguna
Salidas:Los valores de las variables globales omitiendo los valores repetidos dentro de estas
Restricciones: Ninguna
'''
def mostrarListasTraducidas():
    articles = eliminarDuplicados(traducirLista(articulos))
    prepositions = eliminarDuplicados(traducirLista(preposiciones))
    pronouns = eliminarDuplicados(traducirLista(pronombres))
    verbs = eliminarDuplicados(traducirLista(verbos))

    listaTokens.delete(1.0, tk.END)
    listasConcatenadas = "-->Articles:\n"+str(ordenarLista(articles))+"\n\n-->Prepositions:\n"+str(ordenarLista(prepositions))+"\n\n-->Pronouns:\n"+str(ordenarLista(pronombres))+"\n\n-->Verbs:\n"+str(ordenarLista(verbos))
    listaTokens.insert(tk.END, listasConcatenadas)     

#-----------------------------------------------------------------------------------------------------------#
'''
Entradas:Ninguna
Salidas:Los valores de las variables globales son reasignados según su valor inicial
Restricciones: Ninguna
'''
def reiniciarValores():
    articulos=[]
    preposiciones=[]
    pronombres=[]
    verbos=[]
    numeros=[]
    sinClasificar=[]
    cadenaTexto=""
    listaTokens.delete(1.0, tk.END)

#-----------------------------------------------------------------------------------------------------------#
'''
Entradas:Ninguna
Salidas:Elimina el contenido del campo de texto de la venta principal
Restricciones: Ninguna
'''
def reiniciarDocumento():
    txtDocumento.delete(1.0, tk.END)


#-----------------------------------------------------------------------------------------------------------#
'''
Entradas: Se hace clic sobre el boton con la leyenda "Generar HTML"
Salidas: Una ventana en la que se confirma el proceso de generar el archivo HTML. En caso de que se el usuario
                 presione el botón Si/Yes se realiza una llamada a la funcion para generar el archivo HTML.
Restricciones:Validar que se hayatokenzado el texto previamente ingresado
'''
def confirmarGenerarHTML():
    resultado=tk.messagebox.askquestion('Crear HTML','¿Esta seguro de generar el archivo HTML? \nEste proceso eliminará el texto ingresado')

    if resultado=='yes':

        if(generarHTML()!=-1):
            tkinter.messagebox.showinfo("Generar HTML","Archivo HTML creado exitosamente.")
            reiniciarValores()           
        else:
            tkinter.messagebox.showerror("Generar HTML","Ha ocurrido un error.\nEl archivo HTML NO se ha generado.")

#-----------------------------------------------------------------------------------------------------------# 
'''
Entradas:Se hace clic sobre el boton con la leyena "Tokenizar".
Salidas:Una ventana en la cual pregunta si desea tokenizar lo ingresado en el cuadro de texto.
Restricciones:Verificar que en el cuadro de texto existan elementos. 
'''
def confirmarTokenizar():
    resultado=tk.messagebox.askquestion("Tokenizar Documento","¿Esta seguro de tokenizar el texto ingresado?")

    if resultado=='yes':

        if(tokenizarCadena()!=-1):

            listaTokens.delete(*listaTokens.get_children())
            listaTokens.insert('', '0', 'documento', text ='Documento')

            listarTokens(articulos, "1", "Articulos")
            listarTokens(preposiciones, "2", "Preposiciones")
            listarTokens(pronombres, "3", "Pronombres")
            listarTokens(verbos, "4", "Verbos")
            listarTokens(numeros, "5", "Numeros")
            listarTokens(sinClasificar, "6", "Sin Clasificar")

            #listaTokens.delete(1.0, tk.END)
            # listasConcatenadas = "-->Articulos:\n"+str(ordenarLista(articulos))+"\n\n-->Preposiciones:\n"+str(ordenarLista(preposiciones))+"\n\n-->Pronombres:\n"+str(ordenarLista(pronombres))+"\n\n-->Verbos:\n"+str(ordenarLista(verbos))+"\n\n-->Numeros:\n"+str(ordenarLista(numeros))+"\n\n-->Sin Clasificar:\n"+str(ordenarLista(sinClasificar))
            # listaTokens.insert(tk.END, listasConcatenadas)
        else:
            tkinter.messagebox.showerror("Tokenizar Documento","Ha ocurrido un error.\nEl texto no se ha tokenizado.")

#-----------------------------------------------------------------------------------------------------------# 
'''
Entradas:Se hace clic sobre el boton con la leyena "Tokenizar".
Salidas:Una ventana en la cual pregunta si desea tokenizar lo ingresado en el cuadro de texto.
Restricciones:Verificar que en el cuadro de texto existan elementos. 
'''
def listarTokens(lista, posicion, categoria):
    indice=0
    nombreElemento=""

    listaTokens.insert('documento', posicion , categoria, text = categoria)  

    while(indice!=len(lista)):
        nombreElemento = categoria + str(indice)
        listaTokens.insert(categoria, 'end', nombreElemento , text = str(lista[indice]))
        indice+=1



#-----------------------------------------------------------------------------------------------------------#
'''
Entradas:Una cadena de caracteres referente a la ruta de un archivo.
Salidas:Una cadena de caracteres que contiene el texto que se encontraba dentro del archivo.
Restricciones:La ruta seleccionda debe corresponder a una ruta valida para un archivo de texto.
'''
def leerArchivo():
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    txtDocumento.delete(1.0, tk.END)
    with open(filepath, "r") as archivoTexto:
        text = archivoTexto.read()
        txtDocumento.insert(tk.END, text)

#-----------------------------------------------------------------------------------------------------------#

# def ventanaPrincipal():

tokenizacion = tk.Tk()
tokenizacion.title("Tokenizacion de Caracteres")
tokenizacion.iconbitmap("icon.ico")
tokenizacion.geometry("950x550")
tokenizacion.config(bg="gray99")
#tokenizacion.resizable(False,False)

frCompleto = tk.Frame(tokenizacion, bg="gray99")
frBtnDocumento = tk.Frame(frCompleto, padx=5, pady=5, bg="gray99")
frBtnLista = tk.Frame(frCompleto, padx=5, pady=5, bg="gray99")

label1 = tk.Label(frCompleto, text="Documento: ", bg="gray99", fg="#006BE5", font=("Calibri", 12))
label2 = tk.Label(frCompleto, text="Estructura de Listas: ", bg="gray99", fg="#006BE5", font=("Calibri", 12))

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#
listaTokens = ttk.Treeview(frCompleto)   

listaTokens.insert('', '0', 'documento', text ='Documento') 
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#

#listaTokens = tk.Text(frCompleto, width="30",font=("Calibri", 11), relief=tk.SUNKEN )  
txtDocumento = tk.Text(frCompleto, width="80", font=("Calibri", 11) )

btnAbrir = tk.Button(frBtnDocumento, text="Abrir Archivo", command=leerArchivo, bg="#0288d1", fg="#ffffff", relief=tk.GROOVE, font=("Calibri", 12) )
btnLimpiar = tk.Button(frBtnDocumento, text="Limpiar", command=reiniciarDocumento, bg="#0288d1", fg="#ffffff", relief=tk.GROOVE, font=("Calibri", 12)  )
btnAbrir.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btnLimpiar.grid(row=0, column=1, sticky="ew", padx=5)

btnTokenizar = tk.Button(frBtnLista, text="Tokenizar", command=confirmarTokenizar, bg="#0288d1", fg="#ffffff", relief=tk.GROOVE, font=("Calibri", 12)  )
btnTraducir = tk.Button(frBtnLista, text="Traducir", command=mostrarListasTraducidas, bg="#0288d1", fg="#ffffff", relief=tk.GROOVE, font=("Calibri", 12))
btnTokenizar.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btnTraducir.grid(row=0, column=1, sticky="ew", padx=5)

btnHtml = tk.Button(frCompleto, text="Generar HTML", command=confirmarGenerarHTML, bg="#0288d1", fg="#ffffff", relief=tk.GROOVE, font=("Calibri", 12))

label1.grid(row=0,column=0, sticky="w", padx=5)
txtDocumento.grid(row=1, column=0, sticky="w", padx=10)
frBtnDocumento.grid(row=2, column=0, sticky="se", padx=5, pady=10)
label2.grid(row=0, column=1, sticky="w", padx=5)
listaTokens.grid(row=1, column=1, sticky="ns", padx=5)
frBtnLista.grid(row=2, column=1, sticky="e", padx=5, pady=10)
btnHtml.grid(row=1, column=2, sticky="n", padx=5)

frCompleto.grid(row=0, column=0, padx=15, pady=15)

tokenizacion.mainloop()

#ventanaPrincipal()