# Programa: EjerciciosArrays2.py
# Propósito: Segundo ejercicio de la relación de ejercicios de arrays
# Autor: Manuel Luna Alarcón
# Fecha: 18/10/2025

try:
    ordered_list = []

    # Escribimos 5 números en la lista
    for i in range(5):
        number_introduced = int(input(f"Introduzca un número ({i + 1}/5): "))
        ordered_list.append(number_introduced)

    print(ordered_list)
    number = ordered_list[-1] # Rotamos la lista una posición a la derecha

    # Desplazamos los elementos una posición a la derecha
    for n in range(len(ordered_list) - 1, 0, -1):
        ordered_list[n] = ordered_list[n - 1] # Asignamos el valor del elemento anterior

    ordered_list[0] = number # Colocamos el último número en la primera posición
    print(ordered_list)

except ValueError:
    print("Error: Entrada no válida. Por favor, introduzca un número entero.")
except KeyboardInterrupt:
    print("\nPrograma interrumpido por el usuario.")