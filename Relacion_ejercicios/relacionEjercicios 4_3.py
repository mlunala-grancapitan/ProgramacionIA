# Programa: RelacionEjercicios4_3.py
# Propósito: Realización del tercer y cuarto ejercicio de la relación de ejercicios 4
# Autor: Manuel Luna Alarcón
# Fecha: 18/10/2025

# Función para representar un número en el sistema de palotes
def palotes(number):
    numero = abs(int(number))
    if numero == 0:
        return '-'
    palitos = []
    for character in str(numero): # Recorremos cada carácter del número
        digit = int(character)
        if digit == 0: # Si el dígito es 0, representamos con un guion
            palitos.append('-')
        else: # Si no, representamos con palitos
            palitos.append(' '.join(['|'] * digit))
    return ' - '.join(palitos) # Unimos los grupos de palitos con un guion

# Función para representar un número en código Morse
def morse(number):
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
    numero_abs = abs(int(number))
    cadena = str(numero_abs)
    return ' '.join(traduce_morse[d] for d in cadena)

# Programa principal
if __name__ == "__main__":
    numero = int(input("Introduzca un número entero: "))
    print("Representación en palotes:")
    print("Sistema palitos: ", palotes(numero))
    print("Morse: ", morse(numero))

