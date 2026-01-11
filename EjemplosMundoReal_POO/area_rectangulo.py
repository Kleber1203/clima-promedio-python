# Programa para calcular el área de un rectángulo
# El programa solicita los datos al usuario y muestra el resultado

# Entrada de datos
base = float(input("Ingrese la base del rectángulo: "))
altura = float(input("Ingrese la altura del rectángulo: "))

# Cálculo del área
area = base * altura

# Uso de variable booleana
es_area_positiva = area > 0

# Salida de resultados
print("El área del rectángulo es:", area)
print("¿El área es positiva?", es_area_positiva)
