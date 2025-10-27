# Programa: EjerciciosArrays3.py
# Propósito: Tercer ejercicio de la relación de ejercicios de arrays
# Autor: Manuel Luna Alarcón
# Fecha: 18/10/2025

import random

try:
    filas = 4
    columnas = 5
    matriz = [[random.randint(100, 999) for _ in range(columnas)] for _ in range(filas)]

    # Calcular sumas parciales
    sumas_filas = [sum(fila) for fila in matriz]  # Suma de cada fila
    sumas_columnas = [sum(matriz[f][c] for f in range(filas)) for c in range(columnas)]  # Suma de cada columna
    suma_total = sum(sumas_filas)  # Suma total de la matriz

    # Mostrar resultados con formato tipo hoja de cálculo
    print("\nMATRIZ CON SUMAS PARCIALES:\n")
    for i in range(filas):
        for j in range(columnas):
            print(f"{matriz[i][j]:5}", end=" ")
        print(f"| {sumas_filas[i]:5}")  # Suma de la fila
    print("-" * 50)

    # Mostrar sumas de columnas y total final
    for c in range(columnas):
        print(f"{sumas_columnas[c]:5}", end=" ")
    print(f"| {suma_total:5}")

except Exception as e:
    print(f"Ha ocurrido un error: {e}")