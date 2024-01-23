import logging
from functools import cache
from fastapi import FastAPI, Query

from .text_generation import TextGenerator

app = FastAPI()

@cache
def get_model() -> TextGenerator:
    logging.info("Loading DistilGPT2 model")
    return TextGenerator()

@app.on_event("startup")
async def on_startup():
    get_model()

@app.get("/")
async def health():
    return {"health": "ok"}

@app.get("/{prompt}")
async def generate_text(
    prompt: str,
    max_new_tokens: int = 50,
    num_return_sequences: int = 1,
) -> dict:
    model = get_model()
    sequences = model.generate(
        prompt, max_new_tokens=max_new_tokens, num_return_sequences=num_return_sequences
    )
    return {"generated_sequences": sequences}

# New endpoint for adding two numbers
@app.get("/add_numbers")
async def add_numbers(
    num1: int = Query(..., description="First number"),
    num2: int = Query(..., description="Second number"),
) -> dict:
    result = num1 + num2
    return {"result": result}


import logging
from functools import cache
from fastapi import FastAPI, Query

from .text_generation import TextGenerator

app = FastAPI()

@cache
def get_model() -> TextGenerator:
    logging.info("Loading DistilGPT2 model")
    return TextGenerator()

@app.on_event("startup")
async def on_startup():
    get_model()

@app.get("/")
async def health():
    return {"health": "ok"}

@app.get("/{prompt}")
async def generate_text(
    prompt: str,
    max_new_tokens: int = 50,
    num_return_sequences: int = 1,
) -> dict:
    model = get_model()
    sequences = model.generate(
        prompt, max_new_tokens=max_new_tokens, num_return_sequences=num_return_sequences
    )
    return {"generated_sequences": sequences}

# New endpoint for adding two numbers
@app.get("/add_numbers")
async def add_numbers(
    num1: int = Query(..., description="First number"),
    num2: int = Query(..., description="Second number"),
) -> dict:
    result = num1 + num2
    return {"result": result}
