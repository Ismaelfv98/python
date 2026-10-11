#Un aula tiene 12 plazas disponibles. Reserva 3 plazas y después cancela 1 reserva,
#actualizando la variable con asignación aumentada. Muestra el número 
#final de plazas y, mediante una expresión condicional, muestra
#"Hay plazas" si queda alguna o "Completo" si no queda ninguna.

plazas_disponibles=12
plazas_disponibles -= 3
plazas_disponibles += 1

plazas = "Hay plazas" if plazas_disponibles >=1 else "completo"

print (plazas)