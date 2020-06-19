#Listas para guardar los valores tokenizados
articulos=[]
preposiciones=[]
pronombres=[]
verbos=[]
numeros=[]
sinClasificar=[]

#-----------------------------------------------------------------------------------------------------------#
def obtenerFechaActual():
    from datetime import datetime
    now = datetime.now()
    fechaFormato=str(now.day)+"-"+str(now.month)+"-"+str(now.year)+"-"+str(now.hour)+"-"+str(now.minute)+"-"+str(now.second)

    return fechaFormato

#-----------------------------------------------------------------------------------------------------------#
def generarHTML(cadena):
    nombreArchivo ="Análisis-"+obtenerFechaActual()+".html"
    #     <tr>
    #   <th>Number</th>
    #   <th>Square</th>
    # </tr>
    html_top = """
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
          margin: 0;
          top:0;
          left:0;
        }

        section {
          display: -webkit-flex;
          display: flex;
        }

        article {
          -webkit-flex: 3;
          -ms-flex: 3;
          flex: 3;
          background-color: #fff;
          padding: 10px;
        }

        @media (max-width: 1000px) {
          section {
            -webkit-flex-direction: column;
            flex-direction: column;
          }
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

      <section>
        <article>
          <h1>Contenido Analizado</h1>
          <p>
    """

    html_bottom = """ 
         </p>
      <hr>
      <h1>Análisis del documento</h1>
      <table>
        <tr>
          <th>Articulos</th>
          <th>Preposiciones</th>
          <th>Pronombres</th>
          <th>Verbos</th>
          <th>Numeros</th>
          <th>Sin Clasificar</th>
        </tr>
        <tr>
          <td> </td>
          <td> </td>
          <td> </td>
          <td> </td>
          <td> </td>
          <td> </td>
        </tr>
        <tr>
          <td> </td>
          <td> </td>
          <td> </td>
          <td> </td>
          <td> </td>
          <td> </td>
        </tr>
      </table>

      <h1>Analisis del documento</h1>
      <table>
        <tr>
          <th>Articulos</th>
          <th>Preposiciones</th>
          <th>Pronombres</th>
          <th>Verbos</th>
        </tr>
        <tr>
          <td> </td>
          <td> </td>
          <td> </td>
          <td> </td>
        </tr>
        <tr>
          <td> </td>
          <td> </td>
          <td> </td>
          <td> </td>
        </tr>
      </table>

    </article>
  </section>

</body>
</html>
"""
    html_text=cadena
    
##    html_rows=""
##
##    for elemento in articulos:
##        html_rows=html_rows+"<tr><td><p>"+str(elemento)+"</p></td></tr>"

    try:
        Html_file= open(nombreArchivo,"x")
        Html_file.write(html_top+html_text+html_bottom)
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
    abcValido = "abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ1234567890. áéíúóüÁÉÍÓÚÜ"
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

    return nuevaLista

#-----------------------------------------------------------------------------------------------------------#
def tokenizarCadena(cadena):
    #Listas para de valores posibles para los elementos
    listaArticulos=["el", "la", "los", "las", "un", "una", "unos", "unas", "lo", "al", "del"]
    listaPreposiciones=["a", "ante", "bajo", "cabe", "con", "contra", "de", "desde", "durante", "en", "entre", "hacia", "hasta", "mediante", "para", "por", "según", "sin", "so", "sobre", "tras", "versus", "vía"]
    listaPronombres=["yo", "me", "mí", "conmigo", "nosotros", "nosotras", "nos", "tú", "te", "ti", "contigo", "vosotros", "vosotras", "vos", "él", "ella", "se", "consigo", "le", "les","mío", "mía", "míos", "mías", "nuestro", "nuestra", "nuestros", "nuestras", "tuyo", "tuya", "tuyos", "vuestro", "vuestra", "vuestros", "vuestras", "suyo", "suya", "suyos", "suyas"]


    #Lista con las palabras de la cadena separadas, y sin símbolos
    listaTokenizada = eliminarSimbolos(cadena).lower().split()

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

#-----------------------------------------------------------------------------------------------------------#
def mostrarListas():
    
    print("\n\tListas de Elementos")
    print("\n-->Articulos: ",ordenarLista(articulos))
    print("-->Preposiciones: ",ordenarLista(preposiciones))
    print("-->Pronombres: ",ordenarLista(pronombres))
    print("-->Verbos: ",ordenarLista(verbos))
    print("-->Numero: ",ordenarLista(numeros))
    print("-->Sin Clasificar: ",ordenarLista(sinClasificar))

#------------------------------------------Opcion Secundaria--------------------------------------------#
def opcionSecundaria(cadena):
    opcion=0
    print("\n\t¿Desea generar el archivo HTML?.")
    print("\n\t1. Si")
    print("\t2. No")

    try:
        opcion = int(input("\n<--Opcion: "))
    except:
        print("\t***************************************")
        print("\t*         Opcion NO valida            *")
        print("\t***************************************")

    if (opcion == 1):

        if(generarHTML(cadena)==1):
            print("\n-->Archivo HTML generado exitosamente.")
        else:
            print("\t*****************************************************")
            print("\t*Se ha producido un error al generar el archivo HTML*")
            print("\t*****************************************************")

        #Reiniciar los valores de las listas
        articulos=[]
        preposiciones=[]
        pronombres=[]
        verbos=[]
        numeros=[]
        sinClasificar=[]

    elif (opcion == 2):
        #Reiniciar los valores de las listas
        articulos=[]
        preposiciones=[]
        pronombres=[]
        verbos=[]
        numeros=[]
        sinClasificar=[]
        
    else:
        print("\t***************************************")
        print("\t*Opcion no valida, vuelva a intentarlo*")
        print("\t***************************************")
        menuPrincipal()

#------------------------------------------Menu Principal----------------------------------------------#

def menuPrincipal():
    opcion=0
    print("\n\t\t≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈")
    print("\t\t     Tokenización")
    print("\t\t≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈")

    while(opcion!=3):
        print("\n\t\t--------------------")
        print("\t\t   Menú Principal")
        print("\t\t--------------------")
        print("\n\tSeleccione una de las opciones.")
        print("\tDigite el numero correspondiente.")
        print("\n\t1. Ingresar cadena de texto")
        print("\t2. Leer archivo de texto")
        print("\t3. Finalizar Programa")

        try:
            opcion = int(input("\n<--Opcion: "))
        except:
            print("\t***************************************")
            print("\t*Opcion no valida, vuelva a intentarlo*")
            print("\t***************************************")
            menuPrincipal()

        if (opcion == 1):
            cadena = input("\n<--Ingrese la frase o palabra que desea tokenizar: ")
            tokenizarCadena(cadena)
            mostrarListas()
            opcionSecundaria(cadena)

        elif (opcion == 2):
            ruta = input("\n<--Ingrese la ruta del archivo de texto: ")
            cadena=leerArchivoTxt(ruta)
            tokenizarCadena(cadena)
            mostrarListas()
            opcionSecundaria(cadena)

        elif (opcion == 3):
            print("\n\t»»»»»»»»»»»»»»»»»»»»»")
            print("\t»Programa Finalizado»")
            print("\t»»»»»»»»»»»»»»»»»»»»»")
            #sys.exit(0)
        else:
            print("\t***************************************")
            print("\t*Opcion no valida, vuelva a intentarlo*")
            print("\t***************************************")
            menuPrincipal()

menuPrincipal()
