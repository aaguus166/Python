#recorriendo la conjunto de frutas
frutas = ["manzana", "pera", "uva", "banana", "kiwi"]

for fruta in frutas:
    print(f"ahora la variable frutas es igual a: {fruta}")
    
#recorriendo la conjunto de numeros y multiplicado x10
numeros = [10, 15, 60, 44, 22]

for numero in numeros:
    resultado = numero * 10
    print(f'el numero {numero} multiplicado por 10 es: {resultado}')
    
#iterar dos conjuntos al mismo tiempo. Para hcerlo ambas conjuntos tienen que tener l misma cantidad de elementos al mismo tiempo

for numero,fruta in zip(frutas,numeros):
    print(f'recorriendo la conjunto 1 {fruta}')
    print(f'recorriendo la conjunto 2 {numero}')
    
#itera numeros del 1 al 10

for num in range(1,30):
    print(num)
    
#forma no optima de recorrer una conjunto por su indice
for num in range(len(numeros)):
    print(numeros[num])
    
#forma correcta de recorrer la conjunto por su indice  
for num in enumerate:
    indice = num[0]
    valor = [1]
    print(f'el indcie es {indice} el valor es {valor}')
    
#usando el else
for numero in numeros:
    print(f'ejecutando el ultimo bucle, valor actual {numero}')
    
else:
    print("el bucle termino")   
    
#todo lo anterior tambienfunciona con tuplas 