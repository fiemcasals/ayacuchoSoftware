
# def get_cost():
#     print("el costo es 10 pesos")


# get_cost()

# def get_costo(a): #'a' representa la cantidad de horas
#     suma = a * 30000
#     print(f"{suma}")


# get_costo(4) #fue una sesion de 4 horas

def multiplicar(primer_valor:int, segundo_valor:int)->int:
    return primer_valor * segundo_valor

# resultado = multiplicar(2,3)
# print(resultado)

# first_value = int(input("ingrese el primer valor a multiplicar: "))
# second_value = int(input("ingrese el segundo valor a multiplicar: "))
# print(f"es resultado de la multiplicacion es igual a {multiplicar(first_value,second_value)}")


# print(f"es resultado de la multiplicacion es igual a {multiplicar(int(input("ingrese el primer valor a multiplicar: ")),int(input("ingrese el segundo valor a multiplicar: ")))}")

# print(f"es resultado de la multiplicacion es igual a {int(input("ingrese el primer valor a multiplicar: ")) + int(input("ingrese el segundo valor a multiplicar: "))}")


# def respuesta():
#     return int(input("Ingrese 1 para continuar \nIngrese 0 para salir\n"))

# #quiero hacer una estructura que se repita
# continuar = 1 #positivo == 1 , negativo == 0
# while continuar:
#     print("pregunto: ")
#     continuar = respuesta()
# print("Termino el programa")

#vamos a jugar a las adivinanzas

# def adivinar():
#     return input("adivina mi nombre: ")

# mi_nombre = "mauri"
# respuesta = "nico"

# while True:
#     respuesta = adivinar()
#     if respuesta == mi_nombre:
#         print(f"felicidades el nombre es efectivamente {respuesta}")
#         break
#     else:
#         print("intenta de vuelta")

# print("ganaste")



# def es_resto_cero(numero):
   
#     #modulo 6
#     if numero%6 == 0:
#         return 6
#     #modulo 8
#     elif numero%8 == 0:
#         return 8
#     #modulo 12
#     elif numero%12 == 0:
#         return 12
#     else:
#         print("no es modulo cero con ninguno")

# numero = int(input("ingrese un numero: "))
# divisor = es_resto_cero(numero)

# if divisor != None:
#     print(f"el numero: {numero} es modulo cero con {divisor}")


def es_resto_cero(numero):
   
    #declaro un vector
    vector = []
    # para llenar el vector yo uso -> vector.append(<el numero a cargar>)
    #modulo 6
    if numero%6 == 0:
        #le supo un numero al vector
    #modulo 8
    if numero%8 == 0:
        #le supo un numero al vector
    #modulo 12
    if numero%12 == 0:
        #le supo un numero al vector
    #retorno mi vector con todos los numeros modulo cero

numero = int(input("ingrese un numero: "))
vector = es_resto_cero(numero)

if #evaluo si mi vector tiene algun valor len()
    #imprimo dicho valor
else:
    no fue divisible por ninguno