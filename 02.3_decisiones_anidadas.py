print("--- Diagnostico de red ---")
hay_internet =input ("¿El modem tiene luces encendidas? (si/no): ")

if hay_internet == "si":
    print("Paso 1: El equipo recibe energia")
    luz_roja = input ("Alguna de las luces es color ROJO? (si/no):")
    if luz_roja == "si":
        print("Fallo detectado : Problema en la fibra optica. Llame al soporte")
    else:
        print("Todo normal : Su conexion esta operando al 100%")
else:
    print("Fallo critico : Verifique que el equipo este conectado a la corriente ")