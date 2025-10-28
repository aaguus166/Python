#crando diccionario  con dic (es como crear variables dentro del parametro)
diccionario = dict(nombre = "agus", apellido = "torres")

#las listas no pueden ser claves y usamos frozenset para meter conjuntos
diccionario = {frozenset (["lisa", "venus"]): "pochita"}

#creando diccionario con fromkeys() valor por defecto: none
diccionario = dict.fromkeys("nombre", "apellido", "edad")

#creando diccionario con fromkeys() valor por defecyo: no se
diccionario = dict.fromkeys(["nombre", "apellido", "edad"], "nose")