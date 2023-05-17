# 7-Escribe un programa que pida al usuario una palabra y determine si es un
# palíndromo (es decir, si se lee igual de izquierda a derecha que de derecha a
# izquierda).


palabra = input("Introduce una palabra: ")

# Invertimos la palabra usando slicing
palabra_invertida = palabra[::-1]

# Comparamos la palabra original con su versión invertida
if palabra == palabra_invertida:
    print("La palabra es un palíndromo.")
else:
    print("La palabra no es un palíndromo.")
