total_ahorrado = 0

for mes in range(1, 4):
    consignacion = int(input(f"Cuanto dinero vas a ahorrar en el mes {mes}: "))
    total_ahorrado += consignacion

print(f"Ahorro completado. Total acumulado: ${total_ahorrado}")