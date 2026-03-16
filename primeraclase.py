def fac(n):
    # Base Case: This prevents the function from calling itself forever
    if n == 0:
        return 1
    
    # Recursive Case: n! = n * (n-1)!
    else:
        return n * fac(n - 1)

# --- Testing the function ---
# We use an f-string to print the result clearly
number = 5
result = fac(number)

print(f"The factorial of {number} is: {result}")

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
print("cambio primera clase en visual")