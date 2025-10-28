#creando un conjunto con set
conjunto = set(["dato 1"])

#creando un conjunto dentro de otro conjunto
conjunto1 = {"dato 1" , "dato 2"}
conjunto2 = {conjunto1 , "dato 3"}

#teoria de conjuntos. issubest = subconjunto. Esto devuelve true o false
conjunto1 = {1,3,5,8}
conjunto2 = {1,3,8}
resultado = conjunto2.issubset(conjunto1)
#tambien se puede verificar asi
resultado = conjunto2 <= conjunto1


#creando un superconjunto 
conjunto1 = {1,3,5,8}
conjunto2 = {1,3,8}
resultado = conjunto2.issuperset(conjunto1)
#tambien se puede verificar asi
resultado = conjunto2 >= conjunto1

#verificar si hay algun numero en comun. Si hay uno que se repita es false
resultado = conjunto2.isdisjoint(conjunto1)

print(resultado)