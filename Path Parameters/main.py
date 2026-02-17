from fastapi import FastAPI,status
from fastapi.responses import JSONResponse
from enum import Enum








app =FastAPI()










@app.get("/user/{id}")
async def user(id):
    print(id)
    return JSONResponse(status_code=status.HTTP_200_OK,content={"user": True})     



class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    return {"model_name": model_name}


@app.get("/")

async def health():
    
    return {"message": "Hello World"}
