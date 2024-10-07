import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Definir las variables difusas (antecedentes)
lentitud = ctrl.Antecedent(np.arange(0, 11, 1), 'lentitud')
uso_cpu = ctrl.Antecedent(np.arange(0, 101, 1), 'uso_cpu')
reinicios = ctrl.Antecedent(np.arange(0, 11, 1), 'reinicios')
temperatura = ctrl.Antecedent(np.arange(0, 101, 1), 'temperatura')
conexion = ctrl.Antecedent(np.arange(0, 2, 1), 'conexion')  # 0 = sin_conexion, 1 = con_conexion
otros_dispositivos = ctrl.Antecedent(np.arange(0, 2, 1), 'otros_dispositivos')
pantallazo = ctrl.Antecedent(np.arange(0, 2, 1), 'pantallazo')  # 0 = no, 1 = sí
ruido_disco = ctrl.Antecedent(np.arange(0, 11, 1), 'ruido_disco')

# Definir la variable difusa de salida (diagnóstico)
diagnostico = ctrl.Consequent(np.arange(0, 101, 1), 'diagnostico')

# Definir los conjuntos difusos para las entradas
lentitud['baja'] = fuzz.trimf(lentitud.universe, [0, 0, 4])
lentitud['media'] = fuzz.trimf(lentitud.universe, [2, 5, 8])
lentitud['alta'] = fuzz.trimf(lentitud.universe, [6, 10, 10])

uso_cpu['bajo'] = fuzz.trimf(uso_cpu.universe, [0, 0, 40])
uso_cpu['medio'] = fuzz.trimf(uso_cpu.universe, [30, 50, 70])
uso_cpu['alto'] = fuzz.trimf(uso_cpu.universe, [60, 100, 100])

reinicios['pocos'] = fuzz.trimf(reinicios.universe, [0, 0, 4])
reinicios['moderados'] = fuzz.trimf(reinicios.universe, [2, 5, 8])
reinicios['frecuentes'] = fuzz.trimf(reinicios.universe, [6, 10, 10])

temperatura['fria'] = fuzz.trimf(temperatura.universe, [0, 0, 30])
temperatura['normal'] = fuzz.trimf(temperatura.universe, [20, 50, 80])
temperatura['caliente'] = fuzz.trimf(temperatura.universe, [70, 100, 100])

# Definir los conjuntos difusos para las variables binarias (conexión, pantallazo, etc.)
conexion['sin_conexion'] = fuzz.trimf(conexion.universe, [0, 0, 1])
conexion['con_conexion'] = fuzz.trimf(conexion.universe, [0, 1, 1])

otros_dispositivos['sin_conexion'] = fuzz.trimf(otros_dispositivos.universe, [0, 0, 1])
otros_dispositivos['con_conexion'] = fuzz.trimf(otros_dispositivos.universe, [0, 1, 1])

pantallazo['no'] = fuzz.trimf(pantallazo.universe, [0, 0, 1])
pantallazo['si'] = fuzz.trimf(pantallazo.universe, [0, 1, 1])

ruido_disco['bajo'] = fuzz.trimf(ruido_disco.universe, [0, 0, 4])
ruido_disco['alto'] = fuzz.trimf(ruido_disco.universe, [6, 10, 10])

# Definir los conjuntos difusos para la salida (diagnóstico)
diagnostico['sobrecarga_procesos'] = fuzz.trimf(diagnostico.universe, [60, 70, 100])
diagnostico['sobrecalentamiento'] = fuzz.trimf(diagnostico.universe, [60, 80, 100])
diagnostico['problema_red'] = fuzz.trimf(diagnostico.universe, [50, 70, 100])
diagnostico['error_hardware'] = fuzz.trimf(diagnostico.universe, [70, 90, 100])
diagnostico['fallo_disco_duro'] = fuzz.trimf(diagnostico.universe, [70, 90, 100])

# Crear las reglas difusas
regla_1 = ctrl.Rule(lentitud['alta'] & uso_cpu['alto'], diagnostico['sobrecarga_procesos'])
regla_2 = ctrl.Rule(reinicios['frecuentes'] & temperatura['caliente'], diagnostico['sobrecalentamiento'])
regla_3 = ctrl.Rule(conexion['sin_conexion'] & otros_dispositivos['con_conexion'], diagnostico['problema_red'])
regla_4 = ctrl.Rule(pantallazo['si'], diagnostico['error_hardware'])
regla_5 = ctrl.Rule(ruido_disco['alto'], diagnostico['fallo_disco_duro'])

# Crear el sistema de control difuso
sistema_control = ctrl.ControlSystem([regla_1, regla_2, regla_3, regla_4, regla_5])
simulacion_diagnostico = ctrl.ControlSystemSimulation(sistema_control)

# Función para hacer preguntas al usuario y obtener los valores de entrada
def obtener_input_usuario():
    lentitud_val = int(input("¿Cuál es el nivel de lentitud del sistema? (0 = baja, 10 = alta): "))
    uso_cpu_val = int(input("¿Cuál es el porcentaje de uso de CPU? (0 a 100): "))
    reinicios_val = int(input("¿Cuántos reinicios inesperados ha tenido? (0 a 10): "))
    temperatura_val = int(input("¿Cuál es la temperatura del sistema en grados (0 a 100)? "))
    conexion_val = int(input("¿Tiene conexión a internet? (0 = sin conexión, 1 = con conexión): "))
    otros_dispositivos_val = int(input("¿Otros dispositivos tienen conexión a internet? (0 = no, 1 = sí): "))
    pantallazo_val = int(input("¿Ha ocurrido un pantallazo azul? (0 = no, 1 = sí): "))
    ruido_disco_val = int(input("¿Qué tan alto es el ruido del disco duro? (0 = bajo, 10 = alto): "))

    return {
        'lentitud': lentitud_val,
        'uso_cpu': uso_cpu_val,
        'reinicios': reinicios_val,
        'temperatura': temperatura_val,
        'conexion': conexion_val,
        'otros_dispositivos': otros_dispositivos_val,
        'pantallazo': pantallazo_val,
        'ruido_disco': ruido_disco_val
    }

# Asignar los valores de entrada a la simulación desde las respuestas del usuario
def asignar_valores(simulacion, inputs):
    simulacion.input['lentitud'] = inputs['lentitud']
    simulacion.input['uso_cpu'] = inputs['uso_cpu']
    simulacion.input['reinicios'] = inputs['reinicios']
    simulacion.input['temperatura'] = inputs['temperatura']
    simulacion.input['conexion'] = inputs['conexion']
    simulacion.input['otros_dispositivos'] = inputs['otros_dispositivos']
    simulacion.input['pantallazo'] = inputs['pantallazo']
    simulacion.input['ruido_disco'] = inputs['ruido_disco']

# Ejecutar la simulación y mostrar el resultado
def diagnosticar_pc():
    # Obtener los inputs del usuario
    inputs = obtener_input_usuario()

    # Asignar valores a la simulación
    asignar_valores(simulacion_diagnostico, inputs)

    # Ejecutar la simulación
    simulacion_diagnostico.compute()

    # Obtener el resultado del diagnóstico
    resultado = simulacion_diagnostico.output['diagnostico']
    print(f"Diagnóstico: {resultado:.2f} (0 = Bueno, 100 = Malo)")

# Ejecutar el sistema de diagnóstico
diagnosticar_pc()
