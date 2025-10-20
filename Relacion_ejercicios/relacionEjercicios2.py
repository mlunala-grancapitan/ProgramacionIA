# Programa: RelacionEjercicios2.py
# Propósito: Realización de los distintos ejercicios para la iniciación en python
# Autor: Manuel Luna Alarcón
# Fecha: 16/10/2025

import random

while True:
    # Menú de opciones del programa
    print("=======RELACIÓN DE EJERCICIOS 2=======")
    print('1. Ejercicio 1')
    print('2. Ejercicio 2')
    print('3. Ejercicio 3')
    print('4. Ejercicio 4')
    print('5. Ejercicio 5')
    print('6. Ejercicio 6')
    print('7. Ejercicio 7')
    print('8. Salir')

    opcion = input('Elige una opción (1-8): ')

    # Secuencia de condicionales para ejecutar la acción correspondiente a la opción elegida
    if opcion == '1':
        numero1 = int(input('Elige un numero: '))
        numero2 = int(input('Elige otro numero: '))

        # Averiguamos los pares entre ambos números
        if numero1 < numero2:
            for i in range(numero1, numero2 + 1): # Bucle entre los dos números
                if i % 2 == 0: # Si es par, se imprime
                    print(i)
        else: # Si el segundo número es menor, realizamos el bucle al revés
            for i in range(numero2, numero1 + 1): # Bucle entre los dos números
                if i % 2 == 0: # Si es par, se imprime
                    print(i)
    elif opcion == '2':
        numeros = int(input("¿Cuántos números deseas introducir? "))

        mayores = 0
        menores = 0
        iguales = 0

        for _ in range(numeros): # Bucle para introducir los números
            num = float(input("Introduce un número: "))
            if num > 0:
                mayores += 1 # Contador de mayores que 0
            elif num < 0:
                menores += 1 # Contador de menores que 0
            else:
                iguales += 1 # Contador de iguales a 0

        print(f"Números mayores que 0: {mayores}")
        print(f"Números menores que 0: {menores}")
        print(f"Números iguales a 0: {iguales}")
    elif opcion == '3':
        numero = random.randint(1, 100)
        intentos = 10

        print("¡Bienvenido al juego de adivinar el número!")
        print("He generado un número aleatorio entre 1 y 100.")
        print("Tienes 10 intentos para adivinarlo.")

        for intento in range(1, intentos + 1): # Bucle para los intentos
            adivina = int(input(f"Intento {intento}: ¿Cuál es tu número? "))

            if adivina < numero: # Comprobamos si es mayor o menor
                print("El número es mayor.")
            elif adivina > numero: # Comprobamos si es mayor o menor
                print("El número es menor.")
            else: # Acierto
                print(f"¡Felicidades! Has acertado el número {numero} en {intento} intentos.")
                break
        else: # Si se agotan los intentos
            print(f"Lo siento, has agotado tus intentos. El número era {numero}.")

    elif opcion == '4':
        limite_inferior = int(input("Introduce el límite inferior del intervalo: "))
        limite_superior = int(input("Introduce el límite superior del intervalo: "))

        while limite_inferior >= limite_superior: # Validación de los límites
            print("Error: El límite inferior debe ser menor que el límite superior.")
            limite_inferior = int(input("Introduce el límite inferior del intervalo: "))
            limite_superior = int(input("Introduce el límite superior del intervalo: "))

        suma_dentro = 0
        fuera_intervalo = 0
        igual_limites = False

        while True: # Bucle para introducir números hasta que se introduzca 0
            numero = int(input("Introduce un número (0 para terminar): "))
            if numero == 0: # Si se introduce 0, se termina el bucle
                break
            if limite_inferior < numero < limite_superior: # Comprobamos si está dentro del intervalo
                suma_dentro += numero
            elif numero < limite_inferior or numero > limite_superior: # Comprobamos si está fuera del intervalo
                fuera_intervalo += 1
            if numero == limite_inferior or numero == limite_superior: # Comprobamos si es igual a los límites
                igual_limites = True

        print(f"Suma de los números dentro del intervalo: {suma_dentro}")
        print(f"Números fuera del intervalo: {fuera_intervalo}")

        if igual_limites: # Si se ha introducido algún número igual a los límites
            print("Se ha introducido algún número igual a los límites del intervalo.")

    elif opcion == '5':
        numero = input("Introduce un número entero mayor que 1: ")

        if not numero.isdigit() or int(numero) < 2: # Se valida que sea un entero mayor que 1
            print("Error: Debes introducir un número entero mayor que 1.")
        else: # En caso contrario, comprobamos si es primo
            numero = int(numero)
            es_primo = True
            for i in range(2, int(numero**0.5) + 1): # Comprobamos divisibilidad hasta la raíz cuadrada
                if numero % i == 0: # Si es divisible, no es primo
                    es_primo = False
                    break
            if es_primo: # Si es primo, lo indicamos
                print(f"El número {numero} es primo.")
            else: # Si no es primo, lo indicamos
                print(f"El número {numero} no es primo.")

    elif opcion == '6':
        numeros = int(input("Introduce cuántos números primos deseas ver: "))
        primos = []
        numero = 2  # El primer número primo

        while len(primos) < numeros: # Bucle hasta obtener la cantidad deseada de primos
            es_primo = True
            for i in range(2, int(numero**0.5) + 1): # Comprobamos divisibilidad hasta la raíz cuadrada
                if numero % i == 0:
                    es_primo = False
                    break
            if es_primo: # Si es primo, lo añadimos a la lista
                primos.append(numero)
            numero += 1

        print(f"Los primeros {numeros} números primos son: {primos}")

    elif opcion == '7':
        prestamo = float(input("Importe del préstamo (€): "))
        interes_anual = float(input("Tasa de interés anual (%): "))
        anios = int(input("Plazo de pago (años): "))

        # Cálculos básicos
        meses = anios * 12
        interes_mensual = interes_anual / 100 / 12

        # Fórmula de la cuota mensual (metodo francés buscado en chatGPT)
        if interes_mensual == 0:
            cuota = prestamo / meses
        else:
            cuota = prestamo * (interes_mensual * (1 + interes_mensual) ** meses) / ((1 + interes_mensual) ** meses - 1)

        print(f"\nCuota mensual: {cuota:.2f} €")

        # Generamos la tabla de amortización
        saldo = prestamo
        print("\nMes\tCuota\t\tInterés\t\tCapital\t\tSaldo")
        for mes in range(1, meses + 1): # Bucle para cada mes
            interes = saldo * interes_mensual
            capital = cuota - interes
            saldo -= capital
            if saldo < 0: # Ajuste final para evitar saldo negativo
                saldo = 0
            print(f"{mes}\t{cuota:10.2f}\t{interes:10.2f}\t{capital:10.2f}\t{saldo:10.2f}")

        print("\n¡Amortización completada!")

    elif opcion == '8':
        print("Saliendo del programa. ¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, elige una opción del 1 al 8.")
