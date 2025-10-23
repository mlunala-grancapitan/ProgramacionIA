# Programa: RelacionEjercicios4_3.py
# Propósito: Realización del tercer y cuarto ejercicio de la relación de ejercicios 4
# Autor: Manuel Luna Alarcón
# Fecha: 18/10/2025

# Función para representar un número en el sistema de palotes
def sticks_system(number_introduced):
    number_introduced = abs(int(number_introduced))
    if number_introduced == 0:
        return '-'
    sticks = []
    for character in str(number_introduced): # Recorremos cada carácter del número
        digit = int(character)
        if digit == 0: # Si el dígito es 0, representamos con un guion
            sticks.append('-')
        else: # Si no, representamos con sticks
            sticks.append(' '.join(['|'] * digit))
    return ' - '.join(sticks) # Unimos los grupos de sticks con un guion

# Función para representar un número en código Morse
def morse(number_introduced):
    traduce_morse = {
        '0': '_____',
        '1': '.____',
        '2': '..___',
        '3': '...__',
        '4': '...._',
        '5': '.....',
        '6': '_....',
        '7': '__...',
        '8': '___..',
        '9': '____.'
    }
    number_abs = abs(int(number_introduced))
    string = str(number_abs)
    return ' '.join(traduce_morse[d] for d in string)

# Programa principal
if __name__ == "__main__":
    try:
        number = int(input("Introduzca un número entero: "))
        print("Representación en palotes:")
        print("Sistema palitos: ", sticks_system(number))
        print("Morse: ", morse(number))
    except ValueError:
        print("Entrada inválida. Por favor, introduzca un número entero válido.")
    except KeyboardInterrupt:
        print("El usuario ha interrumpido la ejecución del programa.")

