import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import json

# Definir las variables difusas
lentitud = ctrl.Antecedent(np.arange(0, 11, 1), 'lentitud')
temperatura = ctrl.Antecedent(np.arange(0, 101, 1), 'temperatura')
reinicios = ctrl.Antecedent(np.arange(0, 11, 1), 'reinicios')
uso_cpu = ctrl.Antecedent(np.arange(0, 101, 1), 'uso_cpu')  # Asegúrate de que coincida 'uso_cpu'

# Definir el diagnóstico como variable de salida
diagnostico = ctrl.Consequent(np.arange(0, 101, 1), 'diagnostico')

# Definir los conjuntos difusos para cada variable
lentitud['baja'] = fuzz.trimf(lentitud.universe, [0, 0, 4])
lentitud['media'] = fuzz.trimf(lentitud.universe, [2, 5, 8])
lentitud['alta'] = fuzz.trimf(lentitud.universe, [6, 10, 10])

temperatura['fria'] = fuzz.trimf(temperatura.universe, [0, 0, 30])
temperatura['normal'] = fuzz.trimf(temperatura.universe, [20, 50, 80])
temperatura['caliente'] = fuzz.trimf(temperatura.universe, [70, 100, 100])

reinicios['pocos'] = fuzz.trimf(reinicios.universe, [0, 0, 4])
reinicios['moderados'] = fuzz.trimf(reinicios.universe, [2, 5, 8])
reinicios['frecuentes'] = fuzz.trimf(reinicios.universe, [6, 10, 10])

uso_cpu['bajo'] = fuzz.trimf(uso_cpu.universe, [0, 0, 40])
uso_cpu['medio'] = fuzz.trimf(uso_cpu.universe, [30, 50, 70])
uso_cpu['alto'] = fuzz.trimf(uso_cpu.universe, [60, 100, 100])

diagnostico['bueno'] = fuzz.trimf(diagnostico.universe, [0, 0, 50])
diagnostico['regular'] = fuzz.trimf(diagnostico.universe, [30, 50, 70])
diagnostico['malo'] = fuzz.trimf(diagnostico.universe, [60, 100, 100])

# Función para cargar las reglas desde un archivo JSON
def cargar_reglas(archivo):
    with open(archivo, 'r') as f:
        reglas = json.load(f)
    return reglas['rules']

# Crear reglas difusas a partir del archivo JSON
def crear_reglas_difusas(reglas_json):
    reglas_difusas = []
    
    # Diccionario para agrupar las condiciones que tienen el mismo 'then'
    agrupador = {'malo': None, 'regular': None, 'bueno': None}

    for regla in reglas_json:
        condiciones_if = []
        
        for variable, valor in regla['if'].items():
            condiciones_if.append(eval(f"{variable}['{valor}']"))
        
        condicion_then = eval(f"diagnostico['{regla['then']}']")
        
        # Si ya hay una condición para ese 'then', agruparla con OR
        if agrupador[regla['then']] is None:
            agrupador[regla['then']] = ctrl.Rule(*condiciones_if, condicion_then)
        else:
            agrupador[regla['then']] = ctrl.Rule(agrupador[regla['then']].antecedent | (condiciones_if[0] & condiciones_if[1]), condicion_then)
    
    # Añadir todas las reglas agrupadas al listado final
    reglas_difusas.extend(list(agrupador.values()))
    
    return reglas_difusas

# Cargar las reglas desde el archivo
reglas_json = cargar_reglas('reglas_difusas.json')

# Crear el sistema de control difuso basado en las reglas cargadas
reglas_difusas = crear_reglas_difusas(reglas_json)

# Crear el sistema de control difuso
control_diagnostico = ctrl.ControlSystem(reglas_difusas)
simulacion_diagnostico = ctrl.ControlSystemSimulation(control_diagnostico)

# Función para realizar el diagnóstico basado en entradas difusas
def diagnosticar_pc(lentitud_val, temperatura_val, reinicios_val, uso_cpu_val):
    # Asignar los valores de entrada
    simulacion_diagnostico.input['lentitud'] = lentitud_val
    simulacion_diagnostico.input['temperatura'] = temperatura_val
    simulacion_diagnostico.input['reinicios'] = reinicios_val
    simulacion_diagnostico.input['uso_cpu'] = uso_cpu_val  # Asegúrate de que el nombre 'uso_cpu' coincida
    
    # Realizar la simulación
    simulacion_diagnostico.compute()
    
    # Obtener el resultado del diagnóstico
    resultado_diagnostico = simulacion_diagnostico.output['diagnostico']
    
    # Imprimir el resultado del diagnóstico
    print(f"Diagnóstico: {resultado_diagnostico:.2f} (0 = Bueno, 100 = Malo)")

# Ejemplo de uso:
# Lentitud: 7 (media), Temperatura: 75 (caliente), Reinicios: 8 (frecuentes), Uso de CPU: 80 (alto)
diagnosticar_pc(7, 75, 8, 80)
