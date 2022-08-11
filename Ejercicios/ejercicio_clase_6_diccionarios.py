def desperdicio_de_gaseosa (amigo_1:dict, amigo_2:dict, amigo_3:dict, capacidad_boton:float) -> str:
    
    amigo_1["capacidad_disponible"] = amigo_1["capacidad_vaso"] - amigo_1["capacidad_actual"]
    amigo_2["capacidad_disponible"] = amigo_2["capacidad_vaso"] - amigo_2["capacidad_actual"]
    amigo_3["capacidad_disponible"] = amigo_3["capacidad_vaso"] - amigo_3["capacidad_actual"]
    
    if amigo_1["capacidad_disponible"] < capacidad_boton:
        return amigo_1["nombre"]
               
    elif amigo_2["capacidad_disponible"] < capacidad_boton:
        return amigo_2["nombre"]
    
    elif amigo_3["capacidad_disponible"] < capacidad_boton:
        return amigo_3["nombre"]
               
    else:        
        return None
    
amigo_1 = {"nombre": "Frank", "capacidad_vaso": 200, "capacidad_actual": 100} 
amigo_2 = {"nombre": "Daniel", "capacidad_vaso": 200, "capacidad_actual": 150} 
amigo_3 = {"nombre": "Lina", "capacidad_vaso": 250, "capacidad_actual": 200}
capacidad_boton = 60

print(desperdicio_de_gaseosa(amigo_1, amigo_2, amigo_3, capacidad_boton))          
