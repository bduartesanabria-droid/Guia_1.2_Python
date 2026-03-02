concesionario = []

for i in range(3):
    marca = input("Ingrese la marca del carro: ")
    modelo = input("Ingrese el modelo del carro: ")
    precio = input("Ingrese el precio del carro: ")

    carro = {
        "marca": marca,
        "modelo": modelo,
        "precio": precio
    }

    concesionario.append(carro)

for vehiculo in concesionario:
    print(f"Vehiculo registrado: Marca {vehiculo['marca']}, Modelo {vehiculo['modelo']}, Precio ${vehiculo['precio']}")