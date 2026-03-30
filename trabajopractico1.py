# Trabajo Práctico 1 - Ejercicio 1 #
def fibonacci_r (number : int) -> int:
    if number == 0 or number == 1:
        return num 
    else:
        return fibonacci_r(number - 1) + fibonacci_r(number - 2)

def fibonacci (number : int) -> int:
    fib_1 = 0 
    fib_2 = 1
    for i in range(2, number + 1):
        fib_next = fib_1 + fib_2
        fib_1 = fib_2
        fib_2 = fib_next
    return fib_next
print(fibonacci(10))

# Trabajo Práctico 1 - Ejercicio 2 #

print ('Calculador de sumatoria')
number = int(input('Ingrese un número entero positivo: '))
if number < 0:
    print('Por favor, ingrese un número entero positivo.')
else:    sumatoria = sum(range(number + 1))
    print (f'La sumatoria de los números enteros entre 0 y {number} es: {sumatoria}')

# Trabajo Práctico 1 - Ejercicio 3 #
num1 = int(input('Ingrese el primer número entero: '))
num2 = int(input('Ingrese el segundo número entero: ')) 
resultado = producto(num1, num2)
print (f'El producto de {num1} y {num2} es: {resultado}')

# Trabajo Práctico 1 - Ejercicio 4 #
print ('hello world')
print ('Calculador de potencias')
base = int(input('Ingrese la base: '))
exponente = int(input('Ingrese el exponente: '))
resultado = base ** exponente
print (f'El resultado de {base} elevado a {exponente} es: {resultado}')

