depositos = 0.0
retiros = 0.0
saldo = 0.0
operacion_tipo = str(input("Ingrese el tipo de transacción a realizar (D:DEPOSITO/R:RETIRO): "))
valor = float(input("Ingrese el monto: $ "))
#validación
# if operacion_tipo != "D" or operacion_tipo != "R": 
#     print("Tipo de transacción inválido. Intente de nuevo")
# if operacion_tipo !="d" or operacion_tipo != "r":    
#    print("Tipo de transacción inválido. Intente de nuevo") 
#proceso
while valor != "":   
    if operacion_tipo == "D" or operacion_tipo == "d":
        depositos += valor
    elif operacion_tipo == "R" or operacion_tipo == "r":
        retiros += valor
    operacion_tipo = str(input("Ingrese el tipo de transacción a realizar (D:DEPOSITO/R:RETIRO): "))    
saldo = depositos - retiros
print(saldo)    
      
  
    