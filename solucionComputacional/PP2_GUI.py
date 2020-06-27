import PP2_LogicaDeNegocio as LDN

from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter.filedialog import askopenfilename

#Variables Globales para Interfaz Grafica
listaTokens=[]
txtDocumento=""
treeViewTokens=""
btnTokenizar=""
btnTraducir=""
btnGenerarHtml=""

'''
generafilas(filas="", x=0, y=0):
  global recursos
  filas=filas+"<tr>"

  return generafilas(filas="") 

  Primera Ejecucion (Para listas con = tamaño)
    funcionRecursiva --> recursos[1] --> recursos(0,0)=recursos[articulos[0]]
    funcionRecursiva --> recursos[2] --> recursos(1,0)=recursos[preposiciones[0]]
    funcionRecursiva --> recursos[3] --> recursos(2,0)=recursos[pronombres[0]]
    funcionRecursiva --> recursos[4] --> recursos(3,0)=recursos[verbos[0]]
    funcionRecursiva --> recursos[5] --> recursos(4,0)=recursos[numeros[0]]
    funcionRecursiva --> recursos[6] --> recursos(5,0)=recursos[sinClasificar[0]]

  Segunda Ejecucion
    funcionRecursiva --> recursos[1] --> recursos(0,1)=recursos[articulos[1]]
    funcionRecursiva --> recursos[2] --> recursos(1,1)=recursos[preposiciones[1]]
    funcionRecursiva --> recursos[3] --> recursos(2,1)=recursos[pronombres[1]]
    funcionRecursiva --> recursos[4] --> recursos(3,1)=recursos[verbos[1]]
    funcionRecursiva --> recursos[5] --> recursos(4,1)=recursos[numeros[1]]
    funcionRecursiva --> recursos[6] --> recursos(6,1)=recursos[sinClasificar[1]]
   
'''

#-----------------------------------------------------------------------------------------------------------#
'''
Entradas:Ninguna
Salidas:Reinicia los los valores de las variables globales para los tokens e invoce la funcion 
        para deshabilitar lo botones
Restricciones: Ninguna
'''
def reiniciarValores():
    global listaTokens
    global treeViewTokens

    listaTokens=[]
    treeViewTokens.delete(*treeViewTokens.get_children())

#-----------------------------------------------------------------------------------------------------------#
'''
Entradas: Ninguna
Salidas:Elimina el contenido del campo de texto de la venta principal
Restricciones: Ninguna
'''
def comandoReiniciarDocumento():
    global txtDocumento
    global btnTokenizar
    global btnTraducir

    btnTokenizar.config(state="disabled")
    btnTraducir.config(state="disabled") 
    txtDocumento.configure(state="normal")
    txtDocumento.delete(0.0, END)


#-----------------------------------------------------------------------------------------------------------#
'''
Entradas:Una cadena de caracteres referente a la ruta de un archivo.
Salidas:Una cadena de caracteres que contiene el texto que se encontraba dentro del archivo.
Restricciones:La ruta seleccionda debe corresponder a una ruta valida para un archivo de texto.
'''
def comandoLeerArchivo():
    global txtDocumento
    global btnTokenizar
    global btnTraducir 

    rutaArchivo = askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if not rutaArchivo:
        return
    texto = LDN.leerArchivoTxt(rutaArchivo)
    txtDocumento.configure(state="normal")
    txtDocumento.delete(0.0, END)
    txtDocumento.insert(END, texto)
    btnTokenizar.config(state="normal")
    btnTraducir.config(state="disabled")
    
