# Mi Primera Tortuga de Dibujo (Versión Funcional)

¡Bienvenido! Este es un proyecto sencillo donde aprendí a organizar mi código en Python usando **módulos** y **paquetes**.

### ¿De qué trata este proyecto?
Imagina que tienes una caja de herramientas. En este proyecto, guardamos todas las instrucciones para mover una "tortuga" (como avanzar o bajar) dentro de una carpeta llamada `mini_turtle`. 

### ¿Qué hace el código?
1. **Dibuja una escalera**: El programa principal (`main.py`) usa las herramientas de la carpeta para dibujar una figura paso a paso.
2. **Usa un contador global**: La tortuga siempre sabe en qué posición está porque usa una memoria compartida llamada `posicion_x`.
3. **Botón de reinicio**: Agregamos una función especial llamada `reiniciar()` que borra la memoria y regresa a la tortuga al punto de inicio (cero).

### Estructura del proyecto
* **mini_turtle/**: Es la carpeta donde viven las instrucciones.
* **drawer_logic.py**: Es el "cerebro" donde está escrita la lógica del movimiento.
* **__init__.py**: Es como la recepción de una oficina; ayuda a que sea fácil pedir las herramientas.
* **main.py**: Es donde nosotros, como usuarios, probamos que todo funcione.
* **pyproject.toml**: Archivo de configuración que contiene los metadatos del proyecto, como el nombre y la versión.
