'''1) Hola mundo y variables
Mostrá en pantalla: Hola, Python
Guardá tu edad en una variable y mostrá: "Tengo X años", donde X es el valor de la variable.'''

edad = 19

print(f'hola python tengo {edad} años')

print("---------------------------------------")
#------------------------------------------------

'''2)Operaciones básicas

Pedí dos números al usuario y mostrà: suma, resta, multiplicación, división'''

num1 = int(input("ingrese el primer numero "))
num2 = int(input("igrese el segundo numero "))
resultado = num1+num2
resultado2 = num1 - num2
resultado3 = num1*num2
resultado4 = num1 % num2

print(f'el resultado de la suma es {resultado} ')
print(f'el resultado de la resta es {resultado2}')
print(f'el resultado de la multiplicacion es {resultado3}')
print(f'el resultado de la division es {resultado4}')

print("----------------------------------------------------")
#-------------------------------------------------------------

#3) Pedí un número y decí si es:positivo, negativo, o cero

numero = int(input("ingrese numero "))

if numero > 0: 
  print(f'el numero ingresado es {numero} y es positvo')

elif numero < 0:
   print(f'el numero ingresado es {numero} y es negativo')

else:
   
   (f'el numero ingresado es {numero} y es 0')

print("----------------------------")

#4) Pedí un número y decí si es par o impar.

numero = int(input("ingrese numero "))

if numero % 2 == 0:
   print(f'el numero ingresado es {numero} y es par')
else:
   print(f'el numero ingresado es {numero} y es impar')

print("---------------------------------")

#5) Mostrá los números del 1 al 10 usando:for y después con while

print("usando for")
for i in range(1, 11):
   print(i)

print("usando while")
i = 1
while i <= 10:
   print(i)
   i+=1

print("----------------------------")

#6) Tabla de multiplicar
#Pedí un número y mostrà su tabla del 1 al 10.

N = int(input("igrese numero "))
print(f'el numero ingresado fue {N} y su tabla de multiplicar es ')

for i in range(1, 11):
   print(f'{N}X{i} = {N*i}')

#7) Pedí números hasta que el usuario ingrese 0 y mostrà la suma total.

suma = 0

num = int(input("ingrese un numero (0 para terminar): "))

while num != 0:
    suma += num
    num = int(input("mngrese un numero (0 para terminar): "))

print("la suma total es:", suma)

print("----------------------------")

#8) Pedí 5 números y mostrá cuál fue el mayor.

mayor = int(input("ingrese un numero: "))

for i in range(4):
    num = int(input("ingrese un numero: "))
    if num > mayor:
        mayor = num

print("el mayor es:", mayor)
print("---------------------------------")


#9) Lista de números
# Pedí 5 números. Guardalos en una lista, Mostrá:la lista, la suma el promedio

numeros = []

for i in range(5):
 num = int(input("ingrese numero "))
 numeros.append(num)

 suma = sum(numeros)
 promedio = suma % len (numeros)

 
 
print(f'mostrando lista {numeros}')
print(f'mostrando suma {suma}')
print(f'mostrando promedio {promedio}')

print("--------------------------------")

#10) Contar vocales
# Pedí una palabra y contá cuántas vocales tiene.

palabra = input("ingrese una palabra: ")

contador = 0
vocales = "aeiou"

for letra in palabra:
    if letra in vocales:
        contador += 1

print(f'la palabra {palabra} tiene {contador} vocales')

   


#11) Un poco de lógica
#1️⃣5️⃣ Adivinar número. La compu genera un número del 1 al 100.El usuario intenta adivinarlo.El programa avisa si es mayor o menor


import random

numero = random.randint(1, 100)

while True:
    intento = int(input("Adivina el numero: "))

    if intento == numero:
        print("¡Correcto!")
        break
    elif intento < numero:
        print("Es mayor")
    else:
        print("Es menor")




