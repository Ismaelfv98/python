#Crea un programa que lea precio, unidades y porcentaje de 
#descuento, calcule subtotal, descuento, IVA y total, y muestre 
#cada importe con dos decimales. Añade una condición que indique 
#si el pedido supera un umbral de envío gratuito
precio = 6.89
unidades = 16
descuento = 50

subtotal = precio * unidades
descuento = subtotal * descuento / 100
IVA=0.21
precioIva = subtotal - (subtotal - descuento * IVA)
total = subtotal + precioIva - descuento
print(f"subtotal: {subtotal:.2f}€")
print(f"descuento: {descuento:.2f}€")
print(f"IVA: {precioIva:.2f}€")
print(f"total: {total:.2f}€")