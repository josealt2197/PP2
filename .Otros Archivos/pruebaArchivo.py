# def guardarArchivo():
# 	html_str = """
# 	<table border=1>
# 	     <tr>
# 	       <th>Number</th>
# 	       <th>Square</th>
# 	     </tr>
# 	     <indent>
# 	       <tr>
# 	         <td><p>1</p></td>
# 	         <td><p>3</p></td>
# 	       </tr>
# 	     </indent>
# 	</table>
# 	"""

# 	Html_file= open("prueba3.html","x")
# 	Html_file.write(html_str)
# 	Html_file.close()

# def leerArchivo():
# 	txt_file = open("prueba2.html","r")
# 	cadena = txt_file.read()
# 	print(cadena)
# 	txt_file.close()
    
# def eliminarSimbolos(cadena):
# 	abcValido = "abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ1234567890. áéíúóüÁÉÍÓÚÜ"
# 	cadenaResultante = ""
# 	for caracter in cadena:
# 		if(abcValido.find(caracter)!=-1):
# 			cadenaResultante = cadenaResultante + caracter

# 	return cadenaResultante
# #------------------------------------------Definir tipo de palabra----------------------------------------------#
# '''
# Entradas:Una cadena de caracteres 
# Salidas:El Tipo de palabra (articulo,preposición,pronombre,verbo,numero,no clasificado)
# restricción:no valida restricciones
# '''
# def definirTipoDePalabra(palabra):
# 	palabra.lower()
# 	art=["el", "la", "los", "las", "Un", "una", "unos", "unas", "Lo", "al", "del"]
# 	prep=["a", "ante", "bajo", "cabe", "con", "contra", "de", "desde", "durante", "en", "entre", "hacia", "hasta", "mediante", "para", "por", "según", "sin", "so", "sobre", "tras", "versus", "vía"]
# 	pron=["yo", "me", "mí", "conmigo", "nosotros", "nosotras", "nos", "tú", "te", "ti", "contigo", "vosotros", "vosotras", "vos", "él", "ella", "se", "consigo", "le", "les","Mío", "mía", "míos", "mías", "nuestro", "nuestra", "nuestros", "nuestras", "tuyo", "tuya", "tuyos", "vuestro", "vuestra", "vuestros", "vuestras", "suyo", "suya", "suyos", "suyas"]
	
# 	for i in art:
# 		if (palabra==i):
# 			return "Articulo"
# 	for i in prep:
# 		if (palabra==i):
# 			return "Preposición"
# 	for i in pron:
# 		if (palabra==i):
# 			return "Pronombre"
# 	if (esNumero(palabra)) :
# 		return "Numero"
# 	if (palabra[-2:]=="ar" or palabra[-2:]=="er" or palabra[-2:]=="ir"):
# 	   	return "verbo infinitivo"
# 	if (palabra[-4:]=="ando" or palabra[-4:]=="endo"):
# 		return "verbo gerundio"
# 	if (palabra[-3:]=="ado" or palabra[-3:]=="ido" or palabra[-2:]=="to" or palabra[-3:]=="cho" or palabra[-2:]=="so"):
# 		return "verbo participio"
# 	else:
#    		return "no se clasifica"

# def esNumero(n):
#   try:
#   	int(n)
#   	return True
#   except:
#   	return False
# #------------------------------------------------------------------------------------------------------------#

from translate import Translator

def traducir(cadena):
	translator= Translator(from_lang="Spanish",to_lang="English")
	translation = translator.translate(cadena)
	print(translation)




