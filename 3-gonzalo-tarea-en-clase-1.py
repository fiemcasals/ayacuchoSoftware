# # ejercicio lista de compras con while
lista_productos = []
lista_precios = []

print("Iniciar lista de compras")
while True:
    if len(lista_productos):
        print(f"Su lista tiene {len(lista_productos)} productos. {lista_productos}")
    
    print(f"Ingrese ok para terminar")
    producto = input(f"Ingrese el {len(lista_productos)+1}° producto: ")
    if producto == "ok":
        break
    precio = int(input(f"Ingrese el precio de {producto}: "))
    
    lista_productos.append(producto)
    lista_precios.append(precio)
    

print(f"La lista tiene {len(lista_productos)} productos.")

for i in range(0, len(lista_productos), 1):
    print(f"{i+1}° {lista_productos[i]} : ${lista_precios[i]}")





# # ejercicio lista de compras con for
# productos = []
# precios = []
# total_productos = int(input("Iniciar lista de compras. Cuantos productos Inngresara: "))
# for i in range(total_productos):
#     print(f"Su lista tiene {len(productos)} productos. {productos}")
#     producto = input(f"Ingrese el {len(productos)+1}° producto: ")
#     precio = int(input(f"Ingrese el precio de {producto}: "))

#     productos.append(producto)
#     precios.append(precio)

# print(f"La lista tiene {len(productos)} productos.")

# for i in range(0, len(productos), 1):
#     print(f"{i+1}° {productos[i]} : ${precios[i]}")





# # ejercicio lista de compras con sub-listas
# #productos = [["banana", 3500], ["manzana", 5000], ["cebolla", 1000], ["papa", 1000], ["coca", 3000]]
# productos_2 = []

# print("Iniciar lista de compras")
# while True:
#     if len(productos_2):
#         print(f"Su lista tiene {len(productos_2)} productos.")
    
#     print(f"Ingrese ok para terminar")
#     producto = input(f"Ingrese el {len(productos_2)+1}° producto: ")
#     if producto == "ok":
#         break
#     precio = int(input(f"Ingrese el precio de {producto}: "))
     
#     item = [producto, precio]
#     productos_2.append(item)
    

# print(f"La lista tiene {len(productos_2)} productos.")

# for key, value in productos_2:
#     print(f"{key}: {value}")
