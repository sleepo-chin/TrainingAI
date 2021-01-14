from tensorflow.keras.models import load_model
from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np

app = FastAPI()

class Data(BaseModel):
    x:float
    y:float

def loadModel():
    global predict_model

    predict_model = load_model('model1.h5')

loadModel()

async def predict(data):
    classNameCat = {0:'class_A', 1:'class_B', 2:'class_C'}
    X = np.array([[data.x, data.y]])

    pred = predict_model.predict(X)

    res = np.argmax(pred, axis=1)[0]
    category = classNameCat[res]
    confidence = float(pred[0][res])
        
    return category, confidence

@app.post("/getclass/")
async def get_class(data: Data):
    category, confidence = await predict(data)
    res = {'class': category, 'confidence':confidence}
    return {'results': res}