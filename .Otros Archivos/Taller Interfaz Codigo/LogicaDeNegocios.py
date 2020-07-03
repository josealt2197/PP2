#Imports
import pickle; #Importamos para serializar y leer archivos
#Fin de los imports

#Variables Globales
lista=[];
letra="";
#Fin de las variables globales

def cargarArchivoLista():
    global lista;

    #try que evita que la aplicacion se caiga por problema de archivos
    try: 
        inFile = open("Lista.txt", "rb"); #Recupera la info del archivo llamado Productos
        lista = pickle.load(inFile);

    #Si falla por algun problema de archivo,  la lista productos sale vacia
    except:
       lista = [];

    return lista;

def cargarArchivoLetra(lista, numero):
    global letra;


    inFile = open(lista[numero][1], "rb");
    letra = inFile.read().decode("utf-8") ;

    return letra;

def cargarArchivoImagen(lista, numero):
    return lista[numero][2];



def cargar():

    lista = [["Bastille - Things We Lost in The Fire - All of this is bad blood","Letra\Things We Lost in The Fire-Bastille.txt","Imagenes\Bastille.gif"],
                ["Coldplay - Magic - Ghost Stories","Letra\Magic-Coldplay.txt","Imagenes\Coldplay.gif"],
                ["Foster the People - Houdini - Torches","Letra\Houdini-Foster the People.txt","Imagenes\Foster.gif"],
                ["Twenty One Pilots - Chlorine - Trench","Letra\Chlorine-Twenty One Pilots.txt","Imagenes\ToP.gif"],
                ["Magpie Jay - Skin of a Bear - Tragaluz", "Letra\Skin of a Bear-Magpie Jay.txt", "Imagenes\Mag.gif"],
		["Low Roar - Bones - Once in a Long Long While", "Letra\Bones-Low Roar.txt", "Imagenes\LowRoar.gif"]]    
    # Escritura en modo binario, vacía el fichero si existe
    fichero = open('Lista.txt','wb')

    # Escribe la colección en el fichero 
    pickle.dump(lista, fichero) 

    fichero.close()

