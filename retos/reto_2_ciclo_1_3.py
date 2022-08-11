def cliente (informacion:dict):
    if informacion["edad"] > 18:
        if informacion["primer_ingreso"] == True:
            total_boleta = 20000 * 0.95
        else: 
            total_boleta = 20000
        atraccion = "X-Treme"
        apto = True
        
    elif informacion["edad"] >= 15 and informacion["edad"] <= 18:
        if informacion["primer_ingreso"] == True:
            total_boleta = 5000 * 0.93
        else: 
            total_boleta = 5000
        atraccion = "Carros chocones"
        apto = True
            
    elif informacion["edad"] >= 7 and informacion["edad"] < 15: 
        if informacion["primer_ingreso"] == True:
            total_boleta = 10000 * 0.95
        else:
            total_boleta = 10000
        atraccion = "Sillas voladoras"
        apto = True
    else:
        total_boleta = "N/A"
        atraccion = "N/A"
        apto = False
   
    informacion = {"nombre": informacion["nombre"], "edad": informacion["edad"], "atraccion": atraccion, "apto": apto, "primer_ingreso": informacion["primer_ingreso"], "total_boleta": total_boleta}  
    return informacion

informacion = {
    'id_cliente': 1,
    'nombre': 'Johana Fernandez',
    'edad': 10,
    'primer_ingreso': True
}
print(cliente(informacion))    
 

