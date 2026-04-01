from fastapi import FastAPI

app = FastAPI()


@app.get("/helloworld")
def read_root():
    return {"Hello": "World"}

@app.get("/teste")
async def funcaoteste():
    return {"teste": "deu certo"}