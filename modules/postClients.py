import json

def postEmpleado(empleado):
    import requests
    #json-server storage/empleado.json -b 5501
    peticion = requests.post("http://172.16.100.119:5501", data=json.dumps(empleado))
    res = peticion.json()
    return res