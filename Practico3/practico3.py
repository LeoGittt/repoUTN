# # 1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años, deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.
edad = int(input('Ingresa tu edad '));
if edad >= 18:
    print("Es mayor de edad");
else:
    print("Es menor de edad");

# 2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6
# deberá mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el mensaje “Desaprobado”.

nota = float(input("Ingrese su nota "));
if nota >= 6:
    print("Aprobado");
else: 
    print("Desaprobado");

# 3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un número par
# imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso contrario,
# imprimir por pantalla "Por favor, ingrese un número par".
# Nota: investigar el uso del operador de módulo (%) en Python para evaluar si un número es par o impar.

numero = int(input("Ingrese un numero "));
if numero % 2 == 0:
    print("Ha ingresado un número par");
else:
    print("Por favor, ingrese un número par");

# 4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las siguientes categorías pertenece:
# ● Niño/a: menor de 12 años.
# ● Adolescente: mayor o igual que 12 años y menor que 18 años
# ● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
# ● Adulto/a: mayor o igual que 30 años.

edad = int(input("Ingrese su edad: "));
if edad <= 12:
    print("Eres un Niño");
elif edad >= 12 and edad < 18:
    print("Eres un Adolescente");
elif edad >= 18 and edad < 30:
    print("Eres un Adulto");
else:
    print("Eres un Adulto");

# 5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres (incluyendo 8 y 14). 
# Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en pantalla el mensaje "Ha ingresado una contraseña correcta";
# en caso contrario, imprimir por pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres".
# Nota: investigue el uso de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal como una lista o un string.

contraseña = input("ngrese una contraseña ");
if len(contraseña) >= 8 and len(contraseña) <= 14:
    print("Ha ingresado una contraseña correcta");
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")


# ejercicio 6

import random;
from statistics import mean,median,mode;

# creo la lista con la funcion choices
numerosAleatorios = random.choices(range(1,100),k=50);



moda = mean(numerosAleatorios);
mediana = median(numerosAleatorios);
media = mode(numerosAleatorios)

if media > mediana > moda:
    print("Hay sesgo positivo (a la derecha).")
elif media < mediana < moda:
    print("Hay sesgo negativo (a la izquierda).")
elif media == mediana == moda:
    print("No hay sesgo.")
else:
    print("No se puede determinar un sesgo claro.")


# 7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
# termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
# pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por
# pantalla.

vocales = ["a","e","i","o","u"];
frase = input("Ingrese una frase ");
letra = frase[-1]
if letra in vocales:
 print(f"{frase}" + "!");
else:
 print(frase)


# 8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3
# dependiendo de la opción que desee:
# 1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
# 2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
# 3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
# El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el
# usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(),
# lower() y title() de Python para convertir entre mayúsculas y minúsculas

nombre = input("Ingrese su nombre: ");
numero = int(input("Ingrese un numero del 1 al 3: "));
if numero == 1:
    print(nombre.upper())
elif numero == 2:
    print(nombre.lower())
else:
    print(nombre.title())

# 9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la
# magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado
# por pantalla:
# ● Menor que 3: "Muy leve" (imperceptible).
# ● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
# ● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero
# generalmente no causa daños).
# ● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras
# débiles).
# ● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
# ● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).

magnitud = int(input("Ingrese la magnitud del terremoto: "));
if magnitud <3:
    print("Muy leve,(imperceptible)");
elif magnitud >= 3 and magnitud <4:
     print("Leve (ligeramente perceptible)");
elif magnitud >= 4 and magnitud <5:
     print("Moderado (sentido por personas, pero generalmente no causa daños)");
elif magnitud >= 5 and magnitud <6:
     print("Fuerte (puede causar daños en estructuras débiles)");
elif magnitud >= 6 and magnitud <7:
     print("Muy Fuerte (puede causar daños significativos)");
elif magnitud >= 7:
     print("Extremo (puede causar graves daños a gran escala)");

# 10) Utilizando la información aportada en la siguiente tabla sobre las estaciones del año
# Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes
# del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla
# si el usuario se encuentra en otoño, invierno, primavera o verano.


hemisferio = input("¿En qué hemisferio estás? (N/S): ").strip().upper()
mes = int(input("¿En qué mes estás? (1-12): "))
dia = int(input("¿Qué día del mes es? (1-31): "))
fecha = (mes, dia)
if hemisferio == "N":
    if (fecha >= (12, 21) or fecha <= (3, 20)):
        estacion = "Invierno"
    elif (fecha >= (3, 21) and fecha <= (6, 20)):
        estacion = "Primavera"
    elif (fecha >= (6, 21) and fecha <= (9, 20)):
        estacion = "Verano"
    elif (fecha >= (9, 21) and fecha <= (12, 20)):
        estacion = "Otoño"
elif hemisferio == "S":
    if (fecha >= (12, 21) or fecha <= (3, 20)):
        estacion = "Verano"
    elif (fecha >= (3, 21) and fecha <= (6, 20)):
        estacion = "Otoño"
    elif (fecha >= (6, 21) and fecha <= (9, 20)):
        estacion = "Invierno"
    elif (fecha >= (9, 21) and fecha <= (12, 20)):
        estacion = "Primavera"
else:
    estacion = "Hemisferio no válido"
print(f"La estación en la que estás es: {estacion}")
