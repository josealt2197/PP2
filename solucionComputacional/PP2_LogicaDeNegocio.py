#Proyecto Programado 2 - Grupo: 01 
#Lógica de Negocio del Programa de Tokenizaciósn de Texto.
#Estudiantes: Jose Manuel Altamirano Salazar - 2020426159
#             Josué Brenes Alfaro - 2020054427

from datetime import datetime
from googletrans import Translator
import re, string

#-----------------------------------------------------------------------------------------------------------#
'''
Entradas:Una cadena de caracteres referente a la ruta de un archivo.
Salidas:Una cadena de caracteres que contiene el texto que se encontraba dentro del archivo.
Restricciones:La ruta recibida debe corresponder a una ruta valida para un archivo de texto.
'''
def leerArchivoTxt(rutaArchivo):
    archivoTexto = open(rutaArchivo,"r", encoding='utf-8')
    cadena = archivoTexto.read()
    archivoTexto.close()
    return cadena

#-----------------------------------------------------------------------------------------------------------#
'''
Entradas: Una lista con todos sus elementos en español
Salidas: Otra lista con los valores de la lista recibida traducidos de español a ingles
Restricciones:No valida restricciones
'''
def traducirLista(listaEspanol):
    listaIngles=[]

    traductor = Translator()
    
    for elemento in listaEspanol:
      traduccion = traductor.translate(elemento, target="en")
      listaIngles.append(traduccion.text)

    return listaIngles

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
def generarHTML(cadena, listaTokens):
    nombreArchivo ="Análisis-"+obtenerFechaActual()+".html"
    textoHTML = ""
    filasHTML = ""
    listaTokensIngles = [[],[],[],[]]

    listaTokensIngles[0] = traducirLista(listaTokens[0])
    listaTokensIngles[1] = traducirLista(listaTokens[1])
    listaTokensIngles[2] = traducirLista(listaTokens[2])
    listaTokensIngles[3] = traducirLista(listaTokens[3])  

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
        <h1>Análisis del documento</h1>
        <table>
          <tr>
            <th>Artículos</th>
            <th>Preposiciones</th>
            <th>Pronombres</th>
            <th>Verbos</th>
            <th>Números</th>
            <th>Sin Clasificar</th>
          </tr>
        """
    filasHTML=filasHTML+agregarFilasHTML(listaTokens)
    textoHTML = textoHTML + filasHTML[:-63] + """ 
        </table>

        <h1>Análisis del documento (traducción)</h1>
        <table>
          <tr>
            <th>Articles</th>
            <th>Prepositions</th>
            <th>Pronouns</th>
            <th>Verbs</th>
          </tr>
        """
    filasHTML=""
    filasHTML=filasHTML+agregarFilasHTMLIngles(listaTokensIngles)
    textoHTML = textoHTML + filasHTML[:-45] +  """        
      </table>
      </center>
      </body>
      </html>
      """

    try:
        Html_file = open(nombreArchivo,"x", encoding='utf-8')
        Html_file.write(textoHTML)
        Html_file.close()
        return 1
    except:
        return -1 

#-----------------------------------------------------------------------------------------------------------#
def agregarFilasHTML(lista):
    filasHTML=""
    indiceX=0
    indiceY=0
    finListas=[False,False,False,False,False,False]

    while(True):
      filasHTML=filasHTML+"<tr>"
      
      for indiceX in range(0,6):
        if(indiceY<len(lista[indiceX])):
          filasHTML=filasHTML+"<td><p>"+str(lista[indiceX][indiceY])+"</p></td>"
        else:
          filasHTML=filasHTML+"<td></td>"
          finListas[indiceX]=True

      filasHTML=filasHTML+"</tr>"
      indiceY+=1   

      if (finListas[0]==True and finListas[1]==True and finListas[2]==True and finListas[3]==True and finListas[4]==True and finListas[5]==True):
        break
      else:
        finListas=[False,False,False,False,False,False]

    return filasHTML

#-----------------------------------------------------------------------------------------------------------#
def agregarFilasHTMLIngles(lista):
    filasHTML=""
    indiceX=0
    indiceY=0
    finListas=[False,False,False,False]

    while(True):
      filasHTML=filasHTML+"<tr>"
      
      for indiceX in range(0,4):
        if(indiceY<len(lista[indiceX])):
          filasHTML=filasHTML+"<td><p>"+str(lista[indiceX][indiceY])+"</p></td>"
        else:
          filasHTML=filasHTML+"<td></td>"
          finListas[indiceX]=True

      filasHTML=filasHTML+"</tr>"
      indiceY+=1   

      if (finListas[0]==True and finListas[1]==True and finListas[2]==True and finListas[3]==True):
        break
      else:
        finListas=[False,False,False,False]

    return filasHTML

#-----------------------------------------------------------------------------------------------------------#
'''
Entradas:Una cadena de caracteres 
Salidas:La misma cadena eliminandole los simbolos que no aparezcan en la variable local abcValido
Restricciones:No valida restricciones
'''
def validarCaracteres(cadena, cadenaResultante="", indice=0):
    abcValido = "abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ1234567890áéíúóüÁÉÍÓÚÜ "
    if(indice>=len(cadena)):
      return cadenaResultante
    else:
      if(abcValido.find(cadena[indice])!=-1):
          return validarCaracteres(cadena, cadenaResultante+cadena[indice], indice+1)
      else:
          return validarCaracteres(cadena, cadenaResultante, indice+1)

#-----------------------------------------------------------------------------------------------------------#
'''
Entradas: Una lista con varios elementos y una cadena de caracteres (palabra)
Salidas: En caso de que se encuentre la palabra buscada dentro de la lista se retorna el valor numerico de la 
         posicion en la que esta se encuentra, caso contrario la funcion retorna el valor numerico -1
Restricciones: Los valores de la lista deben corresponder con tipo del valor ingresado para la palabra del 
               segundo parámetro.
'''
def buscarElemento(lista,palabra):
    return buscarElementoAUX(lista,0,len(lista)-1,palabra)

def buscarElementoAUX(lista,inicio,fin,palabra):
    mitad=(inicio+fin)//2
    if (inicio>fin):
        return -1
    elif(lista[mitad]==palabra):
        return mitad
    elif(lista[mitad]>palabra):
        return buscarElementoAUX(lista,inicio,mitad-1,palabra)
    else:
        return buscarElementoAUX(lista,mitad+1,fin,palabra)

#-----------------------------------------------------------------------------------------------------------#
'''
Entradas:Un caracter 
Salidas:True si el caracter es un numero o False si el caracter no es un numero con decimales
Restricciones:No valida restricciones
'''
def esNumero(caracter):
    try:
        resultado = float(caracter)
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
    elif (palabra[-4:]=="ando" or palabra[-5:]=="iendo"):
        return 2
    elif (palabra[-3:]=="ado" or palabra[-3:]=="ido" or palabra[-2:]=="to" or palabra[-3:]=="cho" or palabra[-2:]=="so"):
        return 3
    else:
        return -1

#-----------------------------------------------------------------------------------------------------------#
'''
Entradas:Una lista de elementos de un mismo tipo.
Salidas:la lista ingresada con sus elementos en orden ascendente
Restricciones:No valida restricciones
'''
def ordenarLista(lista):
    izquierda = []
    pivotes = []
    derecha = []
    if len(lista) > 1:
        pivote = lista[0]
        for indice in lista:
            if indice < pivote:
                izquierda.append(indice)
            elif indice == pivote:
                pivotes.append(indice)
            elif indice > pivote:
                derecha.append(indice)
        return ordenarLista(izquierda)+pivotes+ordenarLista(derecha)
    else:
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
'''
Entradas: Una lista de valores individuales de un mismo tipo
Salidas: Una de con varias sublistas de elementos segun su clasificacion como: articulos, preposiciones, 
         pronombres, verbos, numeros o sin clasificar
Restricciones: No se valida ninguna restriccion 
'''
def clasificarTokens(listaTokenizada):
    listadoTokens=[[],[],[],[],[],[]]

    #Listas para de valores posibles para los elementos
    listaArticulos=['al', 'del', 'el', 'la', 'las', 'lo', 'los', 'un', 'una', 'unas', 'unos']
    listaPreposiciones=['a', 'ante', 'bajo', 'cabe', 'con', 'contra', 'de', 'desde', 'durante', 'en', 'entre', 'hacia', 'hasta', 'mediante', 'para', 'por', 'según', 'sin', 'so', 'sobre', 'tras', 'versus', 'vía']
    listaPronombres=['conmigo', 'consigo', 'contigo', 'ella', 'le', 'les', 'me', 'mí', 'mía', 'mías', 'mío', 'míos', 'nos', 'nosotras', 'nosotros', 'nuestra', 'nuestras', 'nuestro', 'nuestros', 'se', 'suya', 'suyas', 'suyo', 'suyos', 'te', 'ti', 'tuya', 'tuyo', 'tuyos', 'tú', 'vos', 'vosotras', 'vosotros', 'vuestra', 'vuestras', 'vuestro', 'vuestros', 'yo', 'él']

    #Recorrer los elementos de la lista tokenizada y agregarlos a la
    #lista que corresponda cada uno.
    for elemento in listaTokenizada:
        if(buscarElemento(listaArticulos, elemento)!=-1):
            listadoTokens[0].append(elemento)
        elif(buscarElemento(listaPreposiciones, elemento)!=-1):
            listadoTokens[1].append(elemento)
        elif(buscarElemento(listaPronombres, elemento)!=-1):
            listadoTokens[2].append(elemento)
        elif(esVerbo(elemento)!=-1):
            listadoTokens[3].append(elemento)        
        elif(esNumero(elemento)):
            listadoTokens[4].append(elemento)
        elif (elemento!=""):
            listadoTokens[5].append(elemento)

    for indice in range(0, 6):
        listadoTokens[indice]=ordenarLista(listadoTokens[indice])

    for indice in range(0, 6):
        listadoTokens[indice]=eliminarDuplicados(listadoTokens[indice])

    return listadoTokens

#-----------------------------------------------------------------------------------------------------------#
'''
Entradas:Los valores ingresados en el cuadro de texto 
Salidas:Se rellenan los valores de las listas globales con los elementos ingresados dentro del cuadro de texto según su tipo. 
Restricciones:No valida restricciones
'''
def tokenizarCadena(cadena):    
    try:
       #Generar lista con las palabras de la cadena separadas, y sin símbolos
        cadena = cadena.replace("\n", " ")       
        cadenaSinSimbolos = re.sub('[%s]' % re.escape(string.punctuation),' ',cadena)
        cadenaSinSimbolos = validarCaracteres(cadena).lower()
        listaTokenizada = cadenaSinSimbolos.split(" ")
            
        return clasificarTokens(listaTokenizada)

    except Exception as e:
        print(e)         
        return ["-1"]
  
#-----------------------------------------------------------------------------------------------------------#
'''
Entradas:Ninguna
Salidas:Los valores de las listas traducidos omitiendo los valores repetidos dentro de estas, y las listas 
         de numeros y preposiciones
Restricciones: Ninguna
'''
def traducirListas(lista):
    tokensTraducidos=[[],[],[],[],[]]
    try:
      tokensTraducidos[0] = traducirLista(lista[0])
      tokensTraducidos[1] = traducirLista(lista[1])
      tokensTraducidos[2] = traducirLista(lista[2])
      tokensTraducidos[3] = traducirLista(lista[3])

      return tokensTraducidos

    except Exception as e:
        print(e) 
        return ["-1"] 


