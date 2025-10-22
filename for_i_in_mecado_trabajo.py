productos = []
precios = []

for i in range(3):
    producto = input("cual es el producto?: ")
    precio = float(input("cual es el precio?: "))

    productos.append(producto)
    precios.append(precio)

print("\nLOS MEJORES PRECIOS:")
for i in range(3):
    print(f"{productos[i]} : ${precios[i]:.2f}")