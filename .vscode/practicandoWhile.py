#🔹 Ejercicio 1 – Continuar o salir

#Pedí números y sumalos mientras el usuario quiera seguir.

seguir = True
suma = 0

while seguir:
    entrada = input("Ingrese un numero (s para salir): ")

    if entrada == "s":
        seguir = False
    else:
        numero = int(entrada)
        suma += numero

print("La suma total es:", suma)
