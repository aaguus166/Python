#Creando una lista(se pueden modificar)
lista = ["lisa", "venus", True, 1.55, 44]
print(lista[3])

#Creando una tupla (no se puede modificar)
tupla = ("lisa", "venus", True, 1.55, 44)
print(tupla[1])

#Esto esvalido
lista[3] = "pochita"

#esto no
#tupla[1] = "pochita"

#creando un conjunto (set) no se accede por elementos indice, no almacena datos duplicados
conjunto = {"lisa", "venus", True, 1.55, 44}
#print(conjunto[0])-->no se puede hacer eso

#creando un diccionario (dic) la estructura es key : value y separamos por comas
diccionario = {
    "nombre" : "agus",
    "edad" : "19",
    "estudia" : "programacion"
}
print(diccionario["edad"])
