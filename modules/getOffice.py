from tabulate import tabulate
import json
import os
import requests

def getAllData():
    import requests
    #json-server storage/oficina.json -b 5503
    peticion = requests.get("http://172.16.100.122:5503")
    data = peticion.json()
    return data

def getOfficeCodigo(codigo):
    for val in getAllData():
        if(val.get("codigo_oficina") == codigo):
            return [val]
        
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
        print(f"""
            --- Reportes ---
            
            1. Obtener oficinas por pais
            2. ....
            0. Menu principal  
            """)
        
        op = input("Seleccione una opcion: ")
        
        if op == "1":
            pais = input("Pais: ")
            print(tabulate(getOfficeCity(pais),headers="keys",tablefmt="github"))
            flag = int(input("Desea realizar otra consulta: 1=Si  0=No: ")) 
        elif op == "0":
            return
