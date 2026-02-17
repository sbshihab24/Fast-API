from fastapi import FastAPI

app = FastAPI()

@app.get("/")



async def root():
    return {"message": "Hello World"}


@app.get("/user")
async def user():
    return {"message": "User information",
            "id": 12345,
            "name": "Shihab",
            "password": "secure123",
            "phone": "0123456789",
            "email": "shihab@example.com"
            }

