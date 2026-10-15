import random

operacion = input("Que operación quieres realizar: ingresar, retirar, abrir, cerrar o consultar ")
operacion_limpia = operacion.lower().strip()
titular = "ismael"
saldo = random.randint(0,1000)
estado = True

match operacion_limpia:
    case "ingresar":
        cantidad = int(input("dinero a ingresar: "))
        if cantidad > 0:
            saldo += cantidad
            print("tu saldo es ", saldo)
        else:
            print ("cantidad no valida")
    case "retirar":
        cantidad = int(input("dinero a retirar: "))
        if cantidad > 0:
            saldo -= cantidad
            print("tu saldo es ", saldo)
        else:
            print ("cantidad no valida")
    case "abrir":
        if not estado:
            estado = True
            print ("activación correcta")
        else:
            print("La cuenta ya está activa")
    case "cerrar":
        if estado and saldo == 0:
            estado = False
            print ("cierre correcto")
        else:
            print("La cuenta ya está cerrada")
    case "consultar":
        print(titular, "tu saldo es: ", saldo)
    case _:
        print("operacion no válida")        