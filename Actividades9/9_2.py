#Guarda en una variable una duración total de 7384 segundos.
#Calcula cuántas horas completas, minutos restantes y segundos
#restantes contiene, usando división entera (//) y resto (%).
#Muestra los tres resultados; deben ser 2 horas, 3 minutos y
#4 segundos.
segundos = 7384
horas = segundos // 3600
segundos %= 3600
minutos = segundos // 60
segundos %= 60
print (f"7384 segundos son {horas} horas, {minutos} minutos y {segundos} segundos")
