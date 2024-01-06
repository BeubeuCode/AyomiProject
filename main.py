from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    return {'status': 'OK'}

@app.get('/compute')
def compute():
    return {'status': 'OK'}