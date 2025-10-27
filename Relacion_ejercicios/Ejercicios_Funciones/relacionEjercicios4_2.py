# Programa: RelacionEjercicios4_2.py
# Propósito: Realización del segundo ejercicio de la relación de ejercicios 4
# Autor: Manuel Luna Alarcón
# Fecha: 18/10/2025

import math

# Esta función devuelve el número de dígitos de un número entero.
def digits(number: int) -> int:
    if number == 0:
        return 1

    number = abs(number)
    count = 0

    while number > 0:
        number //= 10
        count += 1

    return count

# Esta función invierte el orden de los dígitos de un número entero.
def reverse(number: int) -> int:
    sign = -1 if number < 0 else 1
    number = abs(number)
    reversed_number = 0

    while number > 0:
        last_digit = number % 10
        reversed_number = reversed_number * 10 + last_digit
        number //= 10

    return sign * reversed_number

# Esta función determina si un número es palindrómico.
def is_palindromic(number: int) -> bool:
    if number < 0:
        return False
    return number == reverse(number) # Devolvemos si el número es igual a su reversa

# Esta función determina si un número es primo.
def is_prime(number: int) -> bool:
    number = int(number)
    if number < 2:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False

    limit = math.isqrt(number) # Raíz cuadrada entera de number

    for divisor in range(3, limit + 1, 2): # Comprobamos solo los impares
        if number % divisor == 0:
            return False

    return True

# Esta función devuelve el siguiente número primo después del dado.
def next_prime(number: int) -> int:
    candidate = number + 1

    while not is_prime(candidate): # Buscamos el siguiente primo
        candidate += 1

    return candidate

# Esta función devuelve el dígito en la posición dada (0 es el más significativo).
def digit_n(number: int, position: int) -> int:
    number = abs(number)
    total_digits = digits(number)

    if position < 0 or position >= total_digits:
        return -1

    power = 10 ** (total_digits - position - 1)
    return (number // power) % 10 # Devolvemos el dígito en la posición dada

# Esta función devuelve la posición del primer dígito dado en el número (0 es el más significativo).
def digit_position(number: int, digit: int) -> int:
    if digit <0 or digit > 9:
        return -1

    number = abs(number)
    total_digits = digits(number)

    for position in range(total_digits):
        if digit_n(number, position) == digit:
            return position

    return -1

# Esta función elimina una cantidad de dígitos por detrás (menos significativos).
def remove_behind(number: int, count: int) -> int:
    if count < 0:
        return number

    divisor = 10 ** count
    return number // divisor

# Esta función elimina una cantidad de dígitos por delante (más significativos).
def remove_ahead(number: int, count: int) -> int:
    number = abs(number)
    total_digits = digits(number)

    if count <= 0:
        return number
    if count >= total_digits:
        return 0

    modulo = 10 ** (total_digits - count)
    return number % modulo

# Esta función pega un dígito o número por detrás (menos significativo).
def paste_behind(number: int, digit: int) -> int:
    digit_count = digits(digit)
    multiplier = 10 ** digit_count
    return number * multiplier + digit

# Esta función pega un dígito o número por delante (más significativo).
def paste_ahead(number: int, digit: int) -> int:
    number_digit_count = digits(number)
    multiplier = 10 ** number_digit_count
    return digit * multiplier + number

# Esta función extrae una porción de un número entre dos posiciones dadas.
def piece_of_number(number: int, start: int, end: int) -> int:
    number = abs(number)
    total_digits = digits(number)

    if start < 0 or end < start or end > total_digits:
        return -1

    # Eliminamos los dígitos por delante hasta llegar a start
    number = remove_ahead(number, start)

    # Eliminamos dígitos por detrás (sobrantes)
    digits_to_remove = total_digits - end - 1
    return remove_ahead(number, digits_to_remove)

# Esta función concatena dos números.
def concatenate(first: int, second: int) -> int:
    return paste_behind(first, second)

# Módulo de pruebas
def _tests():
    """Módulo de pruebas de todas las funciones."""
    print("=" * 50)
    print("PRUEBAS DE LA BIBLIOTECA NUMÉRICA")
    print("=" * 50)

    print("\n--- Funciones básicas ---")
    print(f"digits(0) = {digits(0)}")
    print(f"digits(12345) = {digits(12345)}")
    print(f"reverse(12345) = {reverse(12345)}")
    print(f"reverse(-12345) = {reverse(-12345)}")

    print("\n--- Funciones de verificación ---")
    print(f"is_palindromic(12321) = {is_palindromic(12321)}")
    print(f"is_palindromic(-12321) = {is_palindromic(-12321)}")
    print(f"is_prime(29) = {is_prime(29)}")
    print(f"is_prime(30) = {is_prime(30)}")
    print(f"next_prime(29) = {next_prime(29)}")

    print("\n--- Acceso a dígitos ---")
    print(f"digit_n(12345, 0) = {digit_n(12345, 0)}")
    print(f"digit_n(12345, 4) = {digit_n(12345, 4)}")
    print(f"digit_position(123405, 0) = {digit_position(123405, 0)}")
    print(f"digit_position(123405, 9) = {digit_position(123405, 9)}")

    print("\n--- Eliminación de dígitos ---")
    print(f"remove_behind(12345, 2) = {remove_behind(12345, 2)}")
    print(f"remove_ahead(12345, 2) = {remove_ahead(12345, 2)}")

    print("\n--- Añadir dígitos ---")
    print(f"paste_behind(123, 45) = {paste_behind(123, 45)}")
    print(f"paste_ahead(123, 45) = {paste_ahead(123, 45)}")

    print("\n--- Extracción y concatenación ---")
    print(f"piece_of_number(1234567, 2, 4) = {piece_of_number(1234567, 2, 4)}")
    print(f"concatenate(12, 345) = {concatenate(12, 345)}")

    print("\n" + "=" * 50)

# Ejecutar las pruebas si se ejecuta este módulo directamente
if __name__ == "__main__":
    _tests()

