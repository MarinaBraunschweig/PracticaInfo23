# 8-Escribe un programa que pida al usuario una cadena de texto y luego imprima
# el número de palabras que contiene.

cadena = input("Ingrese una cadena de texto: ")  # Solicitar al usuario una cadena de texto
palabras = cadena.split()  # Dividir la cadena en palabras usando el espacio como delimitador
numero_palabras = len(palabras)  # Obtener el número de palabras contando los elementos de la lista

print("El número de palabras en la cadena es:", numero_palabras)  # Imprimir el resultado
