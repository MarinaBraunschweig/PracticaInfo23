# Escribir un programa que pida al usuario un número entero y muestre por
# pantalla si es múltiplo de 2 y de 3 a la vez.

entero = int(input("Introduzca un numero entero: "))

if entero % 2 == 0 and entero % 3 == 0 :
    print(f"{entero} es multiplo de 2 y 3 a la vez")
else:
    print(f"{entero} no es multiplo de 2 y 3.")