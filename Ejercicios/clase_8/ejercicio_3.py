def ejercicio5():
    # No hay validación
    # Algoritmo
    mensaje = ""
    cadena = input()

    while cadena != "":
        mensaje += cadena + "\n"
        cadena = input()
        
    #salida
    return mensaje.upper()
# print(ejercicio5())
print(ejercicio5())   
    