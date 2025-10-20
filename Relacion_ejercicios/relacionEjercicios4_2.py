# Programa: RelacionEjercicios4_2.py
# Propósito: Realización del segundo ejercicio de la relación de ejercicios 4
# Autor: Manuel Luna Alarcón
# Fecha: 18/10/2025

import math

# Esta función devuelve el número de dígitos de un número entero.
def digits(number: int) -> int:
    absolute_number = abs(int(number))
    if absolute_number == 0:
        return 1
    contador = 0
    while absolute_number: # Mientras queden dígitos, eliminamos el último dígito
        absolute_number //= 10
        contador += 1 # Contamos un dígito más
    return contador

# Esta función invierte el orden de los dígitos de un número entero.
def reverse(number: int) -> int:
    sign = -1 if number < 0 else 1
    absolute_number = abs(int(number))
    reversa = 0
    while absolute_number: # Mientras queden dígitos, eliminamos el último dígito y lo añadimos a la reversa
        reversa = reversa * 10 + (absolute_number % 10)
        absolute_number //= 10
    return sign * reversa

# Esta función determina si un número es palindrómico.
def is_palindromic(number: int) -> bool:
    if number < 0:
        return False
    return number == reverse(number) # Devolvemos si el número es igual a su reversa

# Esta función determina si un número es primo.
def is_prime(number: int) -> bool:
    n = int(number)
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    sqrt_limit = int(math.isqrt(n)) # Raíz cuadrada entera de n
    for i in range(3, sqrt_limit + 1, 2): # Comprobamos solo los impares
        if n % i == 0:
            return False
    return True

# Esta función devuelve el siguiente número primo después del dado.
def next_prime(number: int) -> int:
    candidato_primo = int(number) + 1
    while True: # Buscamos el siguiente primo
        if is_prime(candidato_primo): # Si es primo, lo devolvemos
            return candidato_primo
        candidato_primo += 1 # Si no, probamos con el siguiente número

# Esta función devuelve el dígito en la posición dada (0 es el más significativo).
def digit_n(number: int, position: int) -> int:
    absolute_number = abs(int(number))
    total_digitos = digits(absolute_number)
    if position < 0 or position >= total_digitos: # Si la posición es inválida, devolvemos -1
        return -1
    potencia = 10 ** (total_digitos - position - 1) # Calculamos la potencia de 10 correspondiente
    return (absolute_number // potencia) % 10

# Esta función devuelve la posición del primer dígito dado en el número (0 es el más significativo).
def digit_position(number: int, digit: int) -> int:
    absolute_number = abs(int(number))
    buscado = int(digit)
    if buscado < 0 or buscado > 9: # Si el dígito es inválido, devolvemos -1
        return -1
    total_digitos = digits(absolute_number)
    for posicion in range(total_digitos):  # Recorremos las posiciones buscando el dígito
        if digit_n(absolute_number, posicion) == buscado: # Si lo encontramos, devolvemos la posición
            return posicion
    return -1

# Esta función elimina una cantidad de dígitos por detrás (menos significativos).
def remove_behind(number: int, remove_count: int) -> int:
    num = int(number)
    remove_count = int(remove_count)
    if remove_count <= 0: # Si no hay que eliminar dígitos, devolvemos el número original
        return num
    divisor = 10 ** remove_count # Calculamos el divisor correspondiente
    return num // divisor # Devolvemos el número dividido por el divisor

# Esta función elimina una cantidad de dígitos por delante (más significativos).
def remove_ahead(number: int, remove_count: int) -> int:
    absolute_number = abs(int(number))
    remove_count = int(remove_count)
    total_digitos = digits(absolute_number)
    if remove_count <= 0: # Si no hay que eliminar dígitos, devolvemos el número original
        return absolute_number
    if remove_count >= total_digitos: # Si se eliminan todos los dígitos, devolvemos 0
        return 0
    modulo = 10 ** (total_digitos - remove_count) # Calculamos el módulo correspondiente
    return absolute_number % modulo

# Esta función pega un dígito o número por detrás (menos significativo).
def paste_behind(number: int, digit: int) -> int:
    num = int(number)
    dig = int(digit)
    digitos_dig = digits(dig)
    return num * (10 ** digitos_dig) + dig

# Esta función pega un dígito o número por delante (más significativo).
def paste_ahead(number: int, digit: int) -> int:
    num = int(number)
    dig = int(digit)
    digitos_num = digits(num)
    return dig * (10 ** digitos_num) + num

# Esta función extrae una porción de un número entre dos posiciones dadas.
def piece_of_number(number: int, start: int, end: int) -> int:
    absolute_number = abs(int(number))
    total_digitos = digits(absolute_number)
    if start < 0 or end < start or end >= total_digitos: # Si las posiciones son inválidas, devolvemos -1
        return -1
    cola = remove_ahead(absolute_number, start) # Eliminamos los dígitos por delante del inicio
    eliminar_de_cola = total_digitos - end - 1 # Calculamos cuántos dígitos eliminar por detrás
    return remove_behind(cola, eliminar_de_cola)

# Esta función concatena dos números.
def concatenate(first: int, second: int) -> int:
    return paste_behind(int(first), int(second))

# Módulo de pruebas
def _pruebas():
    print("Pruebas de la biblioteca numérica:\n")
    numero_palindromo = 12321
    print("is_palindromic(12321):", is_palindromic(numero_palindromo))
    print("reverse(12345):", reverse(12345))
    print("digits(0):", digits(12344))
    print("digits(12345):", digits(12345))
    print("is_prime(29):", is_prime(29))
    print("next_prime(29):", next_prime(29))
    print("digit_n(12345, 0):", digit_n(12345, 0))
    print("digit_n(12345, 4):", digit_n(12345, 4))
    print("digit_position(123405, 0):", digit_position(123405, 0))
    print("remove_behind(12345, 2):", remove_behind(12345, 2))
    print("remove_ahead(12345, 2):", remove_ahead(12345, 2))
    print("paste_behind(123, 45):", paste_behind(123, 45))
    print("paste_ahead(123, 45):", paste_ahead(123, 45))
    print("piece_of_number(1234567, 2, 4):", piece_of_number(1234567, 2, 4))
    print("concatenate(12, 345):", concatenate(12, 345))

# Ejecutar las pruebas si se ejecuta este módulo directamente
if __name__ == "__main__":
    _pruebas()

