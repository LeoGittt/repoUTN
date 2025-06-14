# Ejercicio 1: Factorial recursivo
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def mostrar_factoriales(hasta):
    for i in range(1, hasta + 1):
        print(f"Factorial de {i}: {factorial(i)}")

# Ejercicio 2: Serie de Fibonacci
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

def mostrar_fibonacci(hasta):
    for i in range(hasta + 1):
        print(f"Fibonacci en posición {i}: {fibonacci(i)}")

# Ejercicio 3: Potencia recursiva
def potencia(base, exponente):
    if exponente == 0:
        return 1
    return base * potencia(base, exponente - 1)

# Ejercicio 4: Conversión a binario
def decimal_a_binario(n):
    if n == 0:
        return ""
    return decimal_a_binario(n // 2) + str(n % 2)

# Ejercicio 5: Palíndromo
def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])

# Ejercicio 6: Suma de dígitos
def suma_digitos(n):
    if n == 0:
        return 0
    return n % 10 + suma_digitos(n // 10)

# Ejercicio 7: Pirámide de bloques
def contar_bloques(n):
    if n == 0:
        return 0
    return n + contar_bloques(n - 1)

# Ejercicio 8: Contar dígito
def contar_digito(numero, digito):
    if numero == 0:
        return 0
    return (1 if numero % 10 == digito else 0) + contar_digito(numero // 10, digito)