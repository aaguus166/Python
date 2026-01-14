'''Pedir una frase al usuario y: Mostrarla en mayúsculas, Contar cuántos caracteres tiene y Contar cuántas veces aparece la letra "a"'''

fraseUser = input("ingrese frase ")

mayusculas = fraseUser.upper()
contarCaracteres = len(mayusculas)
contarletra_A = mayusculas.count("A")

print(f"la frase {mayusculas} tiene en total {contarCaracteres} de caracteres y la letra 'a' se repite {contarletra_A} veces")

print("----------------------------------------")


'''Pedir un nombre completo y:

Mostrar solo el nombre

Mostrar solo el apellido

Verificar si empieza con una letra específica'''

nombreUser = input("ingrese su nombre completo ")
nombreCompleto = nombreUser.split()
nombre = nombreCompleto[0]
apellido = nombreCompleto[1]

empizaName = nombre.lower().startswith("s")
empiezaSurname = apellido.lower().startswith("r")


print(f"el nombre completo es {nombreCompleto} su nombre es {nombre} y el apellido es {apellido}")

print(f"el nombre si empieza con la letra 's' ({empizaName})")
print(f"el apellido si empiza con la letra 'r' ({empiezaSurname})")

print("----------------------------------------")

'''Pedir una contraseña:

Verificar si tiene más de 8 caracteres

Verificar si es alfanumérica'''

passwordUser = input("ingrese contraseña ")
es_alfa = passwordUser.isalpha()

if len(passwordUser) > 8 and es_alfa:
    print("la contraseña tiene mas de 8 caracteres y es alfanumerica")
else:
    print("la contraseña tiene menos de ocho caracteres y no es alfanumerica")

print("-------------------------")


'''Crear una lista con 5 números:

Mostrar el mayor

Mostrar el menor

Mostrar la suma total'''


lista = [30, 20, 46, 10, 8]


for i in range(4):
    numMax = max(lista)
    numMin = min(lista)
    sumaLista = sum(lista)

print(f"la lista de numeros es {lista}")
print(f"el numero mayor es {numMax} el numero menor es {numMin} y la suma total total de la lista es {sumaLista}")

print("------------------------------")

'''Pedir 5 nombres y guardarlos en una lista:

Mostrar la lista ordenada

Mostrar la lista invertida'''

listaUser = []
contador = 0

while contador < 5:
    contador+=1
    namesUser = input("ingrese nombre  ")
    listaUser.append(namesUser)
    
listaUser.reverse()

print(f"los cinco nombres ingresados fueron: {listaUser}")
print(f"la lista inververtida es {listaUser}")


