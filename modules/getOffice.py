from tabulate import tabulate
import json
import os
import requests

def getAllData():
    peticion = requests.get("http://154.38.171.54:5005/oficinas")
    data = peticion.json()
    return data

# LOCAL
# def getAllData():
#     #json-server storage/oficina.json -b 5503
#     peticion = requests.get("http://192.168.1.39:5503")
#     data = peticion.json()
#     return data

def getOfficeCodigo(codigo):
    for val in getAllData():
        if(val.get("codigo_oficina") == codigo):
            return [val]

def getIdOffice(id):
     peticion = requests.get(f"http://154.38.171.54:5005/oficinas/{id}") 
     return [peticion.json()] if peticion.ok else []  

#LOCAL                
# def getIdOffice(id):
#     peticion = requests.get(f"http://192.168.1.39:5503/{id}") 
#     return [peticion.json()] if peticion.ok else []              

def getOfficeCity(pais):
    cityOffice = []
    for val in getAllData():
        if (val.get("pais") == pais):
            ciudadOficina = ({
                "ciudad": val.get('ciudad'),
                "oficina": val.get('codigo_oficina'),
                "telefono": val.get('telefono')
            })
            cityOffice.append(ciudadOficina)
    return cityOffice              

def menu():
    flag=1
    while flag == 1:
        os.system("cls")
        print(f"""
            --- Reportes ---
            
            1. Obtener oficinas por pais
            0. Menu principal  
            """)
        
        op = input("Seleccione una opcion: ")
        
        if op == "1":
            pais = input("Pais: ")
            print(tabulate(getOfficeCity(pais),headers="keys",tablefmt="github"))
            flag = int(input("Desea realizar otra consulta: 1=Si  0=No: ")) 
        elif op == "0":
            return
