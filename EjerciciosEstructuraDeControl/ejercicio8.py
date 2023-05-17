# 9-Escribir un programa que pida al usuario tres números y muestre por pantalla
# el mayor de ellos.

numero1 = float(input("ingrese un numero: "))
numero2 = float(input("ingrese un numero: "))
numero3 = float(input("ingrese un numero: "))

if numero1 > numero2 and numero1> numero3:
    print(f"{numero1} es el mayor de todos")
elif numero2 > numero1 and numero2 > numero3:
    print(f"{numero2} es el mayor de todos")
else:
    print(f"{numero3} es mayor.")



       
