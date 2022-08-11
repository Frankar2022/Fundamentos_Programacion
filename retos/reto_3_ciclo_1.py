def autopartes(ventas:list):
    registro_ventas = {}
    for i in range(len(ventas)):
        registro_ventas[i] = str(ventas[i])    
    return registro_ventas   

def consulta_registro(ventas, id_producto):
    for i in range(len(ventas)):
        if ventas[i][0] == id_producto:
           print(f"Producto consultado : {ventas[i][0]} Descripción {ventas[i][1]} #Parte {ventas[i][2]} Cantidad vendida {ventas[i][3]} Stock {ventas[i][4]} Comprador {ventas[i][5]} Documento {ventas[i][6]} Fecha Venta {ventas[i][7]}")
        
ventas = [(2001,"rosca","PT29872",2,45,"Luis Molero", 3456, "12/06/2020"),
        (2010,"bujía","MS9512",4,15,"Carlos Rondon", 1256, "12/06/2020"),
        (2010,"bujía","ER6523",9,36,"Pedro Montes", 1243, "12/06/2020"),
        (3578,"tijera","QW8523",1,128,"Pedro Faria", 1456, "12/06/2020"),
        (9251,"piñón","EN5698",2,8,"Juan Peña", 565, "12/06/2020")
        ]     
print(consulta_registro(ventas, 9251))
#print(autopartes(ventas))

