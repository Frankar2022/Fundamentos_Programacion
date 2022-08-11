def AutoPartes(ventas:list):
    registroVentas = {}
    for i in range(len(ventas)):
        registroVentas[i] = ventas[i]
    return registroVentas    

def consultaRegistro(ventas, idProducto):
    consultaRegistro = {}
    for detalleRegistro in ventas.values():
        if idProducto in detalleRegistro:
            consultaRegistro["idProducto"] = detalleRegistro[0]
            consultaRegistro["dProducto"] = detalleRegistro[1]
            consultaRegistro["pnProducto"] = detalleRegistro[2]
            consultaRegistro["cv_producto"] = detalleRegistro[3]
            consultaRegistro["sProducto"] = detalleRegistro[4]
            consultaRegistro["nComprador"] = detalleRegistro[5]
            consultaRegistro["cComprador"] = detalleRegistro[6]
            consultaRegistro["fVenta"] = detalleRegistro[7]
            print (f"Producto consultado : {consultaRegistro['idProducto']}  Descripción  {consultaRegistro['dProducto']}  #Parte  {consultaRegistro['pnProducto']}  Cantidad vendida  {consultaRegistro['cv_producto']}  Stock  {consultaRegistro['sProducto']}  Comprador {consultaRegistro['nComprador']}  Documento  {consultaRegistro['cComprador']}  Fecha Venta  {consultaRegistro['fVenta']}")                                               
    
    
                
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
         ]), 2010))


#print(AutoPartes(ventas))

# Producto consultado : 2010  Descripción  bujía  #Parte  MS9512  Cantidad vendida  4  Stock  15  Comprador Carlos Rondon  Documento  1256  Fecha Venta  12/06/2020
# Producto consultado : 2010  Descripción  bujía  #Parte  ER6523  Cantidad vendida  9  Stock  36  Comprador Pedro Montes  Documento  1243  Fecha Venta  12/06/2020

# Producto consultado : 2010  Descripci�n  buj�a  #Parte  MS9512  Cantidad vendida  4  Stock  15  Comprador Carlos Rondon  Documento  1256  Fecha Venta  12/06/2020
# Producto consultado : 2010  Descripci�n  buj�a  #Parte  ER6523  Cantidad vendida  9  Stock  36  Comprador Pedro Montes  Documento  1243  Fecha Venta  12/06/2020