#método de string es una función especial que viene incorporada en los objetos tipo texto y que te permite modificar, analizar o trabajar con cadenas fácilmente.
#Los metodos son un dato un . y el ()

cadena1 = "tengo mucho sueño"
cadena2 = "me duele la espalda"

#Cuando le pasás un objeto (por ejemplo, una cadena, una lista, un número), te devuelve una lista con los nombres de todos los métodos y propiedades que podés usar en ese objeto. Esto es una funcion

#print(dir(cadena1))

#convierte a mayusculas
mayusc = cadena1.upper()

#convierte a minuscula
minusc = cadena1.lower()

#primer letra en mayuscula
primer_letra_mayusc = cadena1.capitalize()

#buscamos una cadena en otra cadea/los espacios tambien se cuenta. si no hay coincidencia devuelve valor -1
busqueda_find = cadena1.find("o")

#busqueda en una cadena en otra cadena si no hay coincidencia lanza una excepcion
busqueda_index = cadena1.index("g")

# si es numerico devolvemos true, sino false ejemplo que da true cadena1 = ''774'' SIN cadena de texto
es_numerico = cadena1.isnumeric()

#si es alfa numerico devolvemos true sino false ejemplo: "duki" SIN numeros los espacios no son alfa numericos
es_alfa = cadena1.isalphanum()

#busqueda en una cadena en otra cadena si hay coincidencia devuelve la cantidad de veces que se repita
contar_coincidencia = cadena1.count("o")

#contamos cuantos caracteres hay en una cadena (no es un metodo es una funcion)
contar_caracteres = len(cadena1)

#verificamos si una cadena empieza con otra cadena dada, si es asi devuelve true
empiza_con = cadena1.startswith("g")

##verificamos si una cadena termina con otra cadena dada, si es asi devuelve true
empiza_con = cadena1.endswithswith("o")

#replaza un pedazo de la cadena dada, por otra dada
cadena_nueva = cadena1.replace("gojo" , "nanami") #reemplaza gojo por nanami

#separa las cadenas con la cadena que le demos
cadena_separada = cadena1.split(",")


 






