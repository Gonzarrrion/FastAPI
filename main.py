from fastapi import FastAPI, HTTPException
from typing import List
from pydantic import BaseModel

app = FastAPI()

class Articulo(BaseModel):
    id: int
    titulo: str
    contenido: str

listaArticulos = [
    { "id": 1, "titulo": "Articulo 1", "contenido": "Contenido del articulo 1" },
    { "id": 2, "titulo": "Articulo 2", "contenido": "Contenido del articulo 2" },
    { "id": 3, "titulo": "Articulo 3", "contenido": "Contenido del articulo 3" },
    { "id": 4, "titulo": "Articulo 4", "contenido": "Contenido del articulo 4" }
]

# Obtener todos los articulos
@app.get("/articulos")
async def get_articulos():
    return listaArticulos

# Obtener un articulo por su id (Leer articulo)
@app.get("/articulos/{id}")
async def get_articulo(id: int):
    for articulo in listaArticulos:
        if articulo["id"] == id:
            return articulo
    raise HTTPException(status_code=404, detail="Articulo no encontrado")

# Crear un articulo
@app.post("/articulos")
async def create_articulo(articulo: Articulo):
    listaArticulos.append(articulo.model_dump())
    return articulo

# Borrar un articulo
@app.delete("/articulos/{id}")
async def delete_articulo(id: int):
    for index, articulo in enumerate(listaArticulos):
        if articulo["id"] == id:
            listaArticulos.pop(index)
            return { "message": "Articulo eliminado" }
    raise HTTPException(status_code=404, detail="Articulo no encontrado")

# Modificar un articulo
@app.put("/articulos/{id}")
async def update_articulo(id: int, articulo: Articulo):
    for index, a in enumerate(listaArticulos):
        if a["id"] == id:
            listaArticulos[index] = articulo.model_dump()
            return { "message": "Articulo modificado" }
    raise HTTPException(status_code=404, detail="Articulo no encontrado")

