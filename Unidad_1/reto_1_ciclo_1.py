#usuario = str(input("Ingrese el código de usuario:"))
#apital_inicial = int(input("Ingrese el valor a invertir en el CDT:"))
#tiempo = int(input("Ingrese el tiempo(meses) del CDT:"))

def CDT(usuario, capital_inicial, tiempo):
    """CDT
    Parámetros:
        usuario(str): Identifica al cliente del banco
        capital_inicial(int): Monto inicial invertido en el CDT
        tiempo(int): En meses del CDT 
    Retorna:
        Las ganancias o perdidas generadas en un periodo de tiempo por el CDT
    """
    
    if tiempo > 2 :
        porcentaje_intereses = 0.03
        valor_intereses = (capital_inicial * porcentaje_intereses * tiempo)/12
        capital_final = capital_inicial + valor_intereses
        
    else :
        porcentaje_a_perder = 0.02
        valor_a_perder = capital_inicial * porcentaje_a_perder
        capital_final = capital_inicial - valor_a_perder
        
    return "Para el usuario {} La cantidad de dinero a recibir, según el monto inicial {} para un tiempo de {} meses es: {}".format(usuario,capital_inicial,tiempo,capital_final)   
    
print(CDT("AB1012", 1000000, 3)) 