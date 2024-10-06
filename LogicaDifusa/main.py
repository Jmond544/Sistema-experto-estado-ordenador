import json

# Cargar las reglas desde el archivo JSON
def cargar_reglas(archivo):
    with open(archivo, 'r') as f:
        reglas = json.load(f)
    return reglas['rules']

# Evaluar los síntomas contra las reglas
def diagnostico_pc(sintomas, reglas):
    for regla in reglas:
        if all(sintoma in sintomas for sintoma in regla['if']):
            return regla['then']
    return "No se encontró un diagnóstico específico. Consulta a un especialista."

# Obtener los síntomas del usuario
def obtener_sintomas():
    sintomas = []
    # print("Responde 'sí' o 'no' a las siguientes preguntas sobre tu ordenador:\n")
    
    lentitud = input("¿Tu ordenador está lento? (baja/media/alta): ").lower()
    if lentitud in ['baja', 'media', 'alta']:
        sintomas.append(f"lentitud {lentitud}")
    
    uso_cpu = input("¿El uso del CPU es bajo/medio/alto?: ").lower()
    if uso_cpu in ['bajo', 'medio', 'alto']:
        sintomas.append(f"uso de CPU {uso_cpu}")
    
    reinicios = input("¿El ordenador se reinicia con poca/moderada/frecuente frecuencia?: ").lower()
    if reinicios in ['pocos', 'moderados', 'frecuentes']:
        sintomas.append(f"reinicios {reinicios}")
    
    temperatura = input("¿Cómo describirías la temperatura del ordenador? (fría/normal/caliente): ").lower()
    if temperatura in ['fría', 'normal', 'caliente']:
        sintomas.append(f"temperatura {temperatura}")
    
    return sintomas

# Cargar las reglas
reglas = cargar_reglas('reglas_difusas.json')

# Obtener síntomas del usuario
sintomas_usuario = obtener_sintomas()

# Realizar diagnóstico
resultado = diagnostico_pc(sintomas_usuario, reglas)
print("\nDiagnóstico: ", resultado)