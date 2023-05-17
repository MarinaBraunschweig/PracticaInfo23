# Escribe un programa que pida al usuario un número y luego imprima la
# secuencia de Fibonacci correspondiente a ese número.

numero = int(input("Ingrese un número: "))

fibonacci_sequence = [0, 1]

while len(fibonacci_sequence) < numero:
    next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]
    fibonacci_sequence.append(next_number)

print("La secuencia de Fibonacci para el número", numero, "es:")
for num in fibonacci_sequence[:numero]:
    print(num, end=" ")

