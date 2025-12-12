# Evolución de Mini-Turtle 🐢

Este repositorio contiene la resolución de la práctica de programación donde se aplican conceptos de **modularidad**, **empaquetado** y **Programación Orientada a Objetos (POO)**.

## 📁 Estructura del Proyecto

El proyecto está dividido en dos grandes ejercicios que muestran la evolución del código:

### 1. Ejercicio 1: Versión Funcional (Modularidad)
En esta etapa, transformamos funciones sueltas en un paquete profesional llamado `mini_turtle`.
* **Lógica Separada**: El estado y las funciones de movimiento están en `drawer_logic.py`.
* **Interfaz Limpia**: Se usa `__init__.py` para permitir importaciones directas.
* **Estado Global**: Se maneja la posición mediante la palabra clave `global`.
[Tarea: Evolución de Mini-Turtle](https://github.com/tu-usuario/mini-turtle-task)

### 2. Ejercicio 2: Versión Orientada a Objetos (POO)
Refactorización del paquete para eliminar variables globales y aplicar **Encapsulamiento**.
* **Clase Tortuga**: Toda la lógica reside dentro de una clase.
* **Atributos de Instancia**: La posición se guarda en `self.posicion_x`, eliminando el uso de `global`.
* **Independencia**: Es posible crear múltiples objetos (ej. `t1` y `t2`) que mantienen sus posiciones de forma independiente.

[Tarea: Evolución de Mini-Turtle](https://github.com/tu-usuario/mini-turtle-task)

## 🚀 Cómo ejecutar las pruebas

1. **Para la versión funcional**: Ejecuta el archivo `main.py` en la raíz.
2. **Para la versión de objetos**: Ejecuta el archivo `main_oo.py` en la raíz.
