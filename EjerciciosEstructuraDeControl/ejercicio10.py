# 10-Escribir un programa que pida al usuario una letra y muestre por pantalla si es
# una vocal o una consonante.


letra = input("ingrese una letra: ")

if letra.lower() in ['a','e','i','o','u']:
    print(f"{letra} es una vocal")
else:
    print(f"{letra} es una consonante.")

