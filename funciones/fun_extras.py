#creando una funcion con tres parametros
'''def frase (nombre, apellido, adjetivo):
    return f'hola {nombre} {apellido} sos una {adjetivo}'

resultado = frase("agus", "torres", "capa")
print(resultado)'''

#utilizando keyword arguments (argumentos de palabras claves)
'''def frase (nombre, apellido, adjetivo):
    return f'hola {nombre} {apellido} sos una {adjetivo}'

#resultado = frase(adjetivo = "capa", apellido = "torres", nombre = "agus")
#print(resultado)'''

#creando a funcion con un parametro opcional y un valor por defecto
def frase (nombre, apellido, adjetivo = "inteligente"):
    return f'hola {nombre} {apellido} sos una {adjetivo}'

resultado = frase("agus", "torres", "bruta")
print(resultado)
 #el valor por defecto seria inteligente y el parametro opcional seria adjetivo
 #el valor por defecto se puede cambiar
    

