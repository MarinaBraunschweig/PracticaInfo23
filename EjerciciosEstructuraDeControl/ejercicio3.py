# Escribir un programa que pida al usuario dos números y muestre por pantalla
# cuál de ellos es mayor.

num1=float(input("Introduce un numero: "))
num2=float(input("Introduce otro numero distinto: "))

if num1>num2:
    print(f"{num1} es mayor que {num2}")
else:
    print(f"{num2} es mayor que {num1}")