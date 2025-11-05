vendedores = [
    {"nombre": "sofi", "venta": 330},
    {"nombre": "mauri", "venta": 460},
    {"nombre": "nico", "venta": 220}
]

mayor_venta = vendedores[0]["venta"]
vendedor_top = vendedores[0]["nombre"]

for vendedor in vendedores:
    if vendedor["venta"] > mayor_venta:
        mayor_venta = vendedor["venta"]
        vendedor_top = vendedor["nombre"]

print(f"El mejor vendedor es {vendedor_top} con ${mayor_venta}")
