from fastapi import FASTAPI , HTTPEXCEPTION
from fastapi.middleware import CORSMiddleware, HTTPEXCEPTION


app= FASTAPI()

@app.get("/")

async def welcome():

    try:
        return{"message":"hello from RCW"}
    except Exception as e:
        print(f'Exception:{e}')
        raise HTTPEXCEPTION (status_code=500,detail=str(e))
    

    @app.get("/test")

async def bienvenue():

    try:
        return{"message":"You are in RCW"}
    except Exception as e:
        print(f'Exception:{e}')
        raise HTTPEXCEPTION (status_code=500,detail=str(e))
    