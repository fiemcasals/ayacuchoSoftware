import random
numeros_sorteo = list(range(1, 31))

numero_usuario = random.choice(numeros_sorteo)
print(f"Tu numero para el sorteo es {numero_usuario}")

ganadores = random.sample(numeros_sorteo, 5)
print("¡los siguientes numeros son los ganadores del sorteo!")
print(ganadores)

if numero_usuario in ganadores:
    print(f"felicidades has ganado con el numero {numero_usuario}")

else:
    print("seguí participando")

