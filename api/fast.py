from fastapi import FastAPI
from datetime import datetime

app = FastAPI()

@app.get('/')
def root():
    response = {
        'greeting': 'Servus, griaß di!',    # This is a typical Bavarian greeting ;)
        'timestamp': datetime.now()
    }

    return response
