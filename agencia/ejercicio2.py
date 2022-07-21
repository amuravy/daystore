import requests
import json


def GetElement(id):
    url = "https://api.datos.gob.mx/v1/calidadAire"
    response = requests.get(url)
    parse = json.loads(response)

