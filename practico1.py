nombre = "Ramiro"
edad = 22
hobbie = "jugar al futbol"

print(f"Hola, me llamo {nombre}")

tu_nombre = (input("¿Cómo es tu nombre? "))
print(f"Un gusto {tu_nombre}")

print(f"Mi edad es {edad}")
tu_edad = int(input("¿Cuál es tu edad? "))

if tu_edad >=18:
    print (f"Puedo decir tu edad, es {tu_edad}")
else:
    print (f"No puedo decir tu edad")

print (f"Mi hobbie es {hobbie}")
tu_hobbie = input(("Y el tuyo? "))

python = (input("¿Sabés Python? si/no "))

while True:
    if python == "si":
            print(f"Sos programador Python")
            break
    if tu_edad >=18:
        print (f"Podés hacer la diplomatura")
        break


lista_lenguajes = []

for i in range(3):
    lenguajes = input(f"Diga 3 lenguajes de programación que conozca {i+1}:")
    lista_lenguajes.append(lenguajes)

    print(f"Los lenguajes que conoces son:")
    for lenguajes in lista_lenguajes:
        print(f"- {lenguajes}")

print(f"Entonces tu nombre es {tu_nombre}, tenes {tu_edad} años y conoces estos lenguajes {lista_lenguajes}")