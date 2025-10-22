##lista de supermercado
lista_de_supermercado = []
lista_de_precios = []

for _ in range(4):
    producto = input("ingrese producto: ")
    precio = int(input(f"ingresar precio de {producto}: $"))
   
    lista_de_supermercado.append(producto)
    lista_de_precios.append(precio)

print("\n lista de supermercado:")
for valor in range(len(lista_de_supermercado)):
    print(f"{lista_de_supermercado[valor]} - ${lista_de_precios[valor]}")