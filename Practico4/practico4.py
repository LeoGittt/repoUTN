# 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
# (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

for numero in range(0,100):  
    print(numero)

# 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
# dígitos que contiene.

numero = int(input("Ingrese un número entero: "))
contador = 0

if numero == 0:
    contador = 1
else:
    numero = abs(numero)
    while numero > 0:
        numero = numero // 10
        contador += 1

print(f"El número tiene {contador} dígitos.")

# 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
# dados por el usuario, excluyendo esos dos valores.

inicio = int(input("Ingrese el primer número: "))
fin = int(input("Ingrese el segundo número: "))

suma = 0

if inicio < fin:
    for num in range(inicio + 1, fin):
        suma += num
else:
    for num in range(fin + 1, inicio):
        suma += num

print(f"La suma es: {suma}")


# 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
# secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
# un 0.

total = 0

while True:
    numero = int(input("Ingrese un número (0 para terminar): "))
    if numero == 0:
        break
    total += numero

print(f"El total acumulado es: {total}")

#  5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
# programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

numero_secreto = 4  
intentos = 0

while True:
    intento = int(input("Adivina el número (0-9): "))
    intentos += 1
    
    if intento == numero_secreto:
        print(f"¡Correcto! Acertaste en {intentos} intentos.")
        break
    elif intento < numero_secreto:
        print("El número es mayor")
    else:
        print("El número es menor")

# 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
# entre 0 y 100, en orden decreciente.

for numero in range(100, -1, -2):
    print(numero)

# 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
# número entero positivo indicado por el usuario.

n = int(input("Ingrese un número entero positivo: "))
suma = 0

for numero in range(n + 1):  
    suma += numero

print(f"La suma de los números entre 0 y {n} es: {suma}")

# 8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
# programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
# negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
# menor, pero debe estar preparado para procesar 100 números con un solo cambio).

CANTIDAD_NUMEROS = 100  

pares = 0
impares = 0
positivos = 0
negativos = 0

for i in range(CANTIDAD_NUMEROS):
    numero = int(input(f"Ingrese el número {i + 1}/{CANTIDAD_NUMEROS}: "))
    
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1
    
    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1

print("\nResultados:")
print(f"Pares: {pares}")
print(f"Impares: {impares}")
print(f"Positivos: {positivos}")
print(f"Negativos: {negativos}")

# 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
# media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
# poder procesar 100 números cambiando solo un valor).

cantidad_numeros = 100
suma_total = 0
contador = 0

while contador < cantidad_numeros:
    numero = int(input(f"Ingrese el número {contador + 1}/{cantidad_numeros}: "))
    suma_total += numero
    contador += 1

media = suma_total / cantidad_numeros
print(f"\nLa media de los {cantidad_numeros} números es: {media}")

# 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
# usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

numero = int(input("Ingrese un número entero: "))
invertido = 0

while numero > 0:
    digito = numero % 10
    invertido = (invertido * 10) + digito
    numero = numero // 10

print("El número invertido es:", invertido)