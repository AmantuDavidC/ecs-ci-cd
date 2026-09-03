from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
 return {"message": "Hello, this is the linear deployment app!"}

