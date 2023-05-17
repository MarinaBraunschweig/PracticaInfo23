# 19-Escribe un programa que solicite al usuario un número decimal y luego
# imprima la parte entera y decimal por separado.

numeroDecimal=float(input("Introduce un numero decimal: "))

parteEntera=int(numeroDecimal)
parteDecimal=numeroDecimal-parteEntera

print(f"El numero {numeroDecimal} tiene como parte entera a {parteEntera} y su parte decimal es {parteDecimal}")