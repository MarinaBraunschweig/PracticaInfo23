# Escribir un programa que pida al usuario un número entero y muestre por
# pantalla si es positivo, negativo o cero.

entero=int(input("Introduce un número entero: "))

if entero>0:
    print(f"{entero} es un numero positivo")
elif entero<0:
    print(f"{entero} es un numero negativo")
else:
    print(f"{entero} es cero.")