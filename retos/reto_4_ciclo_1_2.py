from functools import reduce
def ordenes(rutinaContable):
    print("------------------------ Inicio Registro diario ---------------------------------")
    registroDiario = {}
    nuevoTotal = 0.0
    incremento = 25000
    for factura in rutinaContable:
        totalFactura = 0.0
        for detalleFact in factura:
            if type(detalleFact) != int:
                cantVarUnit = tuple(filter(lambda x: type(x) != str, detalleFact))
                subtotal = reduce(lambda x, y: x * y ,cantVarUnit)
                totalFactura += subtotal
                registroDiario[str(factura[0])] = totalFactura
                
    for orden,total in registroDiario.items():
        if total < 600000:
            nuevoTotal = total + incremento
            print(f"La factura {orden} tiene un total en pesos de {nuevoTotal:,.2f}")   
        else:
            print(f"La factura {orden} tiene un total en pesos de {total:,.2f}")      
    print("-------------------------- Fin Registro diario ----------------------------------")
  



# rutinaContable = [ 
#  [1201, ("5464", 4, 25842.99), ("7854",18,23254.99), ("8521", 9, 48951.95)], 
#  [1202, ("8756", 3, 115362.58),("1112",18,2354.99)],
#  [1203, ("2547", 1, 125698.20), ("2635", 2, 135645.20), ("1254", 1, 13645.20),("9965", 5, 1645.20)],
#  [1204, ("9635", 7, 11.99), ("7733",11,18.99), ("88112", 5, 390.95)] 
# ]

# rutinaContable = [ 
# [6587, ("3268", 4, 25842.99), ("8274",18,23254.99), ("6548", 9, 48951.95), ("2547", 5, 8951.95)],
#  [6588, ("1254", 3, 115362.58), ("9744", 2, 99235.66)]
# ]

rutinaContable = [
[6589, ("9874", 1, 125698.20), ("88112", 2, 135645.20), ("3218", 4, 13645.20)],
[6590, ("5236", 8, 11.99), ("7733",11,18.99), ("88112", 5, 390.95)],
[6591, ("7812", 2, 11.99), ("9652",11,18.99)]
] 
print(ordenes(rutinaContable) )     

# ------------------------ Inicio Registro diario ---------------------------------
# La factura 1201 tiene un total en pesos de 962,529.33
# La factura 1202 tiene un total en pesos de 413,477.56
# La factura 1203 tiene un total en pesos de 443,859.80
# La factura 1204 tiene un total en pesos de 27,247.57
# -------------------------- Fin Registro diario ----------------------------------
              
# ------------------------ Inicio Registro diario ---------------------------------
# La factura 1201 tiene un total en pesos de 962,529.33
# La factura 1202 tiene un total en pesos de 413,477.56
# La factura 1203 tiene un total en pesos de 443,859.80
# La factura 1204 tiene un total en pesos de 27,247.57
# -------------------------- Fin Registro diario -----------------------------------            
    
   
    


