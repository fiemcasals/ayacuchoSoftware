#¿el vededor con más ventas?

#lista ejemmplo ["mauri","sofi","nico","nico","nico"]
ventasdiarias = [["mauri", 250], ["sofi", 300], ["nico", 1500],["nico", 300], ["nico", 100], ["sofi", 900], ["mauri", 1000]]

#buscar por nombre y sumar
mauri = ["mauri", 0]
sofi = ["sofi", 0]
nico = ["nico", 0]

#iterar ventas y sumar montos segun vendedor
def sumarVentas(item):
    for dato in item:
        if(dato[0] == "mauri"):
            mauri[1] += dato[1]
        elif(dato[0] == "sofi"):
            sofi[1] += dato[1]
        elif(dato[0] == "nico"):
            nico[1] += dato[1]

# retornar el vendedor con más ventas    
def mejorVendedor(a, b, c):
    if a[1] > b[1] and a[1] > c[1]:
        return a
    elif b[1] > a[1] and b[1] > c[1]:
        return b
    else:
        return c
    
sumarVentas(ventasdiarias)

vendedor = mejorVendedor(mauri, sofi, nico)
print(f"El mejor vendedor es {vendedor}")
