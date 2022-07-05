<p align="center"><a href="https://repuestosgalarza.com.ar" target="_blank"><img src="assets/logoq.png" width="400"></a></p>
<p align="center">

# Simulador de Colas

Este proyecto permite la simulación de colas desde un entorno de pruebas y objetivos académicos. Inspirado en la planilla de cálculo  "*QUEUING TEMPLATES*" desarrollada por  **David W. Ashley**.

En dicha planilla se tratan los siguiente modelos de colas:
- M/M/S
- M/M/S con tamaño de cola finita
- M/M/S con tamaño de población finita
- M/G/1

En la misma, se realizan cálculos demostrativo para un máximo de 170 servidores en todos los casos y 500 de población para el tercer caso.

El presente trabajo entrega una versión dinámica desarrollada para solventar el problema de limitación de servidores (y poblacional). El lenguaje de programación utilizado para el mismo es Python (v3.9.5).

# Usabilidad

Al igual que en la planilla de cálculo nombrada con anterioridad, la usabilidad es similar, se provee de una interfaz gráfica que permite la selección del modelo de cola requerido, una vez elegido se procede a la carga de datos propios del modelo. Posteriormente, se simula el modelo. Además es posible visualizar las probabilidades de manera gráfica (gráfico de barras). Ver [video](#Video)

# Video

https://user-images.githubusercontent.com/54777413/175728920-870e6c5b-8dd4-4437-80b0-ecdece4fa11b.mp4


# Desarrollo

## Versiones:
 
- Python 3.9.5
- PyQt5-5.15.7

## Instalación:

1. Instalar entorno virtual de Python:
   - `python3 -m venv env`
2. Activar el entorno:
   - `source env/bin/activate` (Linux)
   - `./env/bin/activate.bat` (Windows)
3. Instalar dependencias:
   - `pip install -r packages.txt`
4. Convertir .ui en .py:
   - `pyuic5 gui/app.ui -o gui/app.py`
5. Correr el entorno grafico:
   - `python __main__.py` 

* Se pueden obviar los pasos 4 y 5 ejecutando el bash `./run.sh`

# Autor

- Galarza Juan Ignacio

# Licencia
  
Este proyecto tiene la licencia MIT. Consulte el archivo [LICENSE.md](LICENSE.md) para obtener más detalles.