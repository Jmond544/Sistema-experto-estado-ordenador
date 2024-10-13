from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from motor_inferencia import diagnostico_pc, cargar_reglas, Sistema, diagnostico_pc_difusa
from pydantic import BaseModel
from dotenv import load_dotenv
import os

load_dotenv()
app = FastAPI()

class Sintomas(BaseModel):
    sintomas: list[str]

# Configuración de CORS
origins = [
    "http://localhost",
    "http://localhost:8000",
    "http://localhost:5173",
    os.getenv("FRONTEND_URL"),
    # Agrega aquí otros orígenes permitidos
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"Hello": "World"}

# Endpoint para recibir los síntomas y devolver el diagnóstico
@app.post("/diagnostico-clasico")
def obtener_diagnostico(sintomas: Sintomas):
    print(sintomas)
    reglas = cargar_reglas('reglas.json')
    resultado = diagnostico_pc(sintomas.sintomas, reglas)
    return {"diagnostico": resultado}

@app.post("/diagnostico-difuso")
def crear_sistema(sistema: Sistema):
    reglas = cargar_reglas('reglas_difusas.json')
    resultado = diagnostico_pc_difusa(sistema, reglas)
    print(resultado)
    return {
        "mensaje": "Datos procesados correctamente",
        "diagnostico": resultado
    }

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

port = int(os.getenv("PORT"))

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=port, log_level="info")