#-----------------------------------------------------------------------------------------------------------# 
'''
Entradas:Se hace clic sobre el boton con la leyena "Tokenizar".
Salidas:Una ventana en la cual pregunta si desea tokenizar lo ingresado en el cuadro de texto.
Restricciones:Verificar que en el cuadro de texto existan elementos. 
'''
def comandoTokenizarDocumento():
    global txtDocumento
    global treeViewTokens
    global listaTokens
    global btnGenerarHtml

    titulos=["Articulos","Preposiciones","Pronombres","Verbos","Numeros","Sin Clasificar"]
    

    resultado=messagebox.askquestion("Tokenizar Documento","¿Esta seguro de tokenizar el texto ingresado?")

    if resultado=='yes':

        reiniciarValores()
        listaTokens=LDN.tokenizarCadena(txtDocumento.get(0.0, END))

        if(listaTokens[0]!="-1"):

            treeViewTokens.delete(*treeViewTokens.get_children())
            treeViewTokens.insert('', '0', 'documento', text ='Documento')

            for indice in range(0,len(listaTokens)-1):
                listarTokens(listaTokens[indice], str(indice), titulos[indice])

            btnGenerarHtml.config(state="normal")
        else:
            messagebox.showerror("Tokenizar Documento","Ha ocurrido un error.\nEl texto no se ha tokenizado.")

#-----------------------------------------------------------------------------------------------------------# 
'''
Entradas:Se hace clic sobre el boton con la leyena "Tokenizar".
Salidas:Una ventana en la cual pregunta si desea tokenizar lo ingresado en el cuadro de texto.
Restricciones:Verificar que en el cuadro de texto existan elementos. 
'''
def listarTokens(lista, posicion, categoria):
    indice=0
    nombreElemento=""

    btnTraducir.config(state="disabled") 

    treeViewTokens.insert('documento', posicion , categoria, text = categoria)  
    if(lista!=[]):
      while(indice!=len(lista)):
          nombreElemento = categoria + str(indice)
          treeViewTokens.insert(categoria, 'end', nombreElemento , text = str(lista[indice]))
          indice+=1
          btnTraducir.config(state="normal") 

#-----------------------------------------------------------------------------------------------------------#
'''
Entradas:Ninguna
Salidas:Los valores de las variables globales omitiendo los valores repetidos dentro de estas
Restricciones: Ninguna
'''
def comandoTraducirTokens():
    global txtDocumento
    global treeViewTokens
    global listaTokens

    # articles = eliminarDuplicados(traducirLista(listaTokens()))
    # prepositions = eliminarDuplicados(traducirLista(listaTokens))
    # pronouns = eliminarDuplicados(traducirLista(listaTokens))
    # verbs = eliminarDuplicados(traducirLista(listaTokens))

    # treeViewTokens.delete(0.0, END)
    # listasConcatenadas = "-->Articles:\n"+str(ordenarLista(articles))+"\n\n-->Prepositions:\n"+str(ordenarLista(prepositions))+"\n\n-->Pronouns:\n"+str(ordenarLista(pronombres))+"\n\n-->Verbs:\n"+str(ordenarLista(verbos))
    # treeViewTokens.insert(END, listasConcatenadas)     

#-----------------------------------------------------------------------------------------------------------#
'''
Entradas: Se hace clic sobre el boton con la leyenda "Generar HTML"
Salidas: Una ventana en la que se confirma el proceso de generar el archivo HTML. En caso de que se el usuario
         presione el botón Si/Yes se realiza una llamada a la funcion para generar el archivo HTML.
Restricciones:Validar que se haya tokenizado el texto previamente ingresado
'''
def comandoGenerarHTML():
    global txtDocumento
    global treeViewTokens
    global listaTokens

    resultado=messagebox.askquestion('Crear HTML','¿Esta seguro de generar el archivo HTML? \nEste proceso podría tomar un momento')

    if resultado=='yes':

        if(LDN.generarHTML(txtDocumento.get(0.0, END),listaTokens)!=-1):
            messagebox.showinfo("Generar HTML","Archivo HTML creado exitosamente.")
            reiniciarValores()
            btnGenerarHtml.config(state="disabled")
            btnTraducir.config(state="disabled")          
        else:
            messagebox.showerror("Generar HTML","Ha ocurrido un error.\nEl archivo HTML NO se ha generado.")

