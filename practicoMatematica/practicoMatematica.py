# Integrantes: 
# Giuliana Heredia 
# Federico Iacono
# Inga Gonzalo
# Leonel Gonzalez
# Simulador básico de puertas lógicas

print("🧠 Simulador de Puertas Lógicas")

# Pedimos al usuario que ingrese dos valores binarios
a = int(input("Primer valor binario (0 o 1): "))
b = int(input("Segundo valor binario (0 o 1): "))

# Validamos que los valores sean 0 o 1
if (a not in [0, 1]) or (b not in [0, 1]):
    print("Error: Debes ingresar solo 0 o 1.")
else:
    print("AND:", a and b)
    print("OR:", a or b)
    print("NOT A:", 1 - a)
    print("NOT B:", 1 - b)
    print("NAND:", 1 - (a and b))
    print("NOR:", 1 - (a or b))
    print("XOR:", a ^ b)
