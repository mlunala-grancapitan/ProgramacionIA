"""
Programa: RelacionEjercicios4.py
Propósito: Realización del primer ejercicio de la relación de ejercicios 4
Autor: Manuel Luna Alarcón
Fecha: 18/10/2025
"""

# Menú de opciones del programa
def menu(opciones):
    while True:
        print("\nSeleccione una opción:")
        for i, opt in enumerate(opciones, 1):
            print(f"{i}. {opt}")
        elegido = input("Opción: ").strip()
        if elegido.isdigit(): # Comprobamos que es un número
            n = int(elegido)
            if 1 <= n <= len(opciones): # Comprobamos que está en el rango
                return n
        print("Opción incorrecta. Intente de nuevo.")

# Función para sumar dos números
def sumar(a, b):
    print(f"Resultado de la suma: {a + b}")

# Función para restar dos números
def restar(a, b):
    print(f"Resultado de la resta: {a - b}")

# Función para multiplicar dos números
def multiplicar(a, b):
    print(f"Resultado de la multiplicación: {a * b}")

# Función para dividir dos números
def dividir(a, b):
    if b == 0: # Comprobamos división por cero
        print("No se puede dividir por cero.")
    else:
        print(f"Resultado de la división: {a / b}")

# Función principal del programa
def main():
    a = 0.0
    b = 0.0
    variables_introducidas = False
    opciones = [
        "Introducir variables",
        "Sumar",
        "Restar",
        "Multiplicar",
        "Dividir",
        "Terminar"
    ]

    # Bucle principal del programa
    while True:
        opcion = menu(opciones)

        if opcion == 1:
            a = float(input("Introduzca a: "))
            b = float(input("Introduzca b: "))
            variables_introducidas = True
        elif opcion == 2:
            if variables_introducidas:
                sumar(a, b)
            else:
                print("Primero introduzca las variables (opción 1).")
        elif opcion == 3:
            if variables_introducidas:
                restar(a, b)
            else:
                print("Primero introduzca las variables (opción 1).")
        elif opcion == 4:
            if variables_introducidas:
                multiplicar(a, b)
            else:
                print("Primero introduzca las variables (opción 1).")
        elif opcion == 5:
            if variables_introducidas:
                dividir(a, b)
            else:
                print("Primero introduzca las variables (opción 1).")
        else:  # Terminar el programa
            print("Fin del programa.")
            break

# Ejecución del programa
if __name__ == "__main__":
    main()

