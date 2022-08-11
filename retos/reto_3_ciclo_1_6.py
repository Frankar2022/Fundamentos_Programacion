def AutoPartes(ventas:list):
        registro = ("venta_1", "venta_2", "venta_3", "venta_4", "venta_5")
        registro_ventas = {}
        for i in range(len(ventas)):
            registro_ventas[registro[i]] = ventas[i]
        return registro_ventas

def consultaRegistro(ventas, id_producto):
    consulta_x_id_producto= ""
    for detalle_venta in ventas.values():
        if id_producto in detalle_venta:
            consulta_x_id_producto += f"Producto consultado : {detalle_venta[0]}  Descripción  {detalle_venta[1]}  #Parte  {detalle_venta[2]}  Cantidad vendida  {detalle_venta[3]}  Stock  {detalle_venta[4]}  Comprador {detalle_venta[5]}  Documento  {detalle_venta[6]}  Fecha Venta  {detalle_venta[7]}\n"
    
    
    if consulta_x_id_producto == "":
        return "No  hay  registro  de  venta  de  ese  producto"
    else:
        return consulta_x_id_producto 
   
ventas = [(2001,"rosca","PT29872",2,45,"Luis Molero", 3456, "12/06/2020"),
          (2010,"bujía","MS9512",4,15,"Carlos Rondon", 1256, "12/06/2020"),
          (2010,"bujía","ER6523",9,36,"Pedro Montes", 1243, "12/06/2020"),
          (3578,"tijera","QW8523",1,128,"Pedro Faria", 1456, "12/06/2020"),
          (9251,"piñón","EN5698",2,8,"Juan Peña", 565, "12/06/2020")
         ]          

print(consultaRegistro(AutoPartes([(2001,"rosca","PT29872",2,45,"Luis Molero", 3456, "12/06/2020"),
          (2010,"bujía","MS9512",4,15,"Carlos Rondon", 1256, "12/06/2020"),
          (2010,"bujía","ER6523",9,36,"Pedro Montes", 1243, "12/06/2020"),
          (3578,"tijera","QW8523",1,128,"Pedro Faria", 1456, "12/06/2020"),
          (9251,"piñón","EN5698",2,8,"Juan Peña", 565, "12/06/2020")
         ]), 9251))


#print(AutoPartes(ventas))

# Producto consultado : 2010  Descripción  bujía  #Parte  MS9512  Cantidad vendida  4  Stock  15  Comprador Carlos Rondon  Documento  1256  Fecha Venta  12/06/2020
# Producto consultado : 2010  Descripción  bujía  #Parte  ER6523  Cantidad vendida  9  Stock  36  Comprador Pedro Montes  Documento  1243  Fecha Venta  12/06/2020

# Producto consultado : 2010  Descripci�n  buj�a  #Parte  MS9512  Cantidad vendida  4  Stock  15  Comprador Carlos Rondon  Documento  1256  Fecha Venta  12/06/2020
# Producto consultado : 2010  Descripci�n  buj�a  #Parte  ER6523  Cantidad vendida  9  Stock  36  Comprador Pedro Montes  Documento  1243  Fecha Venta  12/06/2020