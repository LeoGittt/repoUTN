# Actividad 1
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
precios_frutas.update({'Naranja': 1200, 'Manzana': 1500, 'Pera': 2300})

# Actividad 2
precios_frutas.update({'Banana': 1330, 'Manzana': 1700, 'Melón': 2800})

# Actividad 3
frutas = list(precios_frutas.keys())
print("Lista de frutas:", frutas)

# Actividad 4
contactos = {}
for _ in range(5):
    nombre = input("Ingrese el nombre del contacto: ")
    numero = input("Ingrese el número telefónico: ")
    contactos[nombre] = numero
consulta = input("Ingrese el nombre para consultar el número: ")
print(f"Número asociado: {contactos.get(consulta, 'No existe el contacto')}")

# Actividad 5
frase = input("Ingrese una frase: ")
palabras = frase.split()
palabras_unicas = set(palabras)
frecuencia_palabras = {palabra: palabras.count(palabra) for palabra in palabras}
print("Palabras únicas:", palabras_unicas)
print("Frecuencia de palabras:", frecuencia_palabras)

# Actividad 6
alumnos = {}
for _ in range(3):
    nombre = input("Ingrese el nombre del alumno: ")
    notas = tuple(float(input(f"Ingrese la nota {i+1}: ")) for i in range(3))
    alumnos[nombre] = notas
for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"Promedio de {nombre}: {promedio}")

# Actividad 7
parcial1 = set(map(int, input("Ingrese los números de estudiantes que aprobaron el Parcial 1 separados por espacio: ").split()))
parcial2 = set(map(int, input("Ingrese los números de estudiantes que aprobaron el Parcial 2 separados por espacio: ").split()))
aprobaron_ambos = parcial1 & parcial2
solo_uno = (parcial1 | parcial2) - aprobaron_ambos
total_aprobados = parcial1 | parcial2
print("Aprobaron ambos parciales:", aprobaron_ambos)
print("Aprobaron solo uno de los dos:", solo_uno)
print("Total de estudiantes que aprobaron al menos un parcial:", total_aprobados)

# Actividad 8
stock_productos = {}
while True:
    accion = input("¿Desea consultar, agregar unidades o agregar un nuevo producto? (consultar/agregar/unidades/salir): ")
    if accion == "salir":
        break
    producto = input("Ingrese el nombre del producto: ")
    if accion == "consultar":
        print(f"Stock de {producto}: {stock_productos.get(producto, 'No existe el producto')}")
    elif accion == "unidades":
        if producto in stock_productos:
            unidades = int(input("Ingrese la cantidad de unidades a agregar: "))
            stock_productos[producto] += unidades
        else:
            print("El producto no existe.")
    elif accion == "agregar":
        unidades = int(input("Ingrese la cantidad inicial de unidades: "))
        stock_productos[producto] = unidades

# Actividad 9
agenda = {}
while True:
    accion = input("¿Desea consultar o agregar un evento? (consultar/agregar/salir): ")
    if accion == "salir":
        break
    dia_hora = tuple(input("Ingrese el día y hora (formato: día,hora): ").split(","))
    if accion == "consultar":
        print(f"Evento: {agenda.get(dia_hora, 'No hay eventos en ese horario')}")
    elif accion == "agregar":
        evento = input("Ingrese el evento: ")
        agenda[dia_hora] = evento

# Actividad 10
paises_capitales = {
    "Argentina": "Buenos Aires",
    "Brasil": "Brasilia",
    "Chile": "Santiago",
    "Uruguay": "Montevideo"
}
capitales_paises = {capital: pais for pais, capital in paises_capitales.items()}
print("Diccionario invertido:", capitales_paises)