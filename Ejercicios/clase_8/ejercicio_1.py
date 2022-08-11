def suma_numeros_x_teclado():
    num = []
    suma = 0
    n = 1
    while n != 0:
        print("Ingrese los números que desa sumar. Con cero (0) realiza la suma.")
        n = int(input("Ingrese un número: "))
        num.append(n)
    # for i in range(len(num)):
    #     suma += num[i]  
    for valor in num:
        suma += valor
    print(f"La suma de los números ingresados es igual a: {suma}")
suma_numeros_x_teclado()