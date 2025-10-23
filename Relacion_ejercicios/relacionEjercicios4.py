"""
Programa: RelacionEjercicios4.py
Propósito: Realización del primer ejercicio de la relación de ejercicios 4
Autor: Manuel Luna Alarcón
Fecha: 18/10/2025
"""

try:
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
        number1 = 0.0
        number2 = 0.0
        variables_introducidas = False
        options = [
            "Introducir variables",
            "Sumar",
            "Restar",
            "Multiplicar",
            "Dividir",
            "Terminar"
        ]

        try:
            # Bucle principal del programa
            while True:
                try:
                    # Menú de options
                    print("=======MENÚ DE OPCIONES=======")
                    for i, opcion in enumerate(options, start=1):
                        print(f"{i}. {opcion}")

                    opcion = int(input("Seleccione una opción: "))

                    if opcion == 1:
                        try:
                            number1 = float(input("Introduzca a: "))
                            number2 = float(input("Introduzca number2: "))
                            variables_introducidas = True
                        except ValueError:
                            print("Entrada inválida. Por favor, introduzca números válidos.")
                    elif opcion == 2:
                        if variables_introducidas:
                            sumar(number1, number2)
                        else:
                            print("Primero introduzca las variables (opción 1).")
                    elif opcion == 3:
                        if variables_introducidas:
                            restar(number1, number2)
                        else:
                            print("Primero introduzca las variables (opción 1).")
                    elif opcion == 4:
                        if variables_introducidas:
                            multiplicar(number1, number2)
                        else:
                            print("Primero introduzca las variables (opción 1).")
                    elif opcion == 5:
                        if variables_introducidas:
                            dividir(number1, number2)
                        else:
                            print("Primero introduzca las variables (opción 1).")
                    else:  # Terminar el programa
                        print("Fin del programa.")
                        break
                except ValueError:
                    print("Entrada inválida. Por favor, introduzca un número válido.")
        except KeyboardInterrupt:
            print("\nPrograma interrumpido por el usuario.")

    # Ejecución del programa
    if __name__ == "__main__":
        main()

except Exception as e:
    print(f"Ocurrió un error: {e}")