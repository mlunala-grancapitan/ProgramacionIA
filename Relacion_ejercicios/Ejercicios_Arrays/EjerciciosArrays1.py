# Programa: EjerciciosArrays1.py
# Propósito: Primer ejercicio de la relación de ejercicios de arrays
# Autor: Manuel Luna Alarcón
# Fecha: 18/10/2025

import random

# Ejercicio 1
try:
    number = [random.randint(1, 100) for _ in range(100)]  # Lista de 100 números aleatorios entre 1 y 100
    square = [number ** 2 for number in number]  # Lista de los cuadrados de los números
    cube = [number ** 3 for number in number]  # Lista de los cubos de los números

    print(number)
    print(square)
    print(cube)

except Exception as e:
    print(f"Ha ocurrido un error: {e}")