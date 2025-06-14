# Actividad 1: Función imprimir_hola_mundo
def imprimir_hola_mundo():
    print("Hola Mundo!")

# Actividad 2: Función saludar_usuario
def saludar_usuario(nombre):
    return f"Hola {nombre}!"

# Actividad 3: Función informacion_personal
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

# Actividad 4: Funciones para cálculos de círculo
def calcular_area_circulo(radio):
    import math
    return math.pi * radio ** 2

def calcular_perimetro_circulo(radio):
    import math
    return 2 * math.pi * radio

# Actividad 5: Función segundos_a_horas
def segundos_a_horas(segundos):
    return segundos / 3600

# Actividad 6: Función tabla_multiplicar
def tabla_multiplicar(numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

# Actividad 7: Función operaciones_basicas
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b if b != 0 else "División por cero no permitida"
    return suma, resta, multiplicacion, division

# Actividad 8: Función calcular_imc
def calcular_imc(peso, altura):
    return round(peso / (altura ** 2), 2)

# Actividad 9: Función celsius_a_fahrenheit
def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Actividad 10: Función calcular_promedio
def calcular_promedio(a, b, c):
    return (a + b + c) / 3

# Programa principal
if __name__ == "__main__":
    # Actividad 1
    imprimir_hola_mundo()

    # Actividad 2
    nombre = input("Ingrese su nombre: ")
    print(saludar_usuario(nombre))

    # Actividad 3
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    edad = input("Ingrese su edad: ")
    residencia = input("Ingrese su lugar de residencia: ")
    informacion_personal(nombre, apellido, edad, residencia)

    # Actividad 4
    radio = float(input("Ingrese el radio del círculo: "))
    print(f"Área: {calcular_area_circulo(radio)}")
    print(f"Perímetro: {calcular_perimetro_circulo(radio)}")

    # Actividad 5
    segundos = int(input("Ingrese la cantidad de segundos: "))
    print(f"Horas: {segundos_a_horas(segundos)}")

    # Actividad 6
    numero = int(input("Ingrese un número para la tabla de multiplicar: "))
    tabla_multiplicar(numero)

    # Actividad 7
    a = float(input("Ingrese el primer número: "))
    b = float(input("Ingrese el segundo número: "))
    resultados = operaciones_basicas(a, b)
    print(f"Suma: {resultados[0]}, Resta: {resultados[1]}, Multiplicación: {resultados[2]}, División: {resultados[3]}")

    # Actividad 8
    peso = float(input("Ingrese su peso en kilogramos: "))
    altura = float(input("Ingrese su altura en metros: "))
    print(f"IMC: {calcular_imc(peso, altura)}")

    # Actividad 9
    celsius = float(input("Ingrese la temperatura en Celsius: "))
    print(f"Fahrenheit: {celsius_a_fahrenheit(celsius)}")

    # Actividad 10
    a = float(input("Ingrese el primer número: "))
    b = float(input("Ingrese el segundo número: "))
    c = float(input("Ingrese el tercer número: "))
    print(f"Promedio: {calcular_promedio(a, b, c)}")