from fastapi import FastAPI
import random 
app = FastAPI()


@app.get("/helloworld")
def read_root():
    return {"Hello": "World"}

@app.get("/teste")
async def funcaoteste():
    return {"teste": "num_aleatorio": random.randint(a:0, b:20000)}