# Desafío 1:
# Trabajas en una empresa X donde sus vendedores cobran comisiones del 6% de
# sus ventas totales y el departamento comercial te solicita que ayudes a los
# vendedores a calcular sus comisiones creando un programa que les pregunte su
# nombre y cuánto han vendido en éste mes.
# Tu programa le va a responder con una frase que incluya su nombre y el monto
# que le corresponde por las comisiones

nombre = input("Introduce tu nombre: ")

ventasTotales = float(input("Introduce las ventas totales en $ de este mes: "))

comisionesPorVentas = 0.06*ventasTotales

print(f"{nombre} tus ventas este mes han generado unas comisiones de {comisionesPorVentas}")





