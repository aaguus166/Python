'''Pedir datos al usuario y guardarlos en un diccionario:

Mostrar solo las claves

Mostrar solo los valores'''

contador = 0
diccionarioUser = {
 
}

while contador < 3:
 contador+=1
 claveUser = input("ingrese clave ")
 ValorUser = input("ingrese valor ")
 diccionarioUser[claveUser] = ValorUser

print(f'el diccionario es el siguiente: {diccionarioUser}')
print(f'las claves son {diccionarioUser.keys()}')
print(f'los valores son: {diccionarioUser.values()}')

