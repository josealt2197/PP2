from tkinter import *
import PantalaPrincipal as pp

loginUser=""
nombreUsuario=""
contrasena=""

def comandoBoton1():
    loginUser.destroy()

def comandoBoton2():
    global nombreUsuario
    global contrasena

    nombreUsuarioRespaldo = nombreUsuario.get()
    contrasenaRespaldo = contrasena.get()

    usuarioYaExiste = False

    if(nombreUsuarioRespaldo.lower()==str("usuario".lower())):

        if(contrasenaRespaldo==str("123")):
            usuarioYaExiste = True

    if(usuarioYaExiste!=False):
        loginUser.destroy()
        pp.inicio()

    else:
        label3 = Label(loginUser, text="Contraseña o usuario incorrecto",  bg="#3e2050", fg="#29a891")
        label3.grid(row=4,column=2) 
            
    

def inicio():

    global loginUser
    global nombreUsuario
    global contrasena

    loginUser=Tk()
    loginUser.title("TEC Music - Iniciar Seccion")
    loginUser.geometry("300x125")
    loginUser.config(bg="#3e2050")
    loginUser.resizable(False,False)

    boton1 = Button(loginUser, text="Salir", command=comandoBoton1, bg="#FFC300", fg="#29A891")
    boton1.grid(row=1,column=1)
    
    label1 = Label(loginUser, text="Iniciar Sesion",  bg="#3e2050", fg="#29a891")
    label1.grid(row=1,column=2)
    
    label1 = Label(loginUser, text="Nombre: ",  bg="#3e2050", fg="#29a891")
    label1.grid(row=2,column=1)

    nombreUsuario_StringVar = StringVar()
    nombreUsuario = Entry(loginUser, bg="#ffffff", fg="#29a891", textvariable=nombreUsuario_StringVar, width="35")
    nombreUsuario.grid(row=2,column=2)

    label3 = Label(loginUser, text="Contraseña: ",  bg="#3e2050", fg="#29a891")
    label3.grid(row=3,column=1)

    contrasena_StringVar = StringVar()
    contrasena = Entry(loginUser, bg="#ffffff", fg="#29a891", textvariable=contrasena_StringVar, show="*", width="35")
    contrasena.grid(row=3,column=2)

    boton2 = Button(loginUser, text="Iniciar Sesion", command=comandoBoton2, bg="#1A1A1B", fg="#29a891")
    boton2.grid(row=5,column=2)

    loginUser.mainloop()
