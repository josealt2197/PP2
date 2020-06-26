from translate import Translator

def traducir(cadena):
	translator= Translator(from_lang="Spanish",to_lang="English")
	translation = translator.translate(cadena)
	print(translation)

#------------------------------------------------------------------------------------------------------------#
# Eliminar Símbolos, no recursivo
#------------------------------------------------------------------------------------------------------------#
def eliminarSimbolos(cadena):
    abcValido = "abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ1234567890áéíúóüÁÉÍÓÚÜ.,;: "
    cadenaResultante = ""
    for caracter in cadena:
        if(abcValido.find(caracter)!=-1):
            cadenaResultante = cadenaResultante + caracter

    return cadenaResultante

#------------------------------------------------------------------------------------------------------------#
# Buscar Elemento, no recursivo
#------------------------------------------------------------------------------------------------------------#
def buscarElemento(lista, palabra):
    indice = 0

    while (indice != len(lista)):
        if (lista[indice] == palabra):
            return indice
        indice += 1

    return -1


def eliminarDuplicadosRecursivo(lista,nuevaLista=[]):
    if (lista==[]):
        return nuevaLista
    else:
        if (buscarElemento(nuevaLista,lista[0])==-1):
            return eliminarDuplicadosRecursivo(lista[1:],nuevaLista+[lista[0]])
        else:
            return eliminarDuplicadosRecursivo(lista[1:],nuevaLista)


#-----------------------------------------------------------------------------------------------------
def traducirLista(listaEspanol):
    listaIngles=[]

    tradutor = Translator(from_lang="Spanish",to_lang="English")

    for elemento in listaEspanol:
      listaIngles.append(tradutor.translate(elemento))

    return listaIngles


def interNum(num1,num2):
    inter=0
    while(num1>0 and num2>0):
        if((num1%10)==(num2%10)):
            inter=inter,num1%10

        num1//10 and num2//10
        return inter