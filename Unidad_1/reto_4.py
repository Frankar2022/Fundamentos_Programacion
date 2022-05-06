cajas_refresco = 9
latas_refresco_por_caja = 24
invitados = 56
total_latas_refresco = cajas_refresco * latas_refresco_por_caja
latas_refresco_sobrantes = total_latas_refresco % invitados
print("El número de latas de refresco sobrantes fue de:", latas_refresco_sobrantes)