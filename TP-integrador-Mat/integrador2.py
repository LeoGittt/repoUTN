def obtener_digitos_unicos(numero_dni):
    """
    Convierte un número de DNI en un conjunto de sus dígitos únicos.
    Ejemplo: 34565164 -> {1, 3, 4, 5, 6}
    """
    return set(int(digito) for digito in str(numero_dni))

def contar_frecuencia_digitos(numero_dni):
    """
    Cuenta la frecuencia de aparición de cada dígito en un número de DNI.
    Retorna un diccionario donde la clave es el dígito y el valor es su frecuencia.
    Ejemplo: 34565164 -> {3: 1, 4: 2, 5: 2, 6: 1, 1: 1}
    """
    frecuencia_digitos = {}
    for digito_str in str(numero_dni):
        digito_int = int(digito_str)
        frecuencia_digitos[digito_int] = frecuencia_digitos.get(digito_int, 0) + 1
    return frecuencia_digitos

def validar_dnis_y_conjuntos(dnis, conjuntos):
    """
    Valida DNIs que contienen el dígito 0 y verifica si la unión de conjuntos tiene menos de 10 dígitos únicos.
    
    Parámetros:
    - dnis: una lista de números enteros que representan los DNIs.
    - conjuntos: una lista de conjuntos, donde cada conjunto contiene los dígitos únicos de cada DNI.
    
    Retorna:
    - tuple: (dnis_con_cero, union_incompleta)
        - dnis_con_cero: lista de DNIs que contienen el dígito 0
        - union_incompleta: booleano que indica si la unión tiene menos de 10 dígitos únicos
    """
    # 1. Verificar qué DNIs contienen el dígito '0'
    dnis_con_cero = []
    for dni in dnis:
        if '0' in str(dni):
            dnis_con_cero.append(dni)
    
    # 2. Calcular la unión de todos los conjuntos de dígitos
    union_total = set()
    for conjunto in conjuntos:
        union_total = union_total.union(conjunto)
    
    # 3. Verificar si la unión tiene menos de 10 dígitos únicos
    union_incompleta = len(union_total) < 10
    
    # 4. Imprimir mensajes informativos
    print("\n--- Validación de DNIs y Conjuntos ---")
    
    if dnis_con_cero:
        print(f"DNIs que contienen el dígito 0: {dnis_con_cero}")
    else:
        print("Ningún DNI contiene el dígito 0.")
    
    print(f"Unión de todos los conjuntos: {sorted(union_total)}")
    
    if union_incompleta:
        print(f"La unión tiene {len(union_total)} dígitos únicos (menos de 10).")
        print("Esto significa que no todos los dígitos del 0 al 9 están presentes en los DNIs del grupo.")
    else:
        print("La unión contiene todos los 10 dígitos posibles (0-9).")
    
    # 5. Retornar los resultados
    return dnis_con_cero, union_incompleta

def main():
    print("--- Conjuntos y Frecuencias ---")

    dnis_grupo = []
    num_integrantes = 4

    print("\n--- Ingreso de DNIs del Grupo ---")
    for i in range(num_integrantes):
        while True:
            try:
                dni = int(input(f"Ingrese el DNI del integrante {i + 1} (8 dígitos): "))
                if len(str(dni)) == 8:
                    dnis_grupo.append(dni)
                    break
                else:
                    print("Error: El DNI debe tener 8 dígitos. Intente de nuevo.")
            except ValueError:
                print("Error: Entrada inválida. Por favor, ingrese un número.")

    conjuntos_dnis = [obtener_digitos_unicos(dni) for dni in dnis_grupo]
    nombres_conjuntos = ['A', 'B', 'C', 'D'] # Para referenciar los conjuntos

    print("\n--- Conjuntos de Dígitos Únicos Generados ---")
    for i, conjunto in enumerate(conjuntos_dnis):
        print(f"DNI {dnis_grupo[i]} -> Conjunto {nombres_conjuntos[i]}: {conjunto}")

    print("\n--- Operaciones de Unión e Intersección entre Pares de Conjuntos ---")

    # Realizar y mostrar Unión e Intersección para todos los pares
    # Este bucle asegura que cada conjunto se compare con cada otro conjunto una sola vez.
    for i in range(len(conjuntos_dnis)):
        for j in range(i + 1, len(conjuntos_dnis)):
            conjunto1 = conjuntos_dnis[i]
            conjunto2 = conjuntos_dnis[j]
            nombre1 = nombres_conjuntos[i]
            nombre2 = nombres_conjuntos[j]

            union_result = conjunto1.union(conjunto2)
            interseccion_result = conjunto1.intersection(conjunto2)

            print(f"\nOperaciones entre Conjunto {nombre1} y Conjunto {nombre2}:")
            print(f"  Unión ({nombre1} U {nombre2}): {union_result}")
            print(f"  Intersección ({nombre1} I {nombre2}): {interseccion_result}")

    print("\n--- Conteo de Frecuencia de cada Dígito por DNI ---")
    for dni_num in dnis_grupo:
        frecuencias = contar_frecuencia_digitos(dni_num)
        print(f"\nFrecuencia de dígitos para DNI {dni_num}:")
        # Ordenar para una salida más limpia
        for digito, frecuencia in sorted(frecuencias.items()):
            print(f"  Dígito {digito}: {frecuencia} veces")

    # Validar DNIs y conjuntos
    dnis_con_cero, union_incompleta = validar_dnis_y_conjuntos(dnis_grupo, conjuntos_dnis)

    print("Fin")

main()