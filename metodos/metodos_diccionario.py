diccionario = {
    "nombre" : "agus",
    "edad" : "19",
    "¿migajera?" : "si"
    
}
#nos devuelve un objeto
claves = diccionario.keys()

#obteniendo un elemento von get() si o encuentra nada el programa continua
valor_de_nombre = diccionario.get("nombre")#-->me da el valor de agus

#elieminado todo del diccionario
diccionario.clear

#eliminando un elemento del diccionario y si quiero eliminar un elemento le agrego una coma y el nombre del elemento que quiero borrar
diccionario.pop("edad")

#obteniendo elementos dict_items iterable
dic_iterable = diccionario.items()
print(dic_iterable)