# Crear el tablero
filas, columnas = 10, 10
tablero = [[' ' for _ in range(columnas)] for _ in range(filas)]

# Objetos en tablero
tablero[3][3] = '#'
tablero[4][3] = '#'
tablero[5][3] = '#'
tablero[0][2] = 'Q'



# Función para imprimir el tablero
def imprimir_tablero(tablero):
    print("   " + " ".join(f"{i:2} " for i in range(len(tablero[0]))))
    print("  +" + "----" * len(tablero[0]) + "+")

    # Enumera las filas verticales
    for i, fila in enumerate(tablero):
        fila_str = " | ".join(fila)
        print(f"{i:2}| {fila_str} |")
        print("  +" + "----" * len(tablero[0]) + "+")

# Mostrar el tablero
imprimir_tablero(tablero)