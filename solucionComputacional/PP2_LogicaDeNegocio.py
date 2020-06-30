from datetime import datetime
from translate import Translator
import re, string

#-----------------------------------------------------------------------------------------------------------#
'''
Entradas:Una cadena de caracteres referente a la ruta de un archivo.
Salidas:Una cadena de caracteres que contiene el texto que se encontraba dentro del archivo.
Restricciones:La ruta recibida debe corresponder a una ruta valida para un archivo de texto.
'''
def leerArchivoTxt(rutaArchivo):
    archivoTexto = open(rutaArchivo,"r")
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

    tradutor = Translator(from_lang="Spanish",to_lang="English")

    for elemento in listaEspanol:
      listaIngles.append(tradutor.translate(elemento))

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
    filasHTML = ""

    articles = eliminarDuplicados(traducirLista(listaTokens[0]))
    prepositions = eliminarDuplicados(traducirLista(listaTokens[1]))
    pronouns = eliminarDuplicados(traducirLista(listaTokens[2]))
    verbs = eliminarDuplicados(traducirLista(listaTokens[3]))

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
      
      if(indice<len(listaTokens[0])):
        filasHTML=filasHTML+"<td><p>"+str(listaTokens[0][indice])+"</p></td>"
      else:
        filasHTML=filasHTML+"<td></td>"
        finArticulos=True

      if(indice<len(listaTokens[1])):
        filasHTML=filasHTML+"<td><p>"+str(listaTokens[1][indice])+"</p></td>"
      else:
        filasHTML=filasHTML+"<td></td>"
        finPreposiciones=True

      if(indice<len(listaTokens[2])):
        filasHTML=filasHTML+"<td><p>"+str(listaTokens[2][indice])+"</p></td>"
      else:
        filasHTML=filasHTML+"<td></td>"
        finPronombres=True

      if(indice<len(listaTokens[3])):
        filasHTML=filasHTML+"<td><p>"+str(listaTokens[3][indice])+"</p></td>"
      else:
        filasHTML=filasHTML+"<td></td>"
        finVerbos=True

      if(indice<len(listaTokens[4])):
        filasHTML=filasHTML+"<td><p>"+str(listaTokens[4][indice])+"</p></td>"
      else:
        filasHTML=filasHTML+"<td></td>"
        finNumeros=True

      if(indice<len(listaTokens[5])):
        filasHTML=filasHTML+"<td><p>"+str(listaTokens[5][indice])+"</p></td>"
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
def validarCaracteres(cadena, cadenaResultante="", indice=0):
    abcValido = "abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ1234567890áéíúóüÁÉÍÓÚÜ "
    if(indice>=len(cadena)):
      return cadenaResultante
    else:
      if(abcValido.find(cadena[indice])!=-1):
          return validarCaracteres(cadena, cadenaResultante+cadena[indice], indice+1)
      # elif(cadena[indice+1:]!=False):
      #   if(indice==0 and cadena[indice]=="."):
      #     return eliminarSimbolos(cadena, cadenaResultante, indice+1)
      #   elif(cadena[indice]=="." and esEntero(cadena[indice-1]) and esEntero(cadena[indice+1])):
      #     return eliminarSimbolos(cadena, cadenaResultante+cadena[indice], indice+1)
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
def buscarElemento(lista, palabra):
    indice = 0

    while (indice != len(lista)):
        if (lista[indice] == palabra):
            return indice
        indice += 1

    return -1

# def buscarElemento(lista,palabra):
#     return buscarElementoAUX(list,0,len(list)-1,element)

# def buscarElementoAUX(lista,inicio,fin,palabra):
#     mitad=(inicio+fin)//2
#     if (inicio>fin):
#         return -1
#     elif(lista[mitad]==palabra):
#         return mitad
#     elif(lista[mitad]>palabra):
#         return buscarElementoAUX(lista,inicio,mitad-1,palabra)
#     else:
#         return buscarElementoAUX(lista,mitad+1,fin,palabra)

#-----------------------------------------------------------------------------------------------------------#
'''
Entradas:Un caracter 
Salidas:True si el caracter es un numero o False si el caracter no es un numero entero
Restricciones:No valida restricciones
'''
def esEntero(caracter):
    try:
        resultado = int(caracter)
        return True
    except:
        return False

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
'''
Entradas:Los valores ingresados en el cuadro de texto 
Salidas:Se rellenan los valores de las listas globales con los elementos ingresados dentro del cuadro de texto según su tipo. 
Restricciones:No valida restricciones
'''
def tokenizarCadena(cadena):
    listadoTokens=[[],[],[],[],[],[],[]]
    #Listas para guardar los valores tokenizados (En Español)
    articulos=[]
    preposiciones=[]
    pronombres=[]
    verbos=[]
    numeros=[]
    sinClasificar=[]

    #Listas para de valores posibles para los elementos
    listaArticulos=["el", "la", "los", "las", "un", "una", "unos", "unas", "lo", "al", "del"]
    listaPreposiciones=["a", "ante", "bajo", "cabe", "con", "contra", "de", "desde", "durante", "en", "entre", "hacia", "hasta", "mediante", "para", "por", "según", "sin", "so", "sobre", "tras", "versus", "vía"]
    listaPronombres=["yo", "me", "mí", "conmigo", "nosotros", "nosotras", "nos", "tú", "te", "ti", "contigo", "vosotros", "vosotras", "vos", "él", "ella", "se", "consigo", "le", "les","mío", "mía", "míos", "mías", "nuestro", "nuestra", "nuestros", "nuestras", "tuyo", "tuya", "tuyos", "vuestro", "vuestra", "vuestros", "vuestras", "suyo", "suya", "suyos", "suyas"]

    try:
        '''Proceso de tokenizacion
            1. Eliminar todos los simbolos, menos los signos de puntuacion 
            2. Crear una lista con los tokens separados por espacios o signos de signos de puntuacion
                (se eliminan todos los signos menos los puntos)
            3. Clasificar los tokens que sean numeros, incluidos los decimales, sacarlos de la lista de tokens
            4. Eliminar los puntos restantes de los tokes de la lista.
            5. Clasificar el resto de los tokens
            
            . --> A o . -->1 . 1 

       '''
       #Lista con las palabras de la cadena separadas, y sin símbolos
        #cadenaSinSaltos = re.sub('[%s]' % re.escape('\n'),' ',cadena)
        cadena = cadena.replace("\n", " ")       
        cadenaSinSimbolos = re.sub('[%s]' % re.escape(string.punctuation),' ',cadena)
        cadenaSinSimbolos = validarCaracteres(cadena).lower()
        #cadenaSinSimbolos.replace("\n", " ")
        listaTokenizada = cadenaSinSimbolos.split(" ")

        #Recorrer los elementos de la lista tokenizada y agregarlos a la
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

        listadoTokens[0]=ordenarLista(eliminarDuplicados(articulos))
        listadoTokens[1]=ordenarLista(eliminarDuplicados(preposiciones))
        listadoTokens[2]=ordenarLista(eliminarDuplicados(pronombres))
        listadoTokens[3]=ordenarLista(eliminarDuplicados(verbos))
        listadoTokens[4]=ordenarLista(eliminarDuplicados(numeros))
        listadoTokens[5]=ordenarLista(eliminarDuplicados(sinClasificar))

        try:
          listadoTokens[5].remove('')
        except Exception as e:
          print(e)

                
        return listadoTokens

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


