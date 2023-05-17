# Desafío 2:
# Escribe un programa que solicite al usuario su información personal, incluyendo
# su nombre completo, edad, estatura, peso, dirección y número de teléfono.
# A continuación, el programa deberá imprimir un mensaje con los datos
# ingresados por el usuario en el siguiente formato:
# La información ingresada es la siguiente:
# Nombre completo: [nombre completo]
# Edad: [edad]
# Estatura: [estatura] cm
# Peso: [peso] kg
# Dirección: [dirección]
# Número de teléfono: [número de teléfono]

nombreCompleto=input("introduce tu nombre completo: ")

edad=int(input("introduce tu edad en años: "))

estatura=float(input("introduce tu estatura en metros : "))

peso=float(input("introduce tu peso en kilogramos : "))

direccion=input("introduce tu direccion: ")

telefono=int(input("introduce tu numero de telefono: "))

print(f"la informacion ingresada es la siguiente:\n Nombre completo: {nombreCompleto}\n Edad: {edad} años \n Estatura: {estatura} metros \n Peso: {peso} kg \n Direccion: {direccion} \n Numero de telefono: {telefono}")