import requests
from callback import catcall
import json


def get_convert():
    r = requests.get("http://localhost:3000/inputData/2")
    f = r.json()
    data = f['input']
    print(data)
    catcall(data)
    print("Finished")
    return f
