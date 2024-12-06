import random
#video de referencia https://www.youtube.com/watch?v=KDyd-ZceUrI
tablero = [" ", " ", " ", " ", " ", " ", " ", " ", " "]


def mostrar_tablero():
    # Función para mostrar el tablero en pantalla
    print("\n")
    print(f"{tablero[0]} | {tablero[1]} | {tablero[2]}")
    print("--+---+--")
    print(f"{tablero[3]} | {tablero[4]} | {tablero[5]}")
    print("--+---+--")
    print(f"{tablero[6]} | {tablero[7]} | {tablero[8]}")
    print("\n")

def verificar_ganador(simbolo):
    combinaciones_ganadoras = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  
        [0, 4, 8], [2, 4, 6]
    ]
    for combinacion in combinaciones_ganadoras:
        if all(tablero[pos] == simbolo for pos in combinacion):
            return True
    return False

def tablero_lleno():
    # Verificar si el tablero esta lleno (empate)
    return " " not in tablero

def movimiento_jugador():
    while True:
        try:
            # pide al jugador que elija una posición
            posicion = int(input("Turno Jugador 1 (1-9): ")) - 1
            if 0 <= posicion < 9 and tablero[posicion] == " ":
                tablero[posicion] = "X"
                break
            else:
                print("Posición inválida. Intente nuevamente.")
        except ValueError:
            print("Por favor, ingrese un número entre 1 y 9.")

def movimiento_maquina():
    print("Turno de la Máquina...")
    while True:
        posicion = random.randint(0, 8)
        if tablero[posicion] == " ":
            tablero[posicion] = "O"
            break

def main():
    print("¡Bienvenido!")
    mostrar_tablero()

    while True:
       
        movimiento_jugador()
        mostrar_tablero()
        if verificar_ganador("X"):
            print("¡Felicidades! Usted gano.")
            break
        if tablero_lleno():
            print("Es un empate.")
            break

        movimiento_maquina()
        mostrar_tablero()
        if verificar_ganador("O"):
            print("GAME OVER la Máquina gana.")
            break
        if tablero_lleno():
            print("Es un empate.")
            break

main()
