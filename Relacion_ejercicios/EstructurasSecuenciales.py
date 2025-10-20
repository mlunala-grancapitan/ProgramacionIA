#Programa: RelacionEjercicios.py
#Propósito: Realización de los distintos ejercicios para la iniciación en python
#Autor: Manuel Luna Alarcón
#Fecha: 15/10/2025

while True:
    #Menú de opciones del programa
    print("=======RELACIÓN DE EJERCICIOS 1=======")
    print('1. Ejercicio 1')
    print('2. Ejercicio 2')
    print('3. Ejercicio 3')
    print('4. Ejercicio 4')
    print('5. Ejercicio 5')
    print('6. Ejercicio 6')
    print('7. Salir')

    opcion = input('Elige una opción (1-7): ')

    #Secuencia de condicionales para ejecutar la acción correspondiente a la opción elegida
    if opcion == '1':
        nombre = input("Introduce tu nombre: ")
        print("Hola, " + nombre)
    elif opcion == '2':
        cateto1 = float(input("Introduce el valor del primer cateto: "))
        cateto2 = float(input("Introduce el valor del segundo cateto: "))

        #Cálculo de la hipotenusa a partir de los catetos introducidos
        hipotenusa = (cateto1**2 + cateto2**2)**0.5

        print("La hipotenusa es:", hipotenusa)
    elif opcion == '3':
        minutos = int(input("Introduce el tiempo en minutos: "))
        horas = minutos // 60

        #Cálculo de los minutos restantes
        minutos_restantes = minutos % 60

        print(f"{minutos} minutos son {horas} horas y {minutos_restantes} minutos.")
    elif opcion == '4':
        numerillo = int(input("Introduce un número entero: "))
        if 10 <= numerillo <= 99:
            decenas = numerillo // 10
            unidades = numerillo % 10

            #Formación del número invertido
            numero_invertido = unidades * 10 + decenas

            print("Número invertido:", numero_invertido)
        else:
            print("Error: El número debe tener dos cifras.")
    elif opcion == '5':
        horas = int(input("Introduce la hora de salida (HH): "))
        minutos = int(input("Introduce los minutos de salida (MM): "))
        segundos = int(input("Introduce los segundos de salida (SS): "))
        tiempo_viaje = int(input("Introduce el tiempo de viaje en segundos (T): "))

        #Cálculo de la hora de llegada
        total_segundos = horas * 3600 + minutos * 60 + segundos + tiempo_viaje
        hora_llegada = (total_segundos // 3600) % 24
        minuto_llegada = (total_segundos % 3600) // 60
        segundo_llegada = total_segundos % 60

        print(f"La hora de llegada es {hora_llegada:02}:{minuto_llegada:02}:{segundo_llegada:02}")
    elif opcion == '6':
        #Cálculo de la puntuación total
        respuestas_correctas = int(input("Introduce el número de respuestas correctas: "))
        respuestas_incorrectas = int(input("Introduce el número de respuestas incorrectas: "))
        respuestas_blanco = int(input("Introduce el número de respuestas en blanco: "))
        puntuacion_total = (respuestas_correctas * 5) + (respuestas_incorrectas * -1) + (respuestas_blanco * 0)

        #Cálculo de la nota normalizada entre 0 y 10
        nota_normalizada = max(0, min(10, puntuacion_total / 5))

        print(f"Puntuación total: {puntuacion_total}")
        print(f"Nota normalizada (0-10): {nota_normalizada}")
    elif opcion == '7':
        print("Saliendo...")
        break
    else:
        print("Opción inválida. Por favor, intente de nuevo.")

