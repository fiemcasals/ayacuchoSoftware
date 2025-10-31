productos = []
precios = []

for i in range(3):
   producto = input("¿Cual es tu producto?:")
   precio = float(input("¿Cual es el precio?:"))

   productos.append(producto)
   precios.append(precio)

print("\n Los mejores precios:")
for i in range(3):
   print(f"{productos[i]} : ${precios[i]:.2f}:")

