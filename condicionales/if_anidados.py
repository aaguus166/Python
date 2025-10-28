#if dentro de otro if se usa para verificar una segunda condicion 
# PERO si solo la primera se cumple.

edad = 16
tiene_dni = True

if edad >= 16:
  if tiene_dni:
      print("puede votar")
  else:
      print("necesita dni para votar")
else:
    print("es menor de edad")      
      
