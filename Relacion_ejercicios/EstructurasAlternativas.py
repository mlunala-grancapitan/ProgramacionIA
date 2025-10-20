"""
Programa: EstructurasAlternativas.py
Propósito: Realización de los distintos ejercicios para la iniciación en python
Autor: Manuel Luna Alarcón
Fecha: 17/10/2025
"""

import math

while True:
    print("=======RELACIÓN DE EJERCICIOS 3=======")
    print('1. Ejercicio 1: Comparación de edades')
    print('2. Ejercicio 2: Clasificación de triángulos')
    print('3. Ejercicio 3: Año bisiesto')
    print('4. Ejercicio 4: Desglose de billetes y monedas')
    print('5. Ejercicio 5: Día de la semana')
    print('6. Ejercicio 6: Mayor de tres números')
    print('7. Ejercicio 7: Mayor de cinco números')
    print('8. Ejercicio 8: Calificación cualitativa')
    print('9. Salir del programa')

    opcion = input('Elige una opción (1-9): ')

    if opcion == '1':
        edad1 = int(input('Escribe una edad: '))
        edad2 = int(input('Escribe otra edad: '))

        # Comparación de edades para determinar la menor, mayor o si son iguales
        if edad1 < edad2:
            print(f'La edad menor es: {edad1}')
        elif edad2 < edad1:
            print(f'La edad menor es: {edad2}')
        else:
            print('Ambas edades son iguales.')

    elif opcion == '2':
        lado1 = float(input('Escribe la dimensión del lado 1: '))
        lado2 = float(input('Escribe la dimensión del lado 2: '))
        lado3 = float(input('Escribe la dimensión del lado 3: '))

        a, b, c = sorted((lado1, lado2, lado3)) # Ordenamos los lados

        # Comprobamos la validez del triángulo
        if a + b <= c:
            print('No es un triángulo válido.')
        else:
            # Clasificación por lados
            if math.isclose(a, b) and math.isclose(b, c):
                tipo = 'equilátero'
            elif math.isclose(a, b) or math.isclose(a, c) or math.isclose(b, c):
                tipo = 'isósceles'
            else:
                tipo = 'escaleno'

            # Comprobamos si es rectángulo (a^2 + b^2 == c^2) utilizando isclose para evitar errores de precisión (Ejemplo 0.1 + 0.2 = 0.33333334 en lugar de 0.3)
            es_rectangulo = math.isclose(a * a + b * b, c * c, rel_tol=1e-9, abs_tol=1e-9)

            print(f'El triángulo es {tipo}.')
            if es_rectangulo: # Si es triángulo rectángulo, lo indicamos
                print('Además, es triángulo rectángulo.')

    elif opcion == '3':
        #Año bisiesto
        year = int(input('Introduce un year: '))
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0): # Si es divisible entre 4 y no entre 100, o si es divisible entre 400
            print(f'El year {year} es bisiesto.')
        else:
            print(f'El year {year} no es bisiesto.')

    elif opcion == '4':
        cantidad = int(input('Introduce una cantidad en euros: '))
        billetes_monedas = [500, 200, 100, 50, 20, 10, 5, 2, 1]
        desglose = {}
        for valor in billetes_monedas: # Recorremos los billetes y monedas disponibles
            if cantidad >= valor: # Si la cantidad es mayor o igual al valor del billete/moneda
                num = cantidad // valor # Calculamos cuántos billetes/monedas de ese valor se necesitan
                desglose[valor] = num # Guardamos el número en el desglose
                cantidad -= num * valor # Restamos la cantidad correspondiente
        print('Desglose mínimo:')
        for valor, num in desglose.items(): # Imprimimos el desglose para cada billete/moneda obtenido
            print(f'{num} billetes/monedas de {valor}€')
    elif opcion == '5':
        dia = int(input('Introduce el día (1-7): '))
        dias_semana = { # Diccionario para mapear números a días de la semana
            1: 'Lunes',
            2: 'Martes',
            3: 'Miércoles',
            4: 'Jueves',
            5: 'Viernes',
            6: 'Sábado',
            7: 'Domingo'
        }
        if dia in dias_semana: # Comprobamos si el día está en el diccionario
            print(f'El día {dia} corresponde a: {dias_semana[dia]}')
        else: # Si el día no es válido, mostramos un mensaje de error
            print('Número de día inválido. Debe estar entre 1 y 7.')
    elif opcion == '6':
        numero1 = int(input('Introduce el primer número entero: '))
        numero2 = int(input('Introduce el segundo número entero: '))
        numero3 = int(input('Introduce el tercer número entero: '))

        # Comparación para encontrar el mayor de los tres números
        if numero1 <= numero2 <= numero3:
            print(f'El mayor es: {numero3}')
        elif numero1 <= numero3 <= numero2:
            print(f'El mayor es: {numero2}')
        else:
            print(f'El mayor es: {numero1}')
    elif opcion == '7':
        mayor = int(input('Introduce el número 1: '))
        for i in range(2, 6): # Bucle para los números 2 a 5
            n = int(input(f'Introduce el número {i}: '))
            if n > mayor: # Si el número es mayor que el actual mayor, lo actualizamos
                mayor = n
        print(f'El mayor es: {mayor}')
    elif opcion == '8':
        nota = float(input('Introduce la nota (0-10): '))
        if nota < 0 or nota > 10: # Comprobamos que la nota esté en el rango válido
            print('Nota fuera de rango. Debe estar entre 0 y 10.')
        else:
            if nota == 10: # Si la nota es 10, es matrícula de honor
                valor = 'Matrícula de Honor'
            elif nota >= 9: # Si la nota es mayor o igual a 9, es sobresaliente
                valor = 'Sobresaliente'
            elif nota >= 7: # Si la nota es mayor o igual a 7, es notable
                valor = 'Notable'
            elif nota >= 5: # Si la nota es mayor o igual a 5, es aprobado
                valor = 'Aprobado'
            else: # Si la nota es menor que 5, es suspenso
                valor = 'Suspenso'
            print(f'La calificación cualitativa es: {valor}')
    elif opcion == '9':
        print("Saliendo...")
        break
    else:
        print("Opción no válida. Por favor, elige una opción del 1 al 9.")
