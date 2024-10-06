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

# Obtener los síntomas del usuario (misma función que antes)
def obtener_sintomas():
    sintomas = []
    print("Responde 'sí' o 'no' a las siguientes preguntas sobre tu ordenador:\n")
    
    if input("¿Tu ordenador está lento? (sí/no): ").lower() == 'sí':
        sintomas.append('lentitud')
    if input("¿El uso del CPU es alto? (sí/no): ").lower() == 'sí':
        sintomas.append('alto uso de CPU')
    if input("¿El ordenador se reinicia inesperadamente? (sí/no): ").lower() == 'sí':
        sintomas.append('reinicios inesperados')
    if input("¿Notas sobrecalentamiento? (sí/no): ").lower() == 'sí':
        sintomas.append('calentamiento')
    if input("¿No tienes conexión a Internet? (sí/no): ").lower() == 'sí':
        sintomas.append('sin conexión')
    if input("¿Otros dispositivos tienen conexión a Internet? (sí/no): ").lower() == 'sí':
        sintomas.append('otros dispositivos conectados')
    if input("¿Has visto un pantallazo azul? (sí/no): ").lower() == 'sí':
        sintomas.append('pantallazo azul')
    if input("¿Escuchas ruidos extraños del ordenador? (sí/no): ").lower() == 'sí':
        sintomas.append('ruido extraño')
    if input("¿El ruido viene del disco duro? (sí/no): ").lower() == 'sí':
        sintomas.append('del disco duro')

    return sintomas

# Cargar las reglas
reglas = cargar_reglas('reglas.json')

# Obtener síntomas del usuario
sintomas_usuario = obtener_sintomas()

# Realizar diagnóstico
resultado = diagnostico_pc(sintomas_usuario, reglas)
print("\nDiagnóstico: ", resultado)

