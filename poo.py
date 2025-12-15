# Programa para calcular el promedio semanal del clima
# usando Programación Orientada a Objetos
# aplicando encapsulamiento, herencia y polimorfismo


class Clima:
    def calcular_promedio(self):
        pass  # Método que será redefinido (polimorfismo)


class ClimaSemanal(Clima):
    def __init__(self):
        self.__temperaturas = []  # Encapsulamiento

    def ingresar_temperaturas(self):
        for dia in range(7):
            temp = float(input(f"Ingrese la temperatura del día {dia + 1}: "))
            self.__temperaturas.append(temp)

    # Polimorfismo: misma función, diferente implementación
    def calcular_promedio(self):
        return sum(self.__temperaturas) / len(self.__temperaturas)


# Programa principal
clima = ClimaSemanal()
clima.ingresar_temperaturas()
print("El promedio semanal del clima es:", clima.calcular_promedio())
