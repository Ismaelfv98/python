edad= int(input("¿Cuántos años tienes?: "))
dia= input("¿Qué día de la semana es hoy?: ")
sesion= input("¿quieres ver la sesión en 3D?: ")
precio = 8
dia = dia.lower().strip()
sesion = sesion.lower().strip()

if dia == "miercoles" or dia == "miércoles":
    precio -= 1
elif dia == "lunes" or dia == "martes" or dia == "jueves" or dia == "viernes" or dia == "sabado" or dia == "sábado" or dia == "domingo":
    print ("no hay descuento estos dias")
else:
    print("eso no es un día de la semana, te quedas sin descuento")

if sesion == "si":
    precio += 2
elif sesion == "no":
    print("se cobrará el precio de la entrada sin incremnto")
else:
    print("Por favor toma una decisión")

match edad:
    case valor if valor >= 12 and valor < 65:
        print("El precio de la entrada es: ", precio, "€")
    case valor if valor < 12 and valor > 0:
        precio -= 3
        print("El precio de la entrada es: ", precio, "€")
    case valor if valor >= 65:
        precio -= 2
        print("El precio de la entrada es: ", precio, "€")
    case _:
        print("Buen intento, la entrada para tí es de 150€ y 2 vacas por graciosito")
    