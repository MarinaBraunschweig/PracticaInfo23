# 6-Crea un programa que pida al usuario el radio de un círculo y calcule su área.
# La fórmula A = pi * r^2. Luego, muestra en pantalla el resultado.
# Supongamos que pi = 3.1416

radio = float(input("introduce el valor del radio: "))

areaCirculo = 3.1416*radio*radio

print(f"El area del circulo con radio {radio} es {areaCirculo}")