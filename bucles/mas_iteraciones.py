animales = ["gato", "perro", "pez", "cotorra", "erizo", "caballo", "pato"]
cadena = "lisa, venus" 
numeros = [28, 5, 18]

#evitando adoptar un pez con la sentencia continue
for animal in animales:
  if animal == "pez":
      continue 
  print(f'voy a adoptar un: {animal}')
  

#evitando adoptar mas animales (cuando llegue a caballo se termina de ejecutar) si hay un "else" tampoco se ejecuta
for animal in animales:
    if animal == "caballo":
        break
    print(f'voy a adoptar un: {animal}')
    

#recorrer una cadena de texto
for letra in cadena:
    print(letra)
    
#for en una solalinea de codigo, se puede ser con cualquier operacion
numeros_duplicados = [x * 2 for x in numeros]
print(numeros_duplicados)
