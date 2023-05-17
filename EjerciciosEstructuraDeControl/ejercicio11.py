# 11-Escribir un programa que pida al usuario dos números y muestre por pantalla
# la suma de ellos solo si ambos son pares.


num1= int(input("ingrese un numero: "))
num2= int(input("ingrese un numero: "))

suma = num1+num2

if num1 % 2 == 0 and num2 % 2 == 0:
    print(suma)
else:
    print("los numeros no son pares")