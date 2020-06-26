from tkinter import *  
from tkinter import ttk   

app = Tk()   

app.title("Prueba de Treeview")   
  
# ttk.Label(app, text ="Treeview(herarquico)").pack() 
  
# Creating treeview window 
listaTokens = ttk.Treeview(app)   
  
# Calling pack method on the treeview 
listaTokens.pack()   

listaTokens.insert('', '0', 'documento', text ='Documento') 

listaTokens.insert('documento', '0', 'articulos', text ='Articulos')
listaTokens.insert('articulos', 'end', '0A', text ='el')
listaTokens.insert('articulos', 'end', '0B', text ='un')
listaTokens.insert('articulos', 'end', '0C', text ='la')

listaTokens.insert('documento', '1', 'preposiciones', text ='Preposiciones')
listaTokens.insert('preposiciones', 'end', '1A', text ='ante')

listaTokens.insert('documento', '2', 'pronombres', text ='Pronombres')
listaTokens.insert('pronombres', 'end', '2A', text ='él')
listaTokens.insert('pronombres', 'end', '2B', text ='ellos')
listaTokens.insert('pronombres', 'end', '2C', text ='nuestro') 

listaTokens.insert('documento', '3', 'numeros', text ='Numeros')
listaTokens.insert('numeros', 'end', '3A', text ='145')

listaTokens.insert('documento', '4', 'verbos', text ='Verbos')
listaTokens.insert('verbos', 'end', '4A', text ='nadar')
listaTokens.insert('verbos', 'end', '4B', text ='mirando')

listaTokens.insert('documento', '5', 'sinClasificar', text ='Sin Clasificar')
listaTokens.insert('sinClasificar', 'end', '5A', text ='casa')
listaTokens.insert('sinClasificar', 'end', '5B', text ='amarillo')
  
# # Placing each child items in parent widget 
# listaTokens.move('item2', 'item1', 'end')   
# listaTokens.move('item3', 'item1B', 'end') 
# listaTokens.move('item4', 'item1C', 'end') 
  
# Calling main()   
app.mainloop() 