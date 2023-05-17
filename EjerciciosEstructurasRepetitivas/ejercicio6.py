# 6-Escribe un programa que pida al usuario una palabra y luego imprima la misma
# palabra pero con las letras en orden inverso.
'''
palabra = input("Ingresa una palabra: ")

palabra_invertida = palabra[::-1]

print("La palabra invertida es:", palabra_invertida)
'''

palabra = input("Ingrese una palabra: ")
palabra_invertida = ''.join(reversed(palabra))
print("La palabra invertida es:", palabra_invertida)


