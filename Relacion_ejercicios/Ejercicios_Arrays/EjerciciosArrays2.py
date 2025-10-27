# Programa: EjerciciosArrays2.py
# Propósito: Segundo ejercicio de la relación de ejercicios de arrays
# Autor: Manuel Luna Alarcón
# Fecha: 18/10/2025

try:
    ordered_list = []

    for i in range(5):
        number_introduced = int(input("Introduzca un número entre: "))
        ordered_list.append(number_introduced)

    print(ordered_list)

    number = ordered_list[-1]

    for n in range(len(ordered_list) - 1, 0, -1):
        ordered_list[n] = ordered_list[n - 1]

    ordered_list[0] = number

    print(ordered_list)

except ValueError:
    print("Error: Entrada no válida. Por favor, introduzca un número entero.")
except KeyboardInterrupt:
    print("\nPrograma interrumpido por el usuario.")