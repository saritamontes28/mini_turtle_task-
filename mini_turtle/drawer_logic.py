posicion_x = 0

def adelante(distancia):
    global posicion_x
    posicion_x += distancia
    print(f"Moviendo adelante: {distancia}. Posición: {posicion_x}")

def abajo(distancia):
    print(f"Moviendo abajo: {distancia}")

def reiniciar():
    global posicion_x
    posicion_x = 0
    print("Posición reiniciada.")
