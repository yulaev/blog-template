from fastapi import FastAPI, Request

app = FastAPI()

@app.post("/posts")
def create_post():
    pass