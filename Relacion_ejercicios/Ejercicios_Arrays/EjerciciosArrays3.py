# Programa: EjerciciosArrays3.py
# Propósito: Tercer ejercicio de la relación de ejercicios de arrays
# Autor: Manuel Luna Alarcón
# Fecha: 18/10/2025

import random

try:
    ROWS = 4
    COLUMNS = 5
    matrix = [[random.randint(100, 999) for _ in range(COLUMNS)] for _ in range(ROWS)]

    # Calcular sumas parciales
    sume_rows = [sum(fila) for fila in matrix]  # Suma de cada fila
    sume_columns = [sum(matrix[f][c] for f in range(ROWS)) for c in range(COLUMNS)]  # Suma de cada columna
    total_sume = sum(sume_rows)  # Suma total de la matrix

    # Mostrar resultados con formato tipo hoja de cálculo
    print("\nMATRIZ CON SUMAS PARCIALES:\n")
    for i in range(ROWS):
        for j in range(COLUMNS):
            print(f"{matrix[i][j]:5}", end=" ")
        print(f"| {sume_rows[i]:5}")
    print("-" * 50)

    # Mostrar sumas de COLUMNS y total final
    for c in range(COLUMNS):
        print(f"{sume_columns[c]:5}", end=" ")
    print(f"| {total_sume:5}")

except Exception as e:
    print(f"Ha ocurrido un error: {e}")