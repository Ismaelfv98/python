#Guarda si una persona está matriculada (True), si tiene autorización especial (False) 
# y su edad (17). Puede acceder si está matriculada y tiene al menos 18 años, o si 
# tiene autorización especial. Calcula y muestra el resultado como True o False. 
# Cambia los valores para comprobar también un caso en el que sí pueda acceder.

matricula = True
autorizacion = False
edad = 17

acceso = True if matricula == True and edad >= 18 or autorizacion == True else False
print(f"acceso: {acceso}")