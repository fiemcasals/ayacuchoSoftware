# Tarea: practicar los temas vistos en clase. 
# variable, print, input, condicionales, for, while.
# tipo de datos, operadores logicos, listas: indice, .append() y len()

#variable, tipo de datos

name = "Gonzalo" #string
age = 35 #integer
height = 1.80 #float
estudiante = True #boolean
print(type(name))
print(type(age))
print(type(height))
print(type(estudiante))

#imprimir datos.
print("Mi nombre es " + name + " y tengo " + str(age) + " años." + " Mi estatura es " + str(height) + ".")
print(f"Mi nombre es {name} y tengo {age} años. Mi estatura es {height}")
print("Mi nombre es {} y tengo {} años. Mi estatura es {:.2f}".format(name, age, height))


##### TRABAJAR CON LISTAS #####
lista_productos = []

print("Iniciar lista de compras")
while True:
    if len(lista_productos):
        print(f"Su lista tiene {len(lista_productos)} productos. {lista_productos}")
    
    print(f"Ingrese el {len(lista_productos)+1}° producto.")
    print(f"Ingrese ok para terminar")
    producto = input()
    if producto == "ok":
        break
    else:
        lista_productos.append(producto)

print(f"La lista tiene {len(lista_productos)} productos.")

for producto in lista_productos:
    print(f"- {producto}")
##### TRABAJAR CON LISTAS #####


##### REPASO #####
print("Registro de usuario")
print("Ingrese su nombre")
nombre_usuario = input()
print("Ingrese su email")
email_usuario = input()
print("Ingrese su contraseña")
contraseña_usuario = input()
estado_login = False

print(f"{nombre_usuario} inicie el login de usuario")
while not estado_login:
    print("Ingrese su email")
    email = input()
    print("Ingrese su contraseña")
    contraseña = input()
    if email == email_usuario and contraseña == contraseña_usuario:
        estado_login = True
        print(f"{nombre_usuario}, su login fue exitoso.")
        break
    else:
        print(f"{nombre_usuario}, hay un error en los datos. Intente de nuevo.")
##### REPASO #####

##### libreria random #####