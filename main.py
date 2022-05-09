from sre_parse import State
import string
from sys import intern
from tokenize import String
from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Note(BaseModel):
    title : str
    content: str

@app.get("/")
async def read_root():
    return {"Hello": "World"}

# API
@app.post("/notes/{note_id}")
async def update_note(note_id: int, note_element: str):
    return{"note_id": note_id, "note_title" : Note.title, "note_content" : Note.contentq}

@app.get("/notes/{note_id}")
async def read_note(note_id: int, note_title: str):
    return{"note_id": note_id, "note_title" : note_title}

@app.put("/notes/{note_id}")
async def update_note(note_id: int, note_element: str):
    return{"note_id": note_id, "note_title" : Note.title, "note_content" : Note.contentq}

@app.delete("/notes/{note_id}")
async def delete_note(note_id: int):
    return{"note_id": note_id}