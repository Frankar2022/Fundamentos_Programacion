tareas = {
        "01":{
            "descripción" : "Ir a mercar",
            "estado" : "pendiente",
            "tiempo" : 60
            },
        "02":{
            "descripción" : "Estudiar Programación",
            "estado" : "pendiente",
            "tiempo" : 180
            },
        "03":{
            "descripción" : "Hacer ejercicio",
            "estado" : "pendiente",
            "tiempo" : 50
            }      
}

#Funciones 
def adicionarTarea(tareas, identificador, nuevaTarea):
    tareas[identificador] = nuevaTarea
    return tareas

def consultarTareas(tareas):
    for identificador, tarea in tareas.items():
        print(identificador, "--",end="")#end="" elimina el salto de línea al final
        for atributo in tarea.values():
            print(atributo,"--",end="")
        print()  

def buscarIdentificador(tareas, identificador):
    #Crear un conjunto con mis identificadores -set
    conjuntoIdentificadores =  set(tareas.keys())
    if identificador in conjuntoIdentificadores:
        return True
    else:
        return False

def actualizarTarea(tareas, identificador):
    nuevaDescripcion = input("Ingrese la descripción de la nueva tarea: ")
    nuevoEstado = input("Ingrese su estado: ")
    nuevoTiempo = input("Ingrese el tiempo de ejecución: ")
    tareas[identificador]["descripción"] =  nuevaDescripcion
    tareas[identificador]["estado"] =  nuevoEstado
    tareas[identificador]["tiempo"] =  nuevoTiempo

def eliminarTarea(tareas, identificador):
    conjuntoIdentificadores = set(tareas.keys())
    if identificador in conjuntoIdentificadores:
        tareas.pop(identificador) #pop() elimina la tarea según el identificador
        print(f"La tarea con el identificador {identificador} ha sido eliminada satisfactoriamente")
    else:
        print(f"No existe una tarea con el identifacor {identificador}")           
#Fin de funciones   
    
#Paso 1. Hacer el menú de opciones
menuOpciones = True
while menuOpciones:
    print("----------Aplicación CRUD------------\n"
            "1. Adicionar Tarea   -  C\n"
            "2. Consultar Tareas  -  R\n"
            "3. Actualizar Tarea  -  U\n"
            "4. Eliminarar Tareas -  D\n"
            "5. Salir")
    opcion = input("Digite la opción: ")    
    
#Paso 2. Hacer funcional todas las opciones del menú   
    if opcion == "1":
        print("-------Adiconar Tarea------")
        #Paso 3. Adicionar Tarea
        #Inicialización de tareas
        #Recibir los datos por teclado
        identificador = input("Ingrese el identifador de la tarea: ")
        descripcion = input("Ingrese la descripción de la tarea: ")
        estado = input("Ingrese el estado de la tarea: ")
        tiempo = int(input("Ingrese el tiempo para realizar la tarea: "))
        nuevaTarea = {
            "descripción" : descripcion,
            "estado" : estado,
            "tiempo" : tiempo
        }
        #Hacer la función adicionarTarea(tareas, identificador, nuevaTarea)(Inicio...)
        adicionarTarea(tareas, identificador,nuevaTarea)
        
    elif opcion == "2":
        print("------Consultar Tareas------")
        #Paso 4. Hacer la función consultaTareas()
        #Llamar a la función consultarTareas(tareas)
        consultarTareas(tareas)
        
    elif opcion == "3":
        print("-------Actualizar Tarea------")
        #Paso 5. Hacer la función actualizarTarea()
        identificador = input("Digite el identifador de la tarea a actualizar: ")
        #Buscar si el identificador existe buscarIdentificador(tareas)
        if buscarIdentificador(tareas, identificador):
            actualizarTarea(tareas, identificador)
        else:
            print(f"El identificador {identificador} NO existe, intente de nuevo")    
    elif opcion == "4":
        print("-------Eliminar Tarea------")
        #Paso 6. Hacer la función eliminarTarea()
        identificador = input("Digite el identificador de la tarea a eliminar: ")
        eliminarTarea(tareas, identificador)
    elif opcion == "5":
        print("Ha salido correctamente del sistema")
        menuOpciones = False
    else:
        print("No ha elegido una opción válida")        