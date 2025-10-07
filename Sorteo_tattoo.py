import random

print("🎨 Bienvenido al Sorteo de un Tatuaje 🎨")

# Lista vacía para los participantes
participantes = []

# Pedimos 3 nombres como mínimo
for i in range(3):
    nombre = input(f"Ingrese el nombre del participante {i + 1}: ")
    participantes.append(nombre)

print("\n✅ Lista inicial de participantes:")
for i, p in enumerate(participantes):
    print(f"- Posición {i}: {p}")

# Permitimos agregar más hasta tener 5
while len(participantes) < 5:
    nuevo = input("Ingrese otro participante para completar la lista: ")
    participantes.append(nuevo)

print("\n📋 Lista final de participantes:")
print(participantes)

# Sorteamos al azar
ganador = random.choice(participantes)
print(f"\n🏆 ¡El ganador del tatuaje es: {ganador}! 🎉")
