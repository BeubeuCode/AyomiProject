from csv import writer as csv_writer
from io import StringIO, BytesIO

from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from lib.reverse_polish_notation import ReversePolishNotation
from lib.db import Database

app = FastAPI()

db = Database('calculator.db')

class ComputeRequest(BaseModel):
    calculation: str


@app.get('/')
def index():
    return {'status': 'OK'}


@app.get('/compute/')
def compute_get():
    return {'message': 'use POST method to compute'}

@app.post('/compute/')
def compute(request: ComputeRequest):
    rpn = ReversePolishNotation()
    result = rpn.calculate(request.calculation)

    db.insert_result(request.calculation, result)

    return {'result': result}

@app.get('/results/')
def results():
    results = db.get_all_results()
    return {'results': results}

@app.get('/results/csv')
async def results_as_csv():
    results = db.get_all_results()

    output = StringIO()
    writer = csv_writer(output)
    writer.writerow(['id', 'calculation', 'result'])

    for result in results:
        writer.writerow(result)

    output.seek(0)

    return StreamingResponse(BytesIO(output.read().encode('utf-8')), media_type="text/csv", headers={'Content-Disposition': 'attachment; filename="results.csv"'})


@app.on_event("shutdown")
async def shutdown():
    db.disconnect()
    pass