def suma(numerillo1, numerillo2):
    return numerillo1 + numerillo2

def resta(numerillo1, numerillo2):
    return numerillo1 - numerillo2

def multiplicacion(numerillo1, numerillo2):
    return numerillo1 * numerillo2

def division(numerillo1, numerillo2):
    if numerillo2 == 0:
        return "Error: Division by zero"
    return numerillo1 / numerillo2, " resto: ", numerillo1 % numerillo2

def divide_enteros(numerillo1, numerillo2):
    if numerillo2 == 0:
        return "Error: Division by zero"
    return numerillo1 // numerillo2

print("Calculadora")
print("Seleccione la operación:")
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")
print("5. Salir")

while True:
    opcion = input("Ingrese la opción (1/2/3/4/5): ")
    if opcion == "1":
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        print(f"{num1} + {num2} = {suma(num1, num2)}")
    elif opcion == "2":
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        print(f"{num1} - {num2} = {resta(num1, num2)}")
    elif opcion == "3":
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        print(f"{num1} * {num2} = {multiplicacion(num1, num2)}")
    elif opcion == "4":
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        print(f"{num1} / {num2} = {division(num1, num2)}")
        print(f"{num1} // {num2} = {divide_enteros(num1, num2)}")
    elif opcion == "5":
        print("Saliendo...")
        break
    else:
        print("Opción inválida. Por favor, intente de nuevo.")
