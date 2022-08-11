class empleado:
    
    def __init__(empleado):
        empleado.nombre=input("Digite el nombre: ")
        empleado.sueldo=float(input("Digite el sueldo: "))
        
    def imprimir(empleado):
      print("****************************")  
      print("Nombre y apellidos: ", empleado.nombre)
      print("Sueldo: ", empleado.sueldo)
      print("****************************") 
      
    def pagar_impuesto(empleado):
        if empleado.sueldo > 3000:
            print(f"El empleado {empleado.nombre} debe pagar impuestos")
        else:
            print(f"El empleado {empleado.nombre} NO debe pagar impuestos")    