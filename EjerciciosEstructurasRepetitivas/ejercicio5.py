# 5-Escribe un programa que imprima la suma de todos los números pares del 1 al
# 100.

'''
PRIMERA FORMA
suma=0

for i in range(1, 101):
    if i % 2 == 0:
        suma += i

print(f"la suma de todos los numeros pares del 1 al 100 es {suma}")
'''

# OTRA FORMA
suma = 0

for i in range(2, 101, 2):
    suma += i

print("La suma de todos los números pares del 1 al 100 es:", suma)