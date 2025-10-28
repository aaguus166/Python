#forma no optima de sumar valores
'''def suma(lista):
    nummeros_sumados = 0
    for numeros in lista:
        nummeros_sumados = nummeros_sumados + numeros
    return nummeros_sumados

resultado = suma([10, 20,30])    
print(resultado)'''

#utilizando el parametro args
def suma (*numeros): # el * le estamos diciendo que es una lista
    return sum(numeros)
resultado = suma(12,20,30)
print(resultado)
    
