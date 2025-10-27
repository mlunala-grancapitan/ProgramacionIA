# Programa: EjerciciosArrays1.py
# Propósito: Primer ejercicio de la relación de ejercicios de arrays
# Autor: Manuel Luna Alarcón
# Fecha: 18/10/2025

import random

# Ejercicio 1
number = [random.randint(1, 100) for _ in range(100)] # Lista de 100 números aleatorios entre 1 y 100
square = [number ** 2 for number in number] # Lista de los cuadrados de los números
cube = [number ** 3 for number in number] # Lista de los cubos de los números

print(number)
print(square)
print(cube)

# Ejercicio 2
ordered_list = []

for i in range(5):
    number_introduced = int(input("Introduzca un número entre: "))
    ordered_list.append(number_introduced)

print(ordered_list)

number = ordered_list[-1]

for n in range(len(ordered_list)-1, 0, -1):
    ordered_list[n] = ordered_list[n-1]

ordered_list[0] = number

print(ordered_list)

# Ejercicio 3
filas = 4
columnas = 5
matriz = [[random.randint(100, 999) for _ in range(columnas)] for _ in range(filas)]

# Calcular sumas parciales
sumas_filas = [sum(fila) for fila in matriz]
sumas_columnas = [sum(matriz[f][c] for f in range(filas)) for c in range(columnas)]
suma_total = sum(sumas_filas)

# Mostrar resultados con formato tipo hoja de cálculo
print("\nMATRIZ CON SUMAS PARCIALES:\n")
for i in range(filas):
    for j in range(columnas):
        print(f"{matriz[i][j]:5}", end=" ")
    print(f"| {sumas_filas[i]:5}")  # Suma de la fila
print("-" * 35)

# Mostrar sumas de columnas y total final
for c in range(columnas):
    print(f"{sumas_columnas[c]:5}", end=" ")
print(f"| {suma_total:5}")