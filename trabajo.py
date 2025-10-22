import random

def pedir_nombre(prompt):
    while True:
        nombre = input(prompt).strip()
        if nombre:
            return nombre
        print("No ingresaste nada. Intenta de nuevo.")

alumnos = [pedir_nombre(f"Ingrese el nombre del alumno {i+1}: ") for i in range(3)]

while len(alumnos) < 5:
    nuevo = pedir_nombre("Ingrese otro alumno para completar la lista: ")
    if nuevo in alumnos:
        print("Ese nombre ya está en la lista, ingresa otro.")
        continue
    alumnos.append(nuevo)

print("\n Lista final de alumnos:")
print(", ".join(alumnos))

sorteado = random.choice(alumnos)
print(f"\n El alumno seleccionado al azar es: {sorteado}")