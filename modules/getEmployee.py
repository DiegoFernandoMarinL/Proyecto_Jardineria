from tabulate import tabulate
import json

def getAllData():
    import requests
    #json-server storage/empleado.json -b 5501
    peticion = requests.get("http://192.168.0.11:5501")
    data = peticion.json()
    return data

def getCodManager(codigoJefe):
    jefeCod = []
    for val in getAllData():
        if (val.get("codigo_jefe") == codigoJefe):
            addEmployee = ({
                "nombre": val.get("nombre"),
                "apellidos": f'{val.get("apellido1")} {val.get("apellido2")}',
                "email": val.get("email")    
            })  
            jefeCod.append(addEmployee)  
    return jefeCod

def getManagerGeneral():
    jefeCod = []
    for val in getAllData():
        if (val.get("codigo_jefe") == None):
            jefeCod.append({
                "cargo": val.get("puesto"),
                "nombre": val.get("nombre"),
                "apellidos": f'{val.get("apellido1")} {val.get("apellido2")}',
                "email": val.get("email")     
            })
    return jefeCod

def getPlacework(puesto):
    puestos = []
    for val in getAllData():
        if (val.get("puesto") == puesto):
            puestos.append({
                "nombre": val.get("nombre"),
                "apellidos": f'{val.get("apellido1")} {val.get("apellido2")}',
                "cargo": val.get("puesto") 
            })  
    return puestos         

def menu():
    flag=1
    while flag == 1:
        print(f"""
            --- Reportes ---
            
            1. Obtener empleados por codigo de jefe
            2. Obtener datos del jefe actual
            3. Obtener empleados por puesto de trabajo
            0. Menu principal  
            """)
        
        op = input("Seleccione una opcion: ")
        
        if op == "1":
            codigoJefe = int(input("Digite codigo del jefe: "))
            print(tabulate(getCodManager(codigoJefe),headers="keys",tablefmt="github"))
            flag = int(input("Desea realizar otra consulta: 1=Si  0=No: ")) 
        elif op == "2":
            print(tabulate(getManagerGeneral(),headers="keys",tablefmt="github"))
            flag = int(input("Desea realizar otra consulta: 1=Si  0=No: "))
        elif op == "3":
            puesto = input("Escriba cargo del empleado: ")
            print(tabulate(getPlacework(puesto),headers="keys",tablefmt="github"))
            flag = int(input("Desea realizar otra consulta: 1=Si  0=No: "))
        elif op == "0":
            return
        else:
            print("No es una opcion valida")