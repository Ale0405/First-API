from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/")
def welcome():
    return {"Message": "Welcome to calculator API!"}

@app.get("/sum/")
def sum(a: float, b: float) -> float:
    return a + b

@app.get("/multiply/")
def multyply(a: int | float, b:int | float) -> int | float:
    return a * b

@app.get("/Division/")
def division(a: int | float , b: int | float) -> int | float:
    if b == 0:
        return 0
    else:
        return a / b