# main_oo.py
# Importamos la Clase Tortuga desde el paquete mini_turtle_oo
from mini_turtle_oo import Tortuga

# 1. Creamos el primer objeto (t1)
t1 = Tortuga()
# 2. Creamos el segundo objeto (t2)
t2 = Tortuga()

print("--- Movimiento de T1 ---")
t1.adelante(10)  # La posición de t1 será 10

print("\n--- Movimiento de T2 ---")
t2.adelante(50)  # La posición de t2 será 50

print("\n--- Verificación de Independencia ---")
# Aquí demostramos que no interfieren entre sí
print(f"Posición final de t1: {t1.posicion_x}")
print(f"Posición final de t2: {t2.posicion_x}")

# 3. Probamos el método reiniciar en solo uno de ellos
t1.reiniciar()
print(f"Nueva posición t1: {t1.posicion_x}")
print(f"Posición t2 sigue intacta: {t2.posicion_x}")
