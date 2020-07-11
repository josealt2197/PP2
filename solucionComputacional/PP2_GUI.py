#Proyecto Programado 2 - Grupo: 01 
#Interfaz Gráfica del programa de Tokenizaciósn de Texto.
#Estudiantes: Jose Manuel Altamirano Salazar - 2020426159
#             Josué Brenes Alfaro - 2020054427

import PP2_LogicaDeNegocio as LDN
import os
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter import PhotoImage
from tkinter.filedialog import askopenfilename

#Variables Globales para Interfaz Grafica
listaTokens=[]
txtDocumento=""
treeViewTokens=""
btnGenerarHtml=""
ventanaTokenizacion=""

#-----------------------------------------------------------------------------------------------------------#
'''
Entradas:Ninguna
Salidas:Reinicia los valores de las variables globales para el listado de tokens y para el campo de texto
Restricciones: Ninguna
'''
def reiniciarValores():
    global listaTokens
    global treeViewTokens
    global txtDocumento

    listaTokens=[]
    treeViewTokens.delete(*treeViewTokens.get_children())

    txtDocumento.configure(state="normal")
    txtDocumento.delete(0.0, END)

    btnGenerarHtml.config(state="disabled")

#-----------------------------------------------------------------------------------------------------------#
'''
Entradas: Ninguna
Salidas:Elimina el contenido del campo de texto de la venta principal
Restricciones: Ninguna
'''
def comandoReiniciarDocumento():
    global txtDocumento

    txtDocumento.configure(state="normal")
    txtDocumento.delete(0.0, END)


#-----------------------------------------------------------------------------------------------------------#
'''
Entradas:Una cadena de caracteres referente a la ruta de un archivo.
Salidas:Se inserta la cadena de caracteres que contiene el texto que se encontraba dentro del archivo, en el
        cuadro de texto.
Restricciones:La ruta seleccionda debe corresponder a una ruta valida para un archivo de texto.
'''
def comandoLeerArchivo():
    global txtDocumento

    rutaArchivo = askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if not rutaArchivo:
        return
    texto = LDN.leerArchivoTxt(rutaArchivo)
    txtDocumento.delete(0.0, END)
    txtDocumento.insert(END, texto)

#-----------------------------------------------------------------------------------------------------------# 
'''
Entradas: Una lista, un valor numerico entero y una cadena de caracteres
Salidas: Se añaden los elementos de cada categoria al listado de tokens (treeview)
Restricciones: Ninguna.
'''
def listarTokens(lista, posicion, categoria):
    indice=0
    nombreElemento="" 

    treeViewTokens.insert('documento', posicion , categoria, text = categoria)  
    if(lista!=[]):
      while(indice!=len(lista)):
          nombreElemento = categoria + str(indice)
          treeViewTokens.insert(categoria, 'end', nombreElemento , text = str(lista[indice]))
          indice+=1 

#-----------------------------------------------------------------------------------------------------------#
'''
Entradas: Se hace clic sobre el boton con la leyena "Traducir".
Salidas: Mensajes emergentes de informacion, alerta o error sobre el proceso traduccion del texto ingresado
Restricciones: Validar que en el cuadro de texto no este vacío.
'''
def comandoTraducirTokens():
    global txtDocumento
    global treeViewTokens
    tokensTraducidos = []

    titulos=["Articles","Prepositions","Pronouns","Verbs"]
    
    if (txtDocumento.compare("end-1c","==","1.0")):
      messagebox.showwarning("Texto Vacío","NO se ha ingresado ningún texto para ser traducido")
    else:
      resultado=messagebox.askquestion('Traducir Tokens','¿Desea traducir los Tokens extraidos del documento? \nEste proceso podría tomar un momento')

      if resultado=='yes':
          
          tokensTraducidos=LDN.traducirListas(LDN.tokenizarCadena(txtDocumento.get(0.0, END)))

          if(tokensTraducidos[0]!="-1"):

              treeViewTokens.delete(*treeViewTokens.get_children())
              treeViewTokens.insert('', '0', 'documento', text ='Document')

              for indice in range(0,len(tokensTraducidos)):
                  listarTokens(tokensTraducidos[indice], str(indice), titulos[indice])
   
          else:
              messagebox.showerror("Traducir Tokens","Ha ocurrido un error.\nNo ha sido posible traducir los tokens.") 
    
#-----------------------------------------------------------------------------------------------------------# 
'''
Entradas:Se hace clic sobre el boton con la leyena "Tokenizar".
Salidas: Mensajes emergentes de informacion, alerta o error sobre el proceso tokenizacion del texto ingresado
Restricciones: Validar que en el cuadro de texto no este vacío. 
'''
def comandoTokenizarDocumento():
    global txtDocumento
    global treeViewTokens
    global listaTokens
    global btnGenerarHtml

    titulos=["Articulos","Preposiciones","Pronombres","Verbos", "Numeros", "Sin Clasificar"]

    if (txtDocumento.compare("end-1c","==","1.0")):
      messagebox.showwarning("Texto Vacío","NO se ha ingresado ningún texto para ser tokenizado")
    else:
      resultado=messagebox.askquestion("Tokenizar Documento","¿Esta seguro de tokenizar el texto ingresado?")

      if resultado=='yes':

          listaTokens=LDN.tokenizarCadena(txtDocumento.get(0.0, END))

          if(listaTokens[0]!="-1"):

              treeViewTokens.delete(*treeViewTokens.get_children())
              treeViewTokens.insert('', '0', 'documento', text ='Documento')

              for indice in range(0,len(listaTokens)):
                  listarTokens(listaTokens[indice], str(indice), titulos[indice])

              btnGenerarHtml.config(state="normal")
          else:
              messagebox.showerror("Tokenizar Documento","Ha ocurrido un error.\nEl texto no se ha tokenizado.") 

#-----------------------------------------------------------------------------------------------------------#
'''
Entradas: Se hace clic sobre el boton con la leyenda "Generar HTML"
Salidas: Una ventana en la que se confirma el proceso de generar el archivo HTML. En caso de que el usuario
         presione el botón Si/Yes se realiza una llamada a la funcion para generar el archivo HTML.
         En caso que ocurra un error se mostrará otro mensaje informando lo sucedido. 
Restricciones: Validar que se haya tokenizado el texto previamente ingresado.
'''
def comandoGenerarHTML():
    global txtDocumento
    global treeViewTokens
    global listaTokens

    resultado=messagebox.askquestion('Crear HTML','¿Esta seguro de generar el archivo HTML? \nEste proceso podría tomar un momento')

    if resultado=='yes':

        if(LDN.generarHTML(txtDocumento.get(0.0, END),listaTokens)!=-1):
            messagebox.showinfo("Generar HTML","Archivo HTML creado exitosamente.")
            btnGenerarHtml.config(state="disabled")        
        else:
            messagebox.showerror("Generar HTML","Ha ocurrido un error.\nEl archivo HTML NO se ha generado.")

#-----------------------------------------------------------------------------------------------------------#
'''
Entradas: Ninguna
Salidas: Se abre el archivo del Manual de Usuario en el lector de PDF prederterminado del equipo.
Restricciones: Ninguna
'''
def comandoAbrirManual():
    rutaManual = os.path.abspath(os.curdir) + "\Recursos\Manual_Usuario.pdf"
    os.startfile(rutaManual)

#-----------------------------------------------------------------------------------------------------------#
'''
Entradas: Ninguna
Salidas: Se detiene la ejecuccion del programa o de la ventana principal.
Restricciones: Ninguna
'''
def comandoSalir():
    global ventanaTokenizacion
    ventanaTokenizacion.destroy()

#-----------------------------------------------------------------------------------------------------------#
'''
Entradas: Ninguna
Salidas: Se configuran los objetos de la ventana que contiene la informacion sobre el equipo que desarrollo 
         el programa y se invoca.
Restricciones: Ninguna
'''
def comandoAcercaDe():
  window = Tk()
  window.geometry("420x400")
  window.iconbitmap("Recursos/form.ico")
  window.config(bg="LightSkyBlue3")
  window.title("Informacion")
  window.resizable(width=0, height=0)
  lbl0 = Label(window, text="Tecnológico de Costa Rica ", bg="LightSkyBlue3", fg="#000",font=("Verdana", 13))
  lbl2 = Label(window, text="TI 1401 - Taller de Programación", bg="LightSkyBlue3", fg="#000",font=("Verdana", 11))
  lbl4 = Label(window, text="Segundo Proyecto Programado", bg="LightSkyBlue3", fg="#000",font=("Verdana", 11))
  lbl6 = Label(window, text="Programa para Tokenización de Texto", bg="LightSkyBlue3", fg="#000",font=("Verdana", 11))


  lbl8 = Label(window, text="Estudiantes:", bg="LightSkyBlue3", fg="#000",font=("Verdana", 13))
  lbl9 = Label(window, text="José Altamirano Salazar - 2020426139", bg="LightSkyBlue3", fg="#000",font=("Verdana", 11))
  lbl10 = Label(window, text="Josué Brenes Alfaro - 2020054427", bg="LightSkyBlue3", fg="#000",font=("Verdana", 11))

  lbl0.pack(padx=20, pady=7)
  lbl2.pack(padx=20, pady=7)
  lbl4.pack(padx=20, pady=7)
  lbl6.pack(padx=20, pady=7)
  lbl8.pack(padx=20, pady=7)
  lbl9.pack(padx=20, pady=7)
  lbl10.pack(padx=20, pady=7)

  imagen = PhotoImage(master = window, file="Recursos/imagen.gif")
  Label(window, image=imagen, bd=0,bg="LightSkyBlue3").pack()


  window.mainloop()


