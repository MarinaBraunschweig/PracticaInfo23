# 12-Escribe un programa que solicite al usuario su fecha de nacimiento en formato
# dd/mm/aaaa y luego imprima su edad en años.
# Utiliza la función .split()

from datetime import date

fecha_nacimiento = input("Introduce tu fecha de nacimiento en formato dd/mm/aaaa: ")

dia, mes, anio = fecha_nacimiento.split("/")  # Separa la fecha en día, mes y año

hoy = date.today()  # Obtiene la fecha actual

edad = hoy.year - int(anio) - ((hoy.month, hoy.day) < (int(mes), int(dia)))  # Calcula la edad

print(f"Tienes {edad} años")
