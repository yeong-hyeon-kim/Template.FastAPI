from sre_parse import State
from sys import intern
from tokenize import String
from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Note(BaseModel):
    title : str
    content: str
    is_offer: Optional[bool] = None

@app.get("/")
async def read_root():
    return {"Hello": "World"}

# API
@app.post("/notes/{note_id}")
async def update_note(note_id: int, note_title: str, note_content: str):
    return{"note_id": note_id, "note_title" : note_title, "note_content" : note_content}

@app.get("/notes/{note_id}")
async def read_note(note_id: int):
    return{"note_id": note_id}

@app.put("/notes/{note_id}")
async def update_note(note_id: int, note_element: Optional[str] = None):
    return{"note_id": note_id, "note_element" : note_element}

@app.delete("/notes/{note_id}")
async def delete_note(note_id: int):
    return{"note_id": note_id}