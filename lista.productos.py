productos = []
precios = []


for i in range(5):
    productos = input("¿Cual es el producto?:")

    precios = float(input("¿Cual es el precio?:"))

    productos.append(productos)
    precios.append(precios)

    print("\n Precios: libreria:")
    for i in range(5):
     print(f"{productos[i]} : ${precios[i]:.2f}:")
