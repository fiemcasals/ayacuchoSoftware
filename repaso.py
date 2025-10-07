#vamos a ver conceptos basicos de python

#que es una variable?
#defino una variable 

#tiene un nombre
#guarda un valor
#puedo cambiar su valor
#puedo usar su valor


#vamos a poner un ejemplo

name = "juan"
age = 17 #entero #cada tipo de dato tiene operaciones propias #cada tipo de dato ocupa un espacio en memoria.
height = 1.75 #float

#vamos a imprimir estos datos.

#print("Mi nombre es", name, ", tengo", age, "años y mido", height, "metros.")

#otra manera de imprimir es print(f"mi nombre es ...{name}").
#print(f"Mi nombre es {name}, tengo {age} años y mido {height} metros.")


#vamos a imprimir el nombre solo si el sujeto tiene mas de 18 años.

# if age > 18:
#     print(f"Mi nombre es {name}, tengo {age} años y mido {height} metros.")
# elif age == 18:
#     print("tengo que preguntar si quiere decir su edad")
# else: 
#     print("No puedo decir mi nombre porque soy menor de edad.")


#datos para trabajar

Nombre = "Maria Belen"
Edad = 17
Estudiante = "Si"

# print(Nombre)
# print(Edad)
# print(Estudiante)
# ctr /

# if Estudiante == "Si" and Edad >= 18:
#     print(f"Mi nombre es {Nombre}, tengo {Edad} años y soy estudiante.")
# elif Estudiante == "Si" or Edad >= 18:
#     print(f"Mi nombre es {Nombre}, tengo {Edad} años y soy estudiante.")
# else:
#     print("no cumple ninguna de las condiciones anteriores")

# while True: #es un bucle infinito que solo se sale cuando la condicion se deja de cumplir o con un break
#     if Estudiante == "Si":
#         print("es estudiante")
#         break
#     if Edad >= 18:
#         print("es mayor de edad")
#         break

# numero = 0
# while numero <20:
#     print(f"el numero es {numero}")
#     numero += 1 #numero = numero + 1
#     #vamos con un ejemplo de division
#     #numero /=2 # numero = numero / 2



#vamos a pedirle al usuario que ingrese datos por pantalla
# dni = int(input("Ingrese su DNI: ")) #devuelve siempre un string
# print(f"Su DNI es {dni}")
# #me confundi le quiero restar 60 
# dni_corregido = dni - 60 #no puedo restar un string con un entero #un string es una concatenacion de caracteres
# print(f"Su DNI corregido es {dni_corregido}")

#voy a explicar for

# for i in range(5):
#     print(f"el valor de i es {i}")

#podemos definir en range el valor inicial, el final y el paso
# for j in range(2, 10, 2): #la condicion implicita seria j < 10 
#     print(f"el valor de j es {j}")

# #podemos imprimir para atras.
# for k in range(10, 0, -1): #la condicion implicita seria k > 0 k!=0 
#     print(f"el valor de k es {k}")

#vamos a ver lo que es una lista
# lista = [1,2,3,4,5,6]

# for elemento in lista:
#     print(f"el elemento es {elemento}")

#vamos a declarar  una lista con string
# lista_nombres = ["juan", "pedro", "maria", "ana"]
# #imprimo los nombres de la lista
# for nombre in lista_nombres:
#     print(f"el nombre es {nombre}")

#vamos a pedir nombres con un input y lo guardamos en una lista con append
lista_nombres = []

#vamos a generar una estructura que pida nombres de manera repetitiva hasta alcanzar 3 registros
for i in range(3):
    nombre = input(f"Ingrese el nombre {i+1}: ")
    lista_nombres.append(nombre)

print("Los nombres ingresados son:")
for nombre in lista_nombres:
    print(f"- {nombre}")

#print(lista_nombres)

#vamos a usar random.choice para seleccionar un nombre al azar
# import random
# nombre_azar = random.choice(lista_nombres)
# print(f"El nombre seleccionado al azar es: {nombre_azar}")

# #el vecto tiene la particularidad de que se puede indexar
# lista_nombres[0] #primer elemento

#ahora voy a imprimir usando el indice
for i in range(3):
    print(f"el nombre en la posicion {i} es {lista_nombres[i]}")


#explicar len. sirve para saber cuantos elementos tiene un arreglo
print(f"la lista tiene {len(lista_nombres)} elementos")


while len(lista_nombres) < 5:
    nombre = input(f"Ingrese el nombres {len(lista_nombres)+1}: ")
    lista_nombres.append(nombre)
print(f"la lista quedo asi: {lista_nombres}")