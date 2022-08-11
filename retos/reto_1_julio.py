ayunas = input("Se encuentra en ayunas? Responda si o no: ")
nivel_glucosa  = float(input("Digite su nivel de glucosa en sangre (mg/dl): "))

if ayunas == "si":
    if nivel_glucosa < 70:
        print("hipoglicemia")
    elif nivel_glucosa >= 70 and nivel_glucosa < 100:
        print("sin diabetes") 
    elif nivel_glucosa >= 100 and nivel_glucosa < 125:
        print("pre diabetes")
    elif nivel_glucosa >= 125:
        print("diabetes")
elif ayunas == "no":
    if nivel_glucosa < 140:
        print("sin diabetes")
    elif nivel_glucosa >= 140 and nivel_glucosa < 200:
        print("pre diabetes")
    elif nivel_glucosa  >= 200:
        print("diabetes")
else:
    print("error en los datos") 
    
                                    
