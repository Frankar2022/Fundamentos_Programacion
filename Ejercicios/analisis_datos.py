import matplotlib.pyplot as plt
import pandas as pd

# x = ["reto_1", "reto_2", "reto_3", "reto_4", "reto_5"]
# y70 = [2.5, 3.5, 4, 1, 2]
# y30 = [3.5, 2.8, 5, 3, 4]

# plt. plot(x,y70, color="blue", linewidth=3, label="Grupo 70")
# plt. plot(x,y30, color="red", linewidth=3, label="Grupo 30")

# plt. bar(x,y70, color="blue", width=0.2, label="Grupo 70")
# plt. bar(x,y30, color="red", width=0.2, label="Grupo 30")

# plt.title = ("Tiempo promedio de realización de los retos del grupo 30 y 70")
# plt.xlabel = "Retos"
# plt.ylabel = "Tiempo"
# plt.legend()
# plt.grid()
# plt.show()

df = pd.read_csv(r"D:\\MISION TIC 2022\\Ciclo_1\\Fundamentos_de_programación\\Unidad_5\\titanic3.csv")
cantidad = df.survived.value_counts()

# print("Cantidad de muertos: ", cantidad[0])
# print("Cantidad de sobrevientes: ", cantidad[1])

x = ["Sobrevientes"]
y = [cantidad[1]]

x2 = ["Muertos"]
y2 = [cantidad[0]]


plt. bar(x,y, color="blue", width=0.2, label="Sobrevivientes")
plt. bar(x2,y2, color="red", width=0.2, label="Muertos")
plt.title = ("Sobrevivientes y muertos en el siniestro del Titanic")
plt.xlabel = "sobrevientes"
plt.ylabel = "Muertos"
plt.legend()
plt.grid()
plt.show()







