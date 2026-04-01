from fastapi import FastAPI
import random 
app = FastAPI()

# 127.0.0.1:8000
@app.get("/")
def read_root():
    return {"Hello": "World"}

# 127.0.0.1:8000/teste1
@app.get("/teste1")
async def funcaoteste():
    return {"teste": "num_aleatorio": random.randint(a:0, b:1000)}