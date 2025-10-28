#creando una lista con list
lista = list(["hola", "mundo", 77])

#cuenta la cantidad de elementos de una lista
cantidad_elementos = len(lista)

#agregando un elemento a la lista 
lista.append("torta")

#agregando un elemento a la lista en un indice especifico
lista.insert(1, "coca")

#agregando varios elemetos a la lista
lista.extend(["lisa", "venus"])

#eliminado elementos de la lista por su indice
lista.pop(3) #si adentro ponemos -1 nos elimina el ultimo elemento y asi sucesivamente

#removiendo un elemento por su valor
lista.remove("torta")#nos elimina la palabra torta

#elimina todos los elementos de la lista
lista.clear()

#ordenando la lista esto se hace sin strings. Si le ponemos ese parametro nos ordena a lista en reversa (tambien in strings)
list.sort(reverse=True)

#invirtiendo los elementos de la lista puede estar desordenada lista pero igual la revierte
lista.reverse()

print(lista)