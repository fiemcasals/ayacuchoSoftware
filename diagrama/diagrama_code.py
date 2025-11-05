N = 0 

while True: 
    resultado = (6**N) % 13 

    if resultado ==2: 
        print("El valor de N es :", N)
        break
    N = N + 1 