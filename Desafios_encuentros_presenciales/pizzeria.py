# Costos
costo_prep = 3.0
costo_piz_peq = 8.0
costo_piz_med = 10.0
costo_piz_gra = 12.0
costo_ing_ext = 1.5

# Tamaño de la pizza
tamanio = input("Ingrese el tamaño de la pizza (P/M/G): ")

# Verificación de tamaño
if tamanio == "P":
  costo_piz = costo_piz_peq
elif tamanio == "M":
  costo_piz = costo_piz_med
elif tamanio == "G":
  costo_piz = costo_piz_gra
else:
  print("Tamaño de pizza inválido")
  exit()

# Número de ingredientes extras
num_ing_ext = int(input("Ingrese el número de ingredientes extras: "))

# Cálculo del costo total
costo_total = costo_prep + costo_piz + num_ing_ext * costo_ing_ext

# Precio de venta
precio_venta = 1.5 * costo_total

# Impresión de resultados
print(f"El costo total de la pizza es: {costo_total:.2f}")
print(f"El precio de venta de la pizza es: {precio_venta:.2f}")
