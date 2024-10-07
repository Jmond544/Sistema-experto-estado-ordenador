# Sistema Experto con Lógica Difusa para Diagnóstico de PC

Este proyecto implementa un **sistema experto** basado en **lógica difusa** para diagnosticar el estado de una PC utilizando variables como la **lentitud**, **temperatura**, **reinicios**, y **uso de CPU**. El sistema emplea reglas difusas para determinar si el estado general de la PC es **bueno**, **regular**, o **malo**. Esto puede ser útil para el diagnóstico de problemas de rendimiento o sobrecalentamiento de una computadora.

## Contenidos del Proyecto

El proyecto contiene los siguientes archivos clave:

- **`main.py`**: Contiene el código principal del sistema difuso.
- **`reglas_difusas.json`**: Archivo de configuración de las reglas difusas en formato JSON.

## Requisitos Previos

Para ejecutar este proyecto, asegúrate de tener instalados los siguientes paquetes de Python:

- **numpy**: Para manejar las operaciones con matrices y números.
- **scikit-fuzzy**: Para implementar la lógica difusa.

Puedes instalarlos ejecutando el siguiente comando:

```
pip install numpy scikit-fuzzy
```

## 1. Definir el dominio del problema

Vamos a tomar algunos síntomas clave y asignarles rangos difusos. Los síntomas que usaremos serán:

- `Lentitud`: ¿Qué tan lento está el ordenador?
- `Temperatura`: ¿El ordenador está sobrecalentado?
- `Reinicios`: ¿Con qué frecuencia se reinicia el ordenador?
- `Uso de CPU`: ¿Qué tan alta es la carga del CPU?

Conjuntos difusos que podemos utilizar:

- `Lentitud`: Puede ser "Baja", "Media" o "Alta".
- `Temperatura`: Puede ser "Fría", "Normal" o "Caliente".
- `Reinicios`: Puede ser "Pocos", "Moderados" o "Frecuentes".
- `Uso de CPU`: Puede ser "Bajo", "Medio" o "Alto".

## 2. Endpoints

## 3. Ejecución del proyecto

Sigue estos pasos para ejecutar el proyecto:

a. Clona este repositorio en tu máquina local o descarga los archivos.
    ```
    git clone https://github.com/tu-usuario/tu-repositorio.git
    ```

b. Instala las dependencias necesarias ejecutando el siguiente comando:
    ```
    pip install numpy scikit-fuzzy
    ```

c. Ejecuta el archivo `main.py` con Python:
    ```
    python main.py
    ```

d. Dentro del archivo `main.py`, puedes modificar los valores de entrada de la función `diagnosticar_pc()` para realizar tu propio diagnóstico. Por ejemplo:
    ```python
    diagnosticar_pc(7, 75, 8, 80)
    ```

