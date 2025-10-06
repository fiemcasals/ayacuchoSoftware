"""
Tipos de datos basicos
- Enteros (int): Números de decimales.
- Decimales (float): Números con decimales.
- Cadenas de texto (strings): Texto entre comillas.
- Booleanos (bool): Valores true or false.
"""
#Ejemplo
print("Tipo numerico(int)", type(24))
print("Tipo con decimales)", type(3.14))
print("Tipo cadena de texto(string))", type("hola"))
print("Tipo verdadero o falso (True or False))", type(True))
"""
Ejercicio 2: Crear una variable booleana que indique si aprobaste un examen (T o F).
"""

aprobado = True

print("Aprobado:", aprobado, "Felicidades aprobaste el examen")

"""
Operaciones aritmeticas: Operadores principales: 
(+) Suma, (-) Resta, (*) Multiplicacion, (/) Division, (//) Division entera, (%) Modulo, (**) Potencia.

Ejercicio 3: Calcular el promedio de tres calificaciones.
"""
calificacion1 = 7
calificacion2 = 4
calificacion3 = 10

print("Tu promedio es:", calificacion1+calificacion2+calificacion3/3)

"""
Entrada de datos con input()
La funcion input() permite leer datos que ingresa el usuario por teclado
ejemplo: nombre = input("Ingrese su nombre")
"""

"""
Ejercicio 4: calcular el promedio de 3 notas que el usuario ingrese por teclado
"""
calificacion_1 = int(input ("ingrese su primera calificacion "))
calificacion_2 = int(input ("ingrese su segunda calificacion "))
calificacion_3 = int(input ("ingrese su tercera calificacion "))

print(calificacion_1 + calificacion_2 + calificacion_3 / 3)
