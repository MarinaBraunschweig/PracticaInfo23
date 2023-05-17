# 10-Crea un programa que pida al usuario una cantidad en dólares y la convierta a
# euros.
# Supón que el tipo de cambio es de 0.84 euros por dólar.

cantidadDolar = float(input("Introduce una cantidad en dolares: "))

dolar_a_euro = cantidadDolar*0.84

print(f"La cantidad {cantidadDolar} dolares es equivalente a {dolar_a_euro} euros")