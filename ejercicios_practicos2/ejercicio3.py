# Hacé una lista con nombres de tus 5 amigxs.
# Pedile al usuario que ingrese un nombre y decile si está en la lista o no.

lista = ["meli" , "karen", "sabri" , "brisa" , "sere"]

nombre = input("ingrese un nombre ")

if nombre in lista:
    print("el nombre ingresado esta en la lista")
    
else:
    print("el nombre ingresado no esta en lista")