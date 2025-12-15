# Programa para calcular el promedio semanal del clima
# usando programación tradicional (funciones)

def ingresar_temperaturas():
    temperaturas = []
    for dia in range(7):
        temp = float(input(f"Ingrese la temperatura del día {dia + 1}: "))
        temperaturas.append(temp)
    return temperaturas

def calcular_promedio(temperaturas):
    return sum(temperaturas) / len(temperaturas)

# Programa principal
temperaturas = ingresar_temperaturas()
promedio = calcular_promedio(temperaturas)

print("El promedio semanal del clima es:", promedio)
