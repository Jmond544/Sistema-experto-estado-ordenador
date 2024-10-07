# Sistema Experto con Lógica Difusa para Diagnóstico de Ordenadores

## 1. Descripción del Proyecto

Este proyecto implementa un sistema experto que utiliza lógica difusa para diagnosticar posibles problemas en un ordenador, basándose en varios síntomas como la lentitud, temperatura, frecuencia de reinicios y uso del CPU. El sistema toma decisiones basadas en reglas difusas predefinidas, ofreciendo recomendaciones o posibles causas de los problemas observados.

El proyecto utiliza **FastAPI** para ofrecer una API REST que permite la interacción con el sistema de manera sencilla, y **Pydantic** para la validación de los datos de entrada.

## 2. Tecnologías Utilizadas

- **Python 3.x**: Lenguaje de programación base del proyecto.
- **FastAPI**: Framework web moderno y de alto rendimiento que permite definir y manejar rutas de la API, proporcionando una interfaz eficiente para realizar diagnósticos.
- **Pydantic**: Utilizado para la validación de los modelos de datos en la API.
- **Uvicorn**: Servidor ASGI utilizado para ejecutar la aplicación FastAPI.
- **JSON**: Almacenamiento de las reglas difusas en formato JSON para facilitar la extensión y modificación de reglas.
- **Lógica Difusa**: La lógica difusa se utiliza para asignar rangos difusos a los síntomas y procesar los datos de entrada.

## 3. Definición del Problema

El sistema se basa en los siguientes síntomas clave, a los que se les asignan rangos difusos:

- **Lentitud**: Baja, Media, Alta.
- **Temperatura**: Fría, Normal, Caliente.
- **Reinicios**: Pocos, Moderados, Frecuentes.
- **Uso de CPU**: Bajo, Medio, Alto.

### Conjuntos Difusos

Cada síntoma tiene un conjunto difuso asignado, y estos son evaluados por el sistema según reglas definidas en un archivo JSON.

## 4. Estructura del Proyecto

El proyecto está compuesto por los siguientes archivos clave:

### `functions.py`

Contiene las funciones necesarias para cargar las reglas difusas desde un archivo JSON y para evaluar los síntomas proporcionados por el usuario en función de estas reglas. Utiliza las siguientes funciones principales:

- **`cargar_reglas(archivo)`**: Carga las reglas difusas desde un archivo JSON.
- **`diagnostico_pc(sistema: Sistema, reglas)`**: Evalúa los síntomas ingresados por el usuario contra las reglas y proporciona un diagnóstico basado en estas.

### `main.py`

Define una API REST utilizando FastAPI. Los usuarios pueden enviar un conjunto de síntomas a través de un endpoint POST para recibir un diagnóstico basado en las reglas difusas.

- **Endpoint**: `/sistema/` (POST)
  - Recibe un JSON con los síntomas del sistema.
  - Devuelve un diagnóstico basado en las reglas difusas.

### `reglas_difusas.json`

Este archivo contiene las reglas difusas en formato JSON. Cada regla se define con una condición "if" (basada en los síntomas) y una acción "then" (diagnóstico).

#### Ejemplo de Regla:

```json
{
    "if": ["lentitud alta", "uso de CPU alto"],
    "then": "Posible sobrecarga de procesos. Revisa los procesos en segundo plano o aumenta la RAM."
}
```

## 5. Ejecución del Proyecto

### Requisitos Previos

- Python 3.x
- FastAPI
- Pydantic
- Uvicorn

Instalar las dependencias ejecutando el siguiente comando:

```bash
pip install fastapi pydantic uvicorn
```

### Ejecutar el servidor
Para iniciar el servidor de FastAPI y exponer la API, ejecutar el siguiente comando:

```bash
uvicorn main:app --reload
```

### Ejemplo de petición
Envío de un JSON a la API para obtener un diagnóstico:
```bash
{
  "lentitud": "alta",
  "uso_cpu": "medio",
  "reinicios": "frecuentes",
  "temperatura": "caliente"
}
```
### Ejemplo de respuesta:
```bash
{
  "mensaje": "Datos procesados correctamente",
  "diagnostico": "Posible sobrecalentamiento. Limpia los ventiladores o revisa la pasta térmica."
}
```


