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

def contar_letra(palabra, letra, i=0):
    if i == len(palabra):
        return 0
    return (1 if palabra[i] == letra else 0) + contar_letra(palabra, letra, i + 1)

def invertir_cadena(cadena):
    if len(cadena) == 0:
        return ""
    return cadena[-1] + invertir_cadena(cadena[:-1])

def potencia(base, exponente):
    if exponente == 0:
        return 1
    return base * potencia(base, exponente - 1)

def menu():
    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Calcular el factorial de un número")
        print("2. Suma de números naturales")
        print("3. Calcular el n-ésimo número de Fibonacci")
        print("4. Contar cuántas veces aparece una letra en una palabra")
        print("5. Invertir una cadena de texto")
        print("6. Calcular la potencia de un número")
        print("7. Salir del programa")

        opcion = input("Seleccione una opción (1-7): ")

        match opcion:
            case "1":
                try:
                    n = int(input("Ingrese un número entero positivo: "))
                    if n < 0:
                        print("El número debe ser positivo.")
                    else:
                        print(f"El factorial de {n} es {factorial(n)}")
                except ValueError:
                    print("Entrada inválida, debe ingresar un número entero.")

            case "2":
                try:
                    n = int(input("Ingrese un número entero positivo: "))
                    if n < 0:
                        print("El número debe ser positivo.")
                    else:
                        print(f"La suma de los primeros {n} números es {suma_naturales(n)}")
                except ValueError:
                    print("Entrada inválida.")

            case "3":
                try:
                    n = int(input("Ingrese un número entero no negativo: "))
                    if n < 0:
                        print("El número debe ser no negativo.")
                    else:
                        print(f"El término {n} de Fibonacci es {fibonacci(n)}")
                except ValueError:
                    print("Entrada inválida.")

            case "4":
                palabra = input("Ingrese una palabra: ")
                letra = input("Ingrese una letra a buscar: ")
                if len(letra) != 1:
                    print("Debe ingresar una sola letra.")
                else:
                    print(f"La letra '{letra}' aparece {contar_letra(palabra, letra)} veces en '{palabra}'.")

            case "5":
                cadena = input("Ingrese una cadena de texto: ")
                print(f"La cadena invertida es: {invertir_cadena(cadena)}")

            case "6":
                try:
                    base = float(input("Ingrese la base: "))
                    exponente = int(input("Ingrese el exponente entero positivo: "))
                    if exponente < 0:
                        print("El exponente debe ser positivo.")
                    else:
                        print(f"{base}^{exponente} = {potencia(base, exponente)}")
                except ValueError:
                    print("Entrada inválida.")

            case "7":
                print("Saliendo del programa...")
                break

            case _:
                print("Opción inválida. Intente nuevamente.")

menu()