from flask import Flask
from get_Info import get_info
from flask_cors import CORS
from convert import get_convert
import json


app = Flask(__name__)
CORS(app)


@app.route("/")
def index():

    g = get_info()
    print(g)
    return "Here are {}".format(g)


@app.route("/get", methods=['GET'])
def getInf():

    g = get_info()
    print(g)
    return g


@app.route("/convert", methods=['GET'])
def call_cat():
    b = get_convert()
    print(b)
    return b


if __name__ == "__main__":
    app.run()
