N = 0 #Empezamos la busqueda desde cero

while True: 
    resultado = (6**N) % 13 #Calculamos 6 elevado a la N, modulo 13

    if resultado ==2: 
        print("El valor de N es :", N)
        break #El bucle se detiene cuando encuentra el valor de N
    N = N + 1 

