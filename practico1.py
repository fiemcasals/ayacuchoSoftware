

nombre = "santiago"
edad = 23
altura = 1.77

print("nombre",nombre,"mi edad es",edad,"altura",altura)

su_altura = int(input("cual es su altura "))
if su_altura > 177:
    print("sos mas alto que yo" )

else:
    print("sos mas bajo que yo")



deportista = (input("haces deportes"))

while True:

    if deportista == "si":

        print("es deportista ")

    break


numero_dni = (input("decime tu dni"))

contador = 0
for numero in numero_dni:
    if numero == "4":

        contador +=1
print("el numero 4 se repite", contador, "veces" )
