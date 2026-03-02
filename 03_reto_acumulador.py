total_compra = 0

for producto in range(1, 6):
    precio = float(input(f"Ingrese el precio del producto {producto}: "))
    total_compra += precio

print(f"El costo total es: ${total_compra}")