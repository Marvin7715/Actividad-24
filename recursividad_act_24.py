def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def suma_naturales (n):
    if n == 0:
        return 0
    return n + suma_naturales(n - 1)

def fibonacci (n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

numero = int(input("Ingrese un número: "))
print(f"El factorial de {numero} es {factorial(numero)}")
print(f"El resultado de {numero} es {suma_naturales(numero)}")
print(f"El resultado de {numero} es {fibonacci(numero)}")