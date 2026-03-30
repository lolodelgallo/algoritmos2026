# Trabajo Práctico 1 - Ejercicio 1 #
print('Calculador de fibonacci')
def fibonacci_r (number : int) -> int:
    if number == 0 or number == 1:
        return number 
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
def producto (num1 : int, num2 : int) -> int:
    return num1 * num2
num1 = int(input('Ingrese el primer número entero: '))
num2 = int(input('Ingrese el segundo número entero: ')) 
resultado = producto(num1, num2)
print (f'El producto de {num1} y {num2} es: {resultado}')

# Trabajo Práctico 1 - Ejercicio 4 #
print ('Calculador de potencias')
base = int(input('Ingrese la base: '))
exponente = int(input('Ingrese el exponente: '))
resultado = base ** exponente
print (f'El resultado de {base} elevado a {exponente} es: {resultado}')

# Trabajo Práctico 1 - Ejercicio 5 #
def romanoadecimal(roman):
    rom_num = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    decimal_value = 0
    for i in range(len(roman)):
        if i > 0 and rom_num[roman[i]] > rom_num[roman[i - 1]]:
            decimal_value += rom_num[roman[i]] - 2 * rom_num[roman[i - 1]]
        else:
            decimal_value += rom_num[roman[i]]
    return decimal_value
rom_num = input('Ingrese un número romano: ')
resultadodecimal = romanoadecimal(rom_num)
print (f'El número romano {rom_num} convertido a decimal es: {resultadodecimal}')

# Trabajo Práctico 1 - Ejercicio 6 #
def invertir_cadena(cadena):
    return cadena[::-1]
cadena = input('Ingrese una secuencia de caracteres: ')
cadena_invertida = invertir_cadena(cadena)
print (f'La secuencia invertida es: {cadena_invertida}')



