"""
tipos de datos basicos
-enteros(int): numeros sin decimales.
-decimales(float): numeros con decimales.
cadenas de textos(str):texto entre comillas.
-booleanos(bool): valores trues o false.

"""""
"""
eje 2: crear una variable booleana que indique
si aprobaste un examen (true/false)
"""
aprobado = True

print("aprobado",aprobado)

calificacion1 = 7
calificacion2 = 2
calificacion3 = 9

print(calificacion1 + calificacion2 + calificacion3 /3 )


#ejemplo
print("tipo numerico",  type(24))
print("tipo con decimales", type(3.14))
print("tipo cadena de texto(string)", type("hola"))
print("tipo verdadero o falso (true or false)", type(True))

"""
operaciones aritmeticas: operadores principales:
(+) suma, (-) resta, (*) multiplicacion, (/) divicion, (//) divicion entera, (%) nodulo, (**) potencia.


"""

"""
entrada de data con imput()
la funcion input() permite leer datos que ingresa el usuario por teclado
ejemplo: nombre = input("ingrese su nombre")

eje 4: calcular el promedio de 3 notas que el usuario
ingrese por teclado
"""

calificacion_1 = int( input("calificacin1"))
calificacion_2 = int( input("calificacion2"))
calificacion_3 = int( input("calificacion3"))

print(calificacion_1 + calificacion_2 + calificacion_3 /3 )