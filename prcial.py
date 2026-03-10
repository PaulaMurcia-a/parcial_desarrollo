from typing import Optional
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Caballero(BaseModel):
    id: int
    nombre: str
    material: str
    ataque: int
    constelacion: str

caballeros = [
    Caballero(id=1, nombre="Seiya", material="Bronce", ataque=900, constelacion="Pegasus"),
    Caballero(id=2, nombre="Shiryu", material="Bronce", ataque=880, constelacion="Dragon"),
]

@app.get("/caballero/{caballero_id}", response_model=Optional[Caballero])
def show_caballero(caballero_id: int):
    for c in caballeros:
        if c.id == caballero_id:
            return c
    return None








