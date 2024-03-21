import os
import re
import json
import requests
import modules.getOffice as gOff
from tabulate import tabulate

def postOffice():
    newOffice = dict()
    while True:
        try: 
            #Validacion codigo oficina
            if(not newOffice.get("codigo_oficina")):
                codigo = input("Codigo de oficina /ej: ABC-DE/: ")
                if(re.match(r'^[A-Z]{3}-[A-Z]{2}$', codigo) is not None):
                    data = gOff.getOfficeCodigo(codigo)
                    if (data):
                        print(tabulate(data, headers="keys", tablefmt="github"))
                        raise Exception("El codigo de oficina ya existe")
                    else:
                        newOffice["codigo_oficina"] = codigo
                else:
                    raise Exception("El codigo de oficina no cumple con el estandar establecido, debe ser con el formato de ejemplo")
            #validacion ciudad
            if(not newOffice.get("ciudad")):
                ciudad = input("Ciudad /ej: Bucaramanga/: ")
                if(re.match(r'^\D+$', ciudad) is not None):
                    ciudad = ciudad.title()
                    newOffice["ciudad"] = ciudad
                else:
                    raise Exception("La ciudad de la oficina no cumple con el estandar establecido, no puede ser vacio ni contener numeros")
            #validacion pais
            if(not newOffice.get("pais")):
                pais = input("Pais /ej: Colombia/: ")
                if(re.match(r'^\D+$', pais) is not None):
                    pais = pais.title()
                    newOffice["pais"] = pais
                else:
                    raise Exception("El pais de la oficina no cumple con el estandar establecido, no puedo ser vacio ni contener numeros")
            #validacion region 
            if(not newOffice.get("region")):
                region = input("Region /ej: Santander/: ")
                region = region.title()
                newOffice["region"] = region
            #validacion codigo postal
            if(not newOffice.get("codigo_postal")):
                codigoPostal = input("Codigo postal /ej: 170435/: ")
                if(re.match(r"^[^a-zA-Z]+$", codigoPostal) is not None):
                    newOffice["codigo_postal"] = codigoPostal
                else:
                    raise Exception("El codigo postal de la oficina no cumple con el estandar establecido, debe contener solo numeros")
            #validacion telefono
            if(not newOffice.get("telefono")):
                telefono = input("Telefono /ej: 1234567890/: ")
                if(re.match(r'^\d{10}$', telefono) is not None):
                    newOffice["telefono"] = telefono        
                else:
                    raise Exception("El telefono de la oficina no cumple con el estandar establecido, debe contener 10 numeros")                
            #validacion linea direccion 1
            if(not newOffice.get("linea_direccion1")):
                lineaDir1 = input("Direccion 1 /ej: Calle 1 #34/: ")
                if(re.match(r"^(?=\S{5,}).+$", lineaDir1) is not None):
                    newOffice["linea_direccion1"] = lineaDir1
                else:
                    raise Exception("La direccion de la oficina no cumple con el estandar establecido, no puede ser vacio")                
            #validacion linea direccion 2
            if(not newOffice.get("linea_direccion2")):
                lineaDir2 = input("Direccion 2 /ej: Calle 1 #34/: ")
                if(lineaDir2 != lineaDir1) is not None:
                    newOffice["linea_direccion2"] = lineaDir2
                else:
                    raise Exception("La direccion 2 de la oficina no puede ser igual que la direccion 2, de no tener dejar vacio")

            peticion = requests.post("http://154.38.171.54:5005/oficinas", data=json.dumps(newOffice))
            res = peticion.json()
            res["Mensaje"] = "Oficina guardada"
            return [res]
            #LOCAL                    
            # peticion = requests.post("http://192.168.1.39:5503", data=json.dumps(newOffice))
            # res = peticion.json()
            # res["Mensaje"] = "Oficina guardada"
            # return [res]
        
        except Exception as error:
            print(error)      

def deleteOffice():
    print(tabulate(gOff.getAllData(),headers="keys", tablefmt="github"))
    id = input("Ingrese el id que desea eliminar: ")
    data = gOff.getIdOffice(id)
    if(len(data)):
        peticion = requests.delete(f"http://154.38.171.54:5005/oficinas/{id}")
        #LOCAL
        #peticion = requests.delete(f"http://192.168.1.39:5503/{id}")
        if(peticion.status_code == 204 or peticion.status_code == 200):
            return("Oficina eliminada correctamente")
        else:
            return peticion.status_code
    else:
        return("Oficina no encontrada")
               
def menu():
    flag = 1
    while flag == 1:
        os.system("cls")
        print(f"""
            --- Administrar datos de oficina ---
            
            1. Guardar oficina nueva
            2. Eliminar nueva oficina   
            0. Atras
            """)
        
        op = input("Seleccione una opcion: ")
        
        if op == "1":
            print(tabulate(postOffice(),headers="keys", tablefmt="github"))
            input("Oprima una tecla para ingresar nueva opcion....")
        elif op == "2":
            print(deleteOffice())
            input("Oprima una tecla para ingresar nueva opcion....")
        elif op == "0":
            flag = 0    
        else:
            print("No es una opcion valida") 