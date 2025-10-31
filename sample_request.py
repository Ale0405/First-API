import requests

base_URL = "http://127.0.0.1:8000"

def callsum(a: float, b:float, endpoint: str):
    URL = f"{base_URL}/{endpoint}/"
    params = {"a": a, "b": b}
    response = requests.get(url=URL, params=params)
    return response.text

def callmultiply(a: int | float, b: int | float, endpoint: str):
    URL = f"{base_URL}/{endpoint}/"
    params = {"a": a, "b": b}
    response = requests.get(url=URL, params=params)
    return float(response.text)

user_input = input('Where is your choice? A for sum or B for multiply. ')
if user_input.lower() == "a":
    somma = callsum(a=float(input("Write a number: ")), b=float(input("Write a number: ")), endpoint="sum")
    print(f'{float(somma):.2f}')
elif user_input.lower() == "b":
    multiply = callmultiply(a=float(input("Write a number: ")), b=float(input("Write a number: ")), endpoint="multiply")
    print(f"{multiply:.2f}")

def calldivison(a: int | float, b: int | float, endpoint:  str) -> int | float:
    URL = f"{base_URL}/{endpoint}/"
    params = {"a": a, "b": b}
    response = requests.get(url=URL, params=params)
    return int(response.text)

calldivison(0, 10, "Division")