
# EJERCICIO 1: ANALISIS DE UNA MATRIZ DE VENTAS

ventas = [
    [12, 15, 10, 18],
    [8, 14, 16, 12],
    [20, 18, 15, 22]
]

# 1. Mostrar la matriz completa
print("MATRIZ DE VENTAS")

for i in range(len(ventas)):
    print("Vendedor", i + 1, end=": ")
    for j in range(len(ventas[i])):
        print(ventas[i][j], end=" ")
    print()

# 2. Calcular el total de ventas por vendedor
print("\nTOTAL DE VENTAS POR VENDEDOR")

totales_vendedores = []

for i in range(len(ventas)):
    total = 0
    for j in range(len(ventas[i])):
        total += ventas[i][j]

    totales_vendedores.append(total)
    print("Vendedor", i + 1, ":", total)

# 3. Calcular el total de ventas por semana
print("\nTOTAL DE VENTAS POR SEMANA")

totales_semanas = []

for j in range(len(ventas[0])):
    total = 0
    for i in range(len(ventas)):
        total += ventas[i][j]

    totales_semanas.append(total)
    print("Semana", j + 1, ":", total)

# 4. Identificar el vendedor con mayor total de ventas
mayor_vendedor = 0

for i in range(len(totales_vendedores)):
    if totales_vendedores[i] > totales_vendedores[mayor_vendedor]:
        mayor_vendedor = i

print("\nVendedor con mayores ventas:")
print("Vendedor", mayor_vendedor + 1,
      "con", totales_vendedores[mayor_vendedor], "millones")

# 5. Identificar la semana con mayor volumen de ventas
mayor_semana = 0

for i in range(len(totales_semanas)):
    if totales_semanas[i] > totales_semanas[mayor_semana]:
        mayor_semana = i

print("\nSemana con mayores ventas:")
print("Semana", mayor_semana + 1,
      "con", totales_semanas[mayor_semana], "millones")

# 6. Calcular el promedio general
suma = 0
cantidad = 0

for fila in ventas:
    for valor in fila:
        suma += valor
        cantidad += 1

promedio = suma / cantidad

print("\nPROMEDIO GENERAL:", promedio, "millones")

# 7. Modificar las ventas de un vendedor en una semana
print("\nMODIFICAR UNA VENTA")

vendedor = int(input("Ingrese el numero del vendedor (1-3): "))
semana = int(input("Ingrese el numero de la semana (1-4): "))
nuevo_valor = float(input("Ingrese el nuevo valor de la venta: "))

if vendedor >= 1 and vendedor <= 3 and semana >= 1 and semana <= 4:
    ventas[vendedor - 1][semana - 1] = nuevo_valor

    print("\nMATRIZ ACTUALIZADA")

    for i in range(len(ventas)):
        print("Vendedor", i + 1, end=": ")
        for j in range(len(ventas[i])):
            print(ventas[i][j], end=" ")
        print()

    print("\nNUEVOS TOTALES POR VENDEDOR")

    for i in range(len(ventas)):
        total = 0
        for j in range(len(ventas[i])):
            total += ventas[i][j]
        print("Vendedor", i + 1, ":", total)

    print("\nNUEVOS TOTALES POR SEMANA")

    for j in range(len(ventas[0])):
        total = 0
        for i in range(len(ventas)):
            total += ventas[i][j]
        print("Semana", j + 1, ":", total)

    suma = 0
    cantidad = 0

    for fila in ventas:
        for valor in fila:
            suma += valor
            cantidad += 1

    print("\nNUEVO PROMEDIO GENERAL:", suma / cantidad)

else:
    print("Posicion no valida.")
