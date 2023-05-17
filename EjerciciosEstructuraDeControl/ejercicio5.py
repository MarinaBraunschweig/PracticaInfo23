# Escribir un programa que pida al usuario un número entero y muestre por
# pantalla si es par o impar.

entero =  int(input("Introduce un numero entero: "))

if entero % 2 == 0:
    print(f"{entero} es par")
else:
    print(f"{entero} es impar")