#-----------------------------------------------------------------------------------------------------------#
'''
Entradas: Ninguna
Salidas: Se configuran los objetos de la ventana principal del programa y se invoca.
Restricciones: Ninguna
'''
def inicio():

  global txtDocumento
  global treeViewTokens
  global btnGenerarHtml
  global ventanaTokenizacion

  ventanaTokenizacion = Tk()
  ventanaTokenizacion.title("Tokenizacion de Texto")
  ventanaTokenizacion.iconbitmap("Recursos/icon.ico")

  ventanaTokenizacion.config(bg="#F8F9FA")
  ventanaTokenizacion.resizable(width=0, height=0) 

  frPrincipal = Frame(ventanaTokenizacion, bg="#F8F9FA", height="850", width="450")
  
  label1 = Label(frPrincipal, text="Documento: ", bg="#F8F9FA", fg="#0288d1", font=("Calibri", 12, "bold"))
  label2 = Label(frPrincipal, text="Estructura de Listas: ", bg="#F8F9FA", fg="#0288d1", font=("Calibri", 12, "bold"))
  
  frameTexto = Frame(frPrincipal, width=250, height=350)

  txtDocumento = Text(frameTexto)

  scrollbarTexto = Scrollbar(frameTexto)
  txtDocumento = Text(frameTexto, width=70, height=25)
  scrollbarTexto.pack(side=RIGHT,fill=Y)
  txtDocumento.pack(side=LEFT, fill=Y)
  scrollbarTexto.config(command=txtDocumento.yview)
  txtDocumento.config(yscrollcommand=scrollbarTexto.set)

  treeViewTokens = ttk.Treeview(frPrincipal) 

  frBtnDocumento = Frame(frPrincipal, padx=5, pady=5, bg="#F8F9FA")
  btnAbrirArchivo = Button(frBtnDocumento, text="Abrir Archivo", command=comandoLeerArchivo, bg="#0288d1", fg="#ffffff", relief=GROOVE, font=("Calibri", 12))
  btnAbrirArchivo.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
  btnLimpiarTexto = Button(frBtnDocumento, text="Limpiar Texto", command=comandoReiniciarDocumento, bg="#0288d1", fg="#ffffff", relief=GROOVE, font=("Calibri", 12)) 
  btnLimpiarTexto.grid(row=0, column=1, sticky="ew", padx=5)

  frBtnLista = Frame(frPrincipal, padx=5, pady=5, bg="#F8F9FA")
  btnTokenizar = Button(frBtnLista, text="Tokenizar", command=comandoTokenizarDocumento, bg="#0288d1", fg="#ffffff", relief=GROOVE, font=("Calibri", 12))
  btnTokenizar.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
  btnTraducir = Button(frBtnLista, text="Traducir", command=comandoTraducirTokens, bg="#0288d1", fg="#ffffff",  relief=GROOVE, font=("Calibri", 12))
  btnTraducir.grid(row=0, column=1, sticky="ew", padx=5)

  btnGenerarHtml = Button(frPrincipal, text="Generar HTML", command=comandoGenerarHTML, bg="#0288d1", fg="#ffffff", state="disabled", relief=GROOVE, font=("Calibri", 12))

  label1.grid(row=0,column=0, sticky="w", padx=5)
  frameTexto.grid(row=1, column=0, sticky="ns", padx=10)
  frBtnDocumento.grid(row=2, column=0, sticky="se", padx=5, pady=10)
  label2.grid(row=0, column=1, sticky="w", padx=5)
  treeViewTokens.grid(row=1, column=1, sticky="ns", padx=5)
  frBtnLista.grid(row=2, column=1, sticky="e", padx=5, pady=10)
  btnGenerarHtml.grid(row=1, column=2, sticky="n", padx=5)

  frPrincipal.pack()

  menuBar = Menu(ventanaTokenizacion)
  menuSuperiorA = Menu(menuBar, tearoff=0)
  menuSuperiorA.add_command(label="Abrir un archivo", command=comandoLeerArchivo)
  menuSuperiorA.add_command(label="Borrar valores", command=reiniciarValores)
  menuSuperiorA.add_command(label="Salir del programa", command=comandoSalir)
  menuBar.add_cascade(label="Opciones", menu=menuSuperiorA)
  menuSuperiorB = Menu(menuBar, tearoff=0)
  menuSuperiorB.add_command(label="Manual de Usuario", command=comandoAbrirManual)
  menuSuperiorB.add_command(label="Acerca de", command=comandoAcercaDe)
  menuBar.add_cascade(label="Ayuda", menu=menuSuperiorB)
  ventanaTokenizacion.config(menu=menuBar)

  ventanaTokenizacion.mainloop()

inicio()