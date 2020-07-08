import PP2_LogicaDeNegocio as LDN
import os
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter import PhotoImage
from tkinter.filedialog import askopenfilename

global txtDocumento
global treeViewTokens
global btnGenerarHtml
global ventanaTokenizacion
ventanaTokenizacion = Tk()
ventanaTokenizacion.title("Tokenizacion de Texto")
ventanaTokenizacion.iconbitmap("Recursos/icon.ico")
ventanaTokenizacion.geometry("950x545")
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
