# drawer_logic.py
posicion_x = 0  # Variable global

def adelante(distancia):
    global posicion_x
    posicion_x += distancia
    print(f"Avanzando {distancia}. Posición: {posicion_x}")

def abajo(distancia):
    print(f"Bajando {distancia}")

def reiniciar():
    global posicion_x
    posicion_x = 0  # Resetea a 0 usando global
    print("Posición reiniciada.")
