# 13-Escribe un programa que solicite al usuario su nombre y su edad, y luego
# imprima un mensaje que indique cuántos años tendrá el usuario en 10 años más.

nombre=input("introduce tu nombre: ")
edad=int(input("introduce tu edad en años: "))
edadEnDiezAños= edad+10
print(f"{nombre} tu edad dentro de 10 años sera de {edadEnDiezAños}")
