def AutoPartes(ventas:list):
    registro_ventas = {}
    nombres = ("idProducto", "dProducto", "pnProducto", "cvProducto", "sProducto", "nComprador", "cComprador" , "fVenta")
        
    for i in range(len(ventas)):
        venta = dict(zip(nombres,ventas[i]))
        registro_ventas["venta_" + str(i)] = venta
    return registro_ventas

def consultaRegistro(ventas, id_producto):
    consulta = ""
    for detalle_venta in ventas.values():
        if id_producto in detalle_venta.values():
            consulta += f"Producto consultado : {detalle_venta['idProducto']}  Descripción  {detalle_venta['dProducto']}  #Parte  {detalle_venta['pnProducto']}  Cantidad vendida  {detalle_venta['cvProducto']}  Stock  {detalle_venta['sProducto']}  Comprador {detalle_venta['nComprador']}  Documento  {detalle_venta['cComprador']}  Fecha Venta  {detalle_venta['fVenta']}\n"
            
    
    if consulta == "":
        print("No hay registro de venta de ese producto")
    else:
        print (consulta)
   
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

# venta_1 = (2001,"rosca","PT29872",2,45,"Luis Molero", 3456, "12/06/2020")
# nombres = ("idProducto", "dProducto", "pnProducto", "cvProducto", "sProducto", "nComprador", "cComprador" , "fVenta")
# dict_de_2_tuplas = dict(zip(nombres,venta_1))
# print(dict_de_2_tuplas)

# Producto consultado : 2010  Descripción  bujía  #Parte  MS9512  Cantidad vendida  4  Stock  15  Comprador Carlos Rondon  Documento  1256  Fecha Venta  12/06/2020
# Producto consultado : 2010  Descripción  bujía  #Parte  ER6523  Cantidad vendida  9  Stock  36  Comprador Pedro Montes  Documento  1243  Fecha Venta  12/06/2020

# Producto consultado : 2010  Descripci�n  buj�a  #Parte  MS9512  Cantidad vendida  4  Stock  15  Comprador Carlos Rondon  Documento  1256 Fecha Venta  12/06/2020
# Producto consultado : 2010  Descripci�n  buj�a  #Parte  ER6523  Cantidad vendida  9  Stock  36  Comprador Pedro Montes  Documento  1243 Fecha Venta  12/06/2020