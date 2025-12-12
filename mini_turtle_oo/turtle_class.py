# turtle_class.py
class Tortuga:
    def __init__(self):
        # El estado es un atributo de instancia (Encapsulamiento)
        self.posicion_x = 0 

    def adelante(self, distancia):
        self.posicion_x += distancia
        print(f"Tortuga movida adelante {distancia}. Total: {self.posicion_x}")

    def abajo(self, distancia):
        print(f"Tortuga movida abajo {distancia}")

    def reiniciar(self):
        self.posicion_x = 0  # Sin usar 'global'
        print("Tortuga reiniciada.")
