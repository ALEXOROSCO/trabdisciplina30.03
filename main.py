from fastapi import FastAPI

app = FastAPI()


@app.get("/helloworld")
def read_root():
    return {"Hello": "World"}

@app.get("/funcaoteste1")
async def funcaoteste():
    return {"teste": "deu certo"}