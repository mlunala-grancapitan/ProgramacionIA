# Programa que lista los 20 primeros números de Fibonacci

def calcula_fibonachi(n):
    fibonachi = [0, 1]
    while len(fibonachi) < n:
        numerillo = fibonachi[-1] + fibonachi[-2]
        fibonachi.append(numerillo)
    return fibonachi

print(*calcula_fibonachi(50), sep='\n')
# Llama a la función para obtener los primeros 20 números de Fibonacci
# y los imprime en la consola.