# 7-Escribir un programa que pida al usuario un carácter y muestre por pantalla si
# es una letra mayúscula, una letra minúscula, un número o un carácter especial.Ç

# Pedir al usuario que ingrese un carácter
caracter = input("Ingrese un carácter: ")

# Verificar el tipo de carácter
if caracter.isupper():
    print("El carácter es una letra mayúscula.")
elif caracter.islower():
    print("El carácter es una letra minúscula.")
elif caracter.isdigit():
    print("El carácter es un número.")
else:
    print("El carácter es un carácter especial.")   