import urllib.request
import json
import brotli
import requests
import reactivex as rx
from reactivex import Observable, Observer
from rx.subject import Subject
from rx import operators as ops


def get_info():
    r = requests.get("http://localhost:3000/inputData/2")
    f = r.json()
   # data = f['input']
   # print(data)
    print(f)
    return f


get_info()
