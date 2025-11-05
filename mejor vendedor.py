ventas = [561, 222, 434]
nombres = ['Mauri', 'Sofi', 'Nico']

mejor_ventas = ventas[0]
mejor_vendedor = nombres[0]

for i in range(len(ventas)):
    if ventas[i] > mejor_ventas:
        mejor_ventas = ventas[i]
        mejor_vendedor = ventas[i]

print(f"El mejor vendedor es {mejor_vendedor} con {mejor_ventas} ventas.")