from fastapi import FastAPI
from pydantic import BaseModel
from functions import cargar_reglas, diagnostico_pc

app = FastAPI()

class Sistema(BaseModel):
    lentitud: str  # "baja", "media", "alta"
    uso_cpu: str   # "bajo", "medio", "alto"
    reinicios: str # "pocos", "moderados", "frecuentes"
    temperatura: str # "fría", "normal", "caliente"

reglas = cargar_reglas('reglas_difusas.json')
print(reglas)

@app.post("/sistema/")
def crear_sistema(sistema: Sistema):
    resultado = diagnostico_pc(sistema, reglas)
    print(resultado)
    return {
        "mensaje": "Datos procesados correctamente",
        "diagnostico": resultado
    }
