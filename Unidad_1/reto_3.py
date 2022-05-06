vueltas_por_minuto_spinner = 147
segundos_por_minuto = 60
vueltas_por_segundo_spinner = vueltas_por_minuto_spinner / segundos_por_minuto
tiempo_a_calcular_en_segundos = 640
total_vueltas = round(vueltas_por_segundo_spinner * tiempo_a_calcular_en_segundos)
print("El Spinner da",total_vueltas,"vueltas en",tiempo_a_calcular_en_segundos,"segundos")
