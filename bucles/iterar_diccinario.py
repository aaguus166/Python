diccionario = {
    "nombre" : "agus",
    "apellido":"tores",
    "edad" : 19 
}
#recorriendo el diccionario para obtener las claves
for key in diccionario:
    key
    print(f'la clave es {key}')
    
    
#recorriendo el diccionario coon items() para obtener las claves y los valores
for datos in diccionario.items():
    key = datos [0]
    value = [1]
    print(f'la clave es: {key} y el valor es: {value}')
    
    