#-----------------------------------------------------------------------------------------------------------#
'''
Entradas:
Salidas: 
Restricciones:
'''
def comandoAbrirManual():
    print("abrirManualUsuario")

#-----------------------------------------------------------------------------------------------------------#

def inicio():

  global txtDocumento
  global treeViewTokens
  global btnTokenizar
  global btnTraducir
  global btnGenerarHtml

  ventanaTokenizacion = Tk()
  ventanaTokenizacion.title("Tokenizacion de Caracteres")
  ventanaTokenizacion.iconbitmap("icon.ico")
  ventanaTokenizacion.geometry("950x550")
  ventanaTokenizacion.config(bg="#F8F9FA")
  ventanaTokenizacion.resizable(False,False)

  frPrincipal = Frame(ventanaTokenizacion, bg="#F8F9FA", height="950", width="550")
  
  label1 = Label(frPrincipal, text="Documento: ", bg="#F8F9FA", fg="#006BE5", font=("Calibri", 12))
  label2 = Label(frPrincipal, text="Estructura de Listas: ", bg="#F8F9FA", fg="#006BE5", font=("Calibri", 12))

  txtDocumento = Text(frPrincipal, width="80", font=("Calibri", 11) )
  treeViewTokens = ttk.Treeview(frPrincipal) 

  frBtnDocumento = Frame(frPrincipal, padx=5, pady=5, bg="#F8F9FA")
  btnAbrirArchivo = Button(frBtnDocumento, text="Abrir Archivo", command=comandoLeerArchivo, bg="#0288d1", fg="#ffffff", relief=GROOVE, font=("Calibri", 12))
  btnAbrirArchivo.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
  btnLimpiarTexto = Button(frBtnDocumento, text="Limpiar Texto", command=comandoReiniciarDocumento, bg="#0288d1", fg="#ffffff", relief=GROOVE, font=("Calibri", 12)) 
  btnLimpiarTexto.grid(row=0, column=1, sticky="ew", padx=5)

  frBtnLista = Frame(frPrincipal, padx=5, pady=5, bg="#F8F9FA")
  btnTokenizar = Button(frBtnLista, text="Tokenizar", command=comandoTokenizarDocumento, bg="#0288d1", fg="#ffffff", state="disabled", relief=GROOVE, font=("Calibri", 12))
  btnTokenizar.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
  btnTraducir = Button(frBtnLista, text="Traducir", command=comandoTraducirTokens, bg="#0288d1", fg="#ffffff", state="disabled", relief=GROOVE, font=("Calibri", 12))
  btnTraducir.grid(row=0, column=1, sticky="ew", padx=5)

  btnGenerarHtml = Button(frPrincipal, text="Generar HTML", command=comandoGenerarHTML, bg="#0288d1", fg="#ffffff", state="disabled", relief=GROOVE, font=("Calibri", 12))

  label1.grid(row=0,column=0, sticky="w", padx=5)
  txtDocumento.grid(row=1, column=0, sticky="w", padx=10)
  frBtnDocumento.grid(row=2, column=0, sticky="se", padx=5, pady=10)
  label2.grid(row=0, column=1, sticky="w", padx=5)
  treeViewTokens.grid(row=1, column=1, sticky="ns", padx=5)
  frBtnLista.grid(row=2, column=1, sticky="e", padx=5, pady=10)
  btnGenerarHtml.grid(row=1, column=2, sticky="n", padx=5)

  frPrincipal.pack()

  menuBar = Menu(ventanaTokenizacion)
  menuSuperior = Menu(menuBar, tearoff=0, activebackground="#0288d1", activeforeground="#ffffff")
  menuSuperior.add_command(label="Manual de Usuario", command=comandoAbrirManual)
  menuBar.add_cascade(label="Ayuda", menu=menuSuperior)
  ventanaTokenizacion.config(menu=menuBar)

  ventanaTokenizacion.mainloop()

