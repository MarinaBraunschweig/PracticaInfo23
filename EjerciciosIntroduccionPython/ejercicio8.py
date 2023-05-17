# 8-Crea un programa que pida al usuario el radio de un círculo y muestre su
# diámetro, su circunferencia y su área.
# Supón que pi es aproximadamente 3.14159.

PI=3.14159

radio = float(input("introduce el valor del radio: "))

diametro = 2*radio

circunferencia = 2*PI*radio

area = PI*radio**2

print(f"El circulo con radio {radio} tiene diametro {diametro}, circunferencia {circunferencia} y area {area} unidades.")
