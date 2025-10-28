#creando una funcion simple
'''def saludar ():
    print("hola mundo")
saludar()'''

#creando una funcion con parametros
def saludar(nombre): #-> esto es un parametro, es una variable que existe dentro de la funcion 
    print(f'hola {nombre} :)')
    
saludar("mundo")
def crear_contraseña(num):
    chars = "abcdefghujkl" #creamos caracteres aleatorios
    num_entero = str(num) #convierte a strig el primer numero
    num = int(num_entero[0])#obtenemos el primer numero,ejemplo 120 = 1
    c1 = num - 2 #aca le resta 2, 120 - 2 =118
    c2 = num  #aca vale 10, 120-10 = 110
    c3 = num - 3 #aca vale 3, 120-3 = 117
    contraseña = f'{chars[c1]}, {chars[c2]}, {chars[c3]} {num * 2}' 
    print(contraseña)

password = crear_contraseña(4)
frase = f'tu nueva contraseña es {password}'
print(frase)