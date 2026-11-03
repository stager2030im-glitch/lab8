"""
Mapa de puestos

DATOS
puestos = [[1, 0, 1], [0, 0, 1]]
0: disponible. 1: ocupado. Las coordenadas son tuplas (fila, columna), desde cero.

IMPLEMENTA
1. crear_mapa(puestos): devuelve un diccionario {(fila, columna): estado}.
   Utiliza una comprension de diccionarios.
2. obtener_disponibles(puestos): devuelve un set de coordenadas disponibles.
   Utiliza una comprension de conjuntos.
No modifiques el tablero.

COMPROBACIONES CON PRINT
- Muestra el mapa completo y los disponibles.
- Consulta el estado de (1, 2) en el mapa: debe ser 1.
- Disponibles esperados: {(0, 1), (1, 0), (1, 1)}. El orden no importa.
- Agrega y comprueba otro tablero propio.

ANALISIS EN COMENTARIOS
- Cuantas celdas se revisan al obtener los disponibles en el ejemplo?
- Cuantas se revisan para f filas y c columnas? Y para n filas y n columnas?

COMMIT SUGERIDO
Completa ejercicio 1: mapa y puestos disponibles
"""

def crear_mapa(puestos):
    return {
        (fila, columna): estado
        for fila, linea in enumerate(puestos)
        for columna, estado in enumerate(linea)
    }
    

def obtener_disponibles(puestos):
    return {
        (fila, columna)
        for fila, linea in enumerate(puestos)
        for columna, estado in enumerate(linea)
        if estado == 0
    }
    

if __name__ == "__main__":
    puestos = [[1, 0, 1], [0, 0, 1]]

    mapa = crear_mapa(puestos)
    disponibles = obtener_disponibles(puestos)
    print("Mapa completo:", mapa)
    print("Disponibles:", disponibles)
    print("Estado de (1, 2):", mapa[(1, 2)])  # debe ser 1
    print("Disponibles correctos:", disponibles == {(0, 1), (1, 0), (1, 1)})
    print("Tablero sin modificar:", puestos == [[1, 0, 1], [0, 0, 1]])

    #caso propio:
    propio = [[0, 1, 0], [1, 1, 0], [0, 0, 1]]
    mapa_propio = crear_mapa(propio)
    disponibles_propio = obtener_disponibles(propio)
    print("\nMapa propio:", mapa_propio)
    print("Disponibles propios:", disponibles_propio)
    print("Estado de (2, 2):", mapa_propio[(2, 2)])  # debe ser 1
    print("Disponibles correctos:",
          disponibles_propio == {(0, 0), (0, 2), (1, 2), (2, 0), (2, 1)})

# ANALISIS
#1. En el ejemplo (2 filas x 3 columnas) se revisan 2 * 3 = 6 celdas,
#    porque hay que mirar el estado de cada una para saber si esta libre.
# 2. Para f filas y c columnas se revisan f * c celdas, es decir O(f * c).
# 3. Para n filas y n columnas se revisan n * n = n^2 celdas, es decir O(n^2).
