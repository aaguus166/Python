numeros = [2, 7, 25, 10, 44]

#encontrando el numero mayor de una lista
numero_mas_alto = max(numeros)
print(f'el numero mas alto es: {numero_mas_alto}')

#encontrando el numero menor de una lista
numero_mas_bajo = min(numeros)
print(f'el numero mas bajo es: {numero_mas_bajo}')

#redondeando a 6 decimales
numero = round(12.67803,4) #poniendo la coma nos pone la cantidad de decimales
print(numero)

#retorna false -> 0, vacio, false, none / true -> distinto a 0, true, cadena, datos no vacio
numero = bool(8)
print(numero)

#retorna true, si todos los valores son verdaderos
resultado_all = all([["jkjddkj"], "true", [89]])
print(resultado_all)

#suma todos los valores un iterable solo con numeros
suma_total = sum(numeros)
print(f'la suma total es {suma_total}')