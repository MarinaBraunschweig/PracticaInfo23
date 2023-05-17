# 2-Escribe un programa que pida al usuario un número y calcule la suma de todos
# los números naturales del 1 hasta ese número.

numero = int(input("ingrese un numero: "))

suma=0

for x in range(1, numero+1):
    suma += x

print(f"la suma de los numeros naturales desde 1 hasta {numero} es {suma}")

#  la línea de código for i in range(1, numero+1): se puede entender como "para cada valor i en la secuencia de números enteros desde 1 hasta numero, haz lo siguiente". En cada iteración del bucle for, i se actualiza con el siguiente número de la secuencia, y el código que está indentado debajo se ejecuta una vez para cada valor de i.