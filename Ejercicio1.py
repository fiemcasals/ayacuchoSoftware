import random

print("📚 Bienvenido al Registro de Alumnos")

# Lista vacía para guardar alumnos
alumnos = []

# Pedimos 3 nombres como mínimo
for i in range(3):
    nombre = input(f"Ingrese el nombre del alumno {i+1}: ")
    alumnos.append(nombre)

print("\n✅ Lista inicial de alumnos:")
for i, alumno in enumerate(alumnos):
    print(f"- Posición {i}: {alumno}")

# Permitimos agregar más hasta tener 5
while len(alumnos) < 5:
    nuevo = input("Ingrese otro alumno para completar la lista: ")
    alumnos.append(nuevo)

print("\n📋 Lista final de alumnos:")
print(alumnos)

# Seleccionamos un alumno al azar
sorteado = random.choice(alumnos)
print(f"\n🎲 El alumno seleccionado al azar es: {sorteado}")
