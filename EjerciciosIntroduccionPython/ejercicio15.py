# Escribe un programa que solicite al usuario una temperatura en grados
# Celsius y luego imprima la temperatura equivalente en grados Fahrenheit.
# La fórmula para convertir de Celsius a Fahrenheit es: F = (C * 1.8) + 32.

temperaturaGradosCelsius=float(input("Introduce una temperatura en grados Celsius: "))
temperaturaGradosFahrenheit=(temperaturaGradosCelsius*1.8)+32

print(f"La temperatura {temperaturaGradosCelsius} ºC es igual a {temperaturaGradosFahrenheit} ºF.")