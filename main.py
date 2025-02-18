#!/bin/python3
from transformers import pipeline
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
import uvicorn

generator = pipeline('text-generation', model='gpt-2')
app = FastAPI(
    title = "Fast API App for LLM Model",
    description = "A text Generator App",
    version = '1.0'
)


class Body(BaseModel):
    text: str


@app.get('/')
def index():
    return HTMLResponse("<h1>Welcome to LLMOps App with a GPT2 model </h1>")

@app.post('/generate')
def predict(body :Body):
    results = generator(body.text, max_length=35, num_return_sequences=1)
    return results[0]['generated_text']

if __name__=="__main":
    uvicorn.run(app, host="0.0.0.0", port=80)

