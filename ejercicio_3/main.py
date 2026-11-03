"""
Reservar y liberar puestos

DATOS
puestos = [[1, 0, 1], [0, 0, 1]]

IMPLEMENTA
1. reservar_puesto(puestos, coordenada): si la coordenada es valida y el puesto
   esta disponible, cambia su estado a 1 y devuelve True. En otro caso, False.
2. liberar_puesto(puestos, coordenada): si la coordenada es valida y el puesto
   esta ocupado, cambia su estado a 0 y devuelve True. En otro caso, False.
Rechaza indices negativos y coordenadas fuera del tablero.
Supone que coordenada es una tupla de dos enteros y el tablero es rectangular,
no vacio y contiene solo 0 y 1. Estas funciones SI modifican el tablero.

COMPROBACIONES CON PRINT
Realiza en orden, sobre el mismo tablero:
- Reservar (0, 1): True.
- Reservar otra vez (0, 1): False.
- Liberar (1, 2): True.
- Liberar otra vez (1, 2): False.
- Reservar (5, 0): False.
- Reservar (-1, 0): False.
Muestra el tablero final y agrega una comprobacion propia.

ANALISIS EN COMENTARIOS
Es necesario recorrer todo el tablero para reservar una coordenada conocida?
Justifica la complejidad de reservar, sin contar la impresion del tablero.

COMMIT SUGERIDO
Completa ejercicio 3: reservas y liberaciones
"""
def _coordenada_valida(puestos, coordenada):
    fila, columna = coordenada
    return 0 <= fila < len(puestos) and 0 <= columna < len(puestos[0])

def reservar_puesto(puestos, coordenada):
    if not _coordenada_valida(puestos, coordenada):
        return False
    fila, columna = coordenada
    if puestos[fila][columna] == 0:
        puestos[fila][columna] = 1
        return True
    return False
    
def liberar_puesto(puestos, coordenada):
    if not _coordenada_valida(puestos, coordenada):
        return False
    fila, columna = coordenada
    if puestos[fila][columna] == 1:
        puestos[fila][columna] = 0
        return True
    return False
    
if __name__ == "__main__":
    puestos = [[1, 0, 1], [0, 0, 1]]
 
    print(reservar_puesto(puestos, (0, 1)))   
    print(reservar_puesto(puestos, (0, 1)))   
    print(liberar_puesto(puestos, (1, 2)))    
    print(liberar_puesto(puestos, (1, 2)))    
    print(reservar_puesto(puestos, (5, 0)))   
    print(reservar_puesto(puestos, (-1, 0)))  
    print(puestos)                            
 
    # Casos propios
    print(liberar_puesto(puestos, (0, 3)))    
    print(reservar_puesto(puestos, (1, 0)))   
    print(puestos) 


# ANALISIS
# Es necesario recorrer todo el tablero para reservar una coordenada conocida?
# No. Como ya conocemos la fila y la columna, se accede directamente con
# puestos[fila][columna]. Las listas de Python permiten acceso por indice en
# tiempo constante, asi que no hace falta buscar el puesto celda por celda.
#
# Complejidad de reservar_puesto: O(1) en tiempo y en espacio extra.
# Justificacion: solo se hacen un numero fijo de operaciones, sin importar el
# tamano del tablero: desempaquetar la tupla, comparar los indices con
# len(puestos) y len(puestos[0]) (len es O(1)), leer una celda y, si esta libre,
# escribir un 1. No hay ciclos. Recorrer todo el tablero seria O(f * c), con
# f filas y c columnas, y aqui se evita por completo.
