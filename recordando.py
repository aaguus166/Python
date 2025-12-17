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

#4) Pedí un número y decí si es:positivo, negativo, o cero

numero = int(input("ingrese numero "))

if numero > 0: 
  print(f'el numero ingresado es {numero} y es positvo')

elif numero < 0:
   print(f'el numero ingresado es {numero} y es negativo')

else:
   
   (f'el numero ingresado es {numero} y es 0')

print("----------------------------")

#Pedí un número y decí si es par o impar.

numero = int(input("ingrese numero "))

if numero % 2 == 0:
   print(f'el numero ingresado es {numero} y es par')
else:
   print(f'el numero ingresado es {numero} y es impar')

print("---------------------------------")

#Mostrá los números del 1 al 10 usando:for y después con while

print("usando for")
for i in range(1, 11):
   print(i)

print("usando while")
i = 1
while i <= 10:
   print(i)
   i+=1

print("----------------------------")

#Tabla de multiplicar
#Pedí un número y mostrà su tabla del 1 al 10.

N = int(input("igrese numero "))
print(f'el numero ingresado fue {N} y su tabla de multiplicar es ')

for i in range(1, 11):
   print(f'{N}X{i} = {N*i}')

#Pedí números hasta que el usuario ingrese 0 y mostrà la suma total.

suma = 0

num = int(input("ingrese un numero (0 para terminar): "))

while num != 0:
    suma += num
    num = int(input("mngrese un numero (0 para terminar): "))

print("la suma total es:", suma)

 