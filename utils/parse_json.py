import json


def teste():
    print("teste")


def json2array():
    fileobject = open('dados/dor.json', 'r')
    json_data = fileobject.read()
    data = json.loads(json_data)
    print("data")
