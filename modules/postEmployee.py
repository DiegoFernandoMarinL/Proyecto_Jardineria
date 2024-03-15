import os
import json

from tabulate import tabulate

def postEmpleado():
    import requests
    #json-server storage/empleado.json -b 5501
    newEmpleado = {
            "codigo_empleado": int(input("Codigo de empleado: ")),
            "nombre": input("Nombre empleado: "),
            "apellido1": input("Primer apellido"),
            "apellido2": input("Segundo apellido"),
            "extension": input("Extension: "),
            "email": input("Email: "),
            "codigo_oficina": input("Codigo oficina: "),
            "codigo_jefe": input("Codigo jefe: "),
            "puesto": "Cargo: "    
        }
    
    peticion = requests.post("http://192.168.0.11:5501", data=json.dumps(newEmpleado))
    res = peticion.json()
    res["Mensaje"] = "Empleado guardado"
    return [res] 

def menu():
    flag = 1
    while flag == 1:
        os.system("clear")
        print(f"""
            --- Administrar datos de productos ---
            
            1. Guardar un cliente nuevo
            0. Atras
            """)
        
        op = input("Seleccione una opcion: ")
        
        if op == "1":
            print(tabulate(postEmpleado(),headers="keys", tablefmt="github"))
        elif op == "0":
            flag = 0    
        else:
            print("No es una opcion valida") 