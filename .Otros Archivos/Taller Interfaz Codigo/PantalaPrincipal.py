from tkinter import *
import LogicaDeNegocios as IDN
from PIL import Image, ImageTk

listaDatos=[]
pantalla=""
frameImagen=""
listbox=""
textArea=""
pantallaPrincipal=""

def cargarImagen(listaDatos,numero):
    global frameImagen

    frameImagen.destroy()

    frameImagen = Frame(pantallaPrincipal, width=250, height=250)
    frameImagen.place(x="145", y="100")

    ubicacionImagen = IDN.cargarArchivoImagen(listaDatos, numero)

    img = Image.open(ubicacionImagen)
    img = img.resize((250, 250), Image.BICUBIC)
    tkimage = ImageTk.PhotoImage(img)
    labelImage = Label(frameImagen, image=tkimage, width=250, height=250).pack()

    pantalla.mainloop()

def cargarLetra(listaDatos,numero):
    global textArea

    letra = IDN.cargarArchivoLetra(listaDatos, numero)
    textArea.configure(state="normal")
    textArea.delete(0.0, END)
    textArea.insert(END, letra)
    textArea.configure(state="disabled")


def comandoBoton1():
    global listbox
    global listaDatos

    numero = listbox.index(ACTIVE)

    cargarLetra(listaDatos, numero)
    cargarImagen(listaDatos, numero)

def comandoBoton2():
    print("") 

def crearPantallaPrincipal():
    global pantallaPrincipal
    global listaDatos
    global pantalla
    global frameImagen
    global listbox
    global textArea
    global pantallaPrincipal
    
    try:
        pantallaPrincipal.destroy()
    except:
        pantallaPrincipal=""

    pantallaPrincipal = Frame (pantalla, bg="#3e2050", bd="0", height="750", width="1000")
    pantallaPrincipal.pack()

    label0 = Label(pantallaPrincipal, font=('Arial', 25), text="TEC Music",  bg="#3e2050", fg="#29a891")
    label0.place(x="425", y="50")  

    frameImagen = Frame(pantallaPrincipal, width=250, height=250)
    frameImagen.place(x="145", y="100")  

    label1 = Label(pantallaPrincipal, font=('Arial', 16), text="Lista:",  bg="#3e2050", fg="#29a891")
    label1.place(x="750", y="100")

    listaDatos = IDN.cargarArchivoLista()

    frameLista = Frame(pantallaPrincipal, width=250, height=150)
    frameLista.place(x="650", y="150") 

    scrollbar = Scrollbar(frameLista)
    listbox = Listbox(frameLista, width=45, height=5)
    scrollbar.pack(side=RIGHT,fill=Y)
    listbox.pack(side=LEFT, fill=Y)
    scrollbar.config(command=listbox.yview)
    listbox.config(yscrollcommand=scrollbar.set)

    for item in listaDatos:
        listbox.insert(END,item[0])

    boton1 = Button(pantallaPrincipal, text="Seleccionar", command=comandoBoton1, bg="#FFC300", fg="#29a891")
    boton1.place(x="750", y="250")

    boton2 = Button(pantallaPrincipal, text="Reproducir", command=comandoBoton2, bg="#FFC300", fg="#29a891", state="disabled")
    boton2.place(x="750", y="350")

    frameLetra = Frame(pantallaPrincipal, width=350, height=350)
    frameLetra.place(x="85", y="375")

    scrollbarLetra = Scrollbar(frameLetra)
    textArea = Text(frameLetra, width=45, height=5)
    scrollbarLetra.pack(side=RIGHT,fill=Y)
    textArea.pack(side=LEFT, fill=Y)
    scrollbarLetra.config(command=textArea.yview)
    textArea.config(yscrollcommand=scrollbarLetra.set)
    textArea.config(state="disabled")

    pantallaPrincipal.mainloop()

def PantallasExtras():
    global pantallaPrincipal
    global pantalla

    pantallaPrincipal.destroy()

    pantallaPrincipal = Frame(pantalla, bg="#3e2050", bd="0", width=1000, height=750)
    pantallaPrincipal.pack()

    label0 = Label(pantallaPrincipal, font=('Arial', 50), text="Proximamente",  bg="#3e2050", fg="#29a891")
    label0.place(x="275", y="325") 


def salirDeSesion():
    import LoginUser as ui
    global pantalla
    pantalla.destroy()
    ui.inicio()

def salir():
    global pantalla
    pantalla.destroy()

def inicio():
    global pantallaPrincipal
    global pantalla

    pantalla=Tk()
    pantalla.title("TEC Music")
    pantalla.geometry("1000x650+250+5")
    pantalla.resizable(False,False)

    menubar = Menu(pantalla)

    gestionCancionesMenu = Menu(menubar, tearoff=0)

    gestionCancionesMenu.add_command(label="Reproductor", command=crearPantallaPrincipal)
    gestionCancionesMenu.add_command(label="Agregar Canciones", command=PantallasExtras)
    gestionCancionesMenu.add_command(label="Eliminar Canciones", command=PantallasExtras)
    menubar.add_cascade(label="Gestion de Canciones", menu=gestionCancionesMenu)

    pantallaMenu = Menu(menubar, tearoff=0)

    pantallaMenu.add_command(label="Cerrar Sesion", command=salirDeSesion)
    pantallaMenu.add_command(label="Salir", command=salir)
    menubar.add_cascade(label="Sesion", menu=pantallaMenu)

    pantalla.config(menu=menubar)
    crearPantallaPrincipal()

