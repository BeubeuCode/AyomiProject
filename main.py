from fastapi import FastAPI
from pydantic import BaseModel
from lib.reverse_polish_notation import reverse_polish_notation_calculator_instance


app = FastAPI()

class ComputeRequest(BaseModel):
    calculation: str


@app.get('/')
def index():
    return {'status': 'OK'}


@app.post('/compute/')
def compute(request: ComputeRequest):
    return {'result': reverse_polish_notation_calculator_instance.calculate(request.calculation)}

