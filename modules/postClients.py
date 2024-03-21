import os
import re
import json
import requests
import modules.getClients as gCli
from tabulate import tabulate

def postEmpleado():
    newClients = dict()
    while True:
        try: 
            #Validacion codigo cliente
            if(not newClients.get("codigo_cliente")):
                codigo = input("Codigo de cliente /ej: 37/: ")
                if(re.match(r'^[0-9]+$', codigo) is not None):
                    data = gCli.getClientsCodigo(codigo)
                    if (data):
                        print(tabulate(data, headers="keys", tablefmt="github"))
                        raise Exception("El codigo de cliente ya existe")
                    else:
                        newClients["codigo_cliente"] = int(codigo)
                else:
                    raise Exception("El codigo de cliente no cumple con el estandar establecido, debe ser un numero")
            #validacion nombre  
            if(not newClients.get("nombre_cliente")):
                nombre = input("Nombre cliente /ej: GoldFish Garden/: ")
                if(re.match(r'^[A-Z][a-zA-Z]*(?: [A-Z][a-zA-Z]*)?$', nombre) is not None):
                    newClients["nombre_cliente"] = nombre
                else:
                    raise Exception("El nombre del cliente no cumple con el estandar establecido, debe contener la primera letra en mayuscula") 
            #validacion nombre contacto
            if(not newClients.get("nombre_contacto")):
                nombre = input("Nombre(s) contacto /ej: Daniel/: ")
                if(re.match(r'^[A-Z][a-zA-Z]*(?: [A-Z][a-zA-Z]*)?$', nombre) is not None):
                    newClients["nombre_contacto"] = nombre
                else:
                    raise Exception("El nombre de contacto no cumple con el estandar establecido, debe contener la primera letra en mayuscula") 
            #validacion apellido
            if(not newClients.get("apellido_contacto")):
                apellido = input("Apellido(s) /ej: Marin Larrota/: ")
                if(re.match(r'^[A-Z][a-zA-Z]*(?: [A-Z][a-zA-Z]*)?$', apellido) is not None):
                    newClients["apellido_contacto"] = apellido
                else:
                    raise Exception("El apellido de contacto no cumple con el estandar establecido, debe contener la primera letra en mayuscula") 
            #validacion telefono
            if(not newClients.get("telefono")):
                telefono = input("Telefono /ej: 1234567890/: ")
                if(re.match(r'^\d{10}$', telefono) is not None):
                    newClients["telefono"] = telefono        
                else:
                    raise Exception("El telefono del cliente no cumple con el estandar establecido, debe contener 10 numeros")                
            #validacion fax
            if(not newClients.get("fax")):
                fax = input("Fax /ej: 1234567890/: ")
                if(re.match(r'^\d{10}$', fax) is not None):
                    newClients["fax"] = fax        
                else:
                    raise Exception("El fax del cliente no cumple con el estandar establecido, debe contener 10 numeros")
            #validacion linea direccion 1
            if(not newClients.get("linea_direccion1")):
                lineaDir1 = input("Direccion 1 /ej: Calle 1 #34/: ")
                if(re.match(r"^(?=\S{5,}).+$", lineaDir1) is not None):
                    newClients["linea_direccion1"] = lineaDir1
                else:
                    raise Exception("La direccion del cliente no cumple con el estandar establecido, no puede ser vacio")                
            #validacion linea direccion 2
            if(not newClients.get("linea_direccion2")):
                lineaDir2 = input("Direccion 2 /ej: Calle 1 #34/: ")
                if(lineaDir2 != lineaDir1) is not None:
                    newClients["linea_direccion2"] = lineaDir2
                else:
                    raise Exception("La direccion 2 del cliente no puede ser igual que la direccion 2, de no tener dejar vacio")
            #validacion ciudad
            if(not newClients.get("ciudad")):
                ciudad = input("Ciudad /ej: Bucaramanga/: ")
                if(re.match(r'^\D+$', ciudad) is not None):
                    ciudad = ciudad.title()
                    newClients["ciudad"] = ciudad
                else:
                    raise Exception("La ciudad del cliente no cumple con el estandar establecido, no puede ser vacio ni contener numeros")
            #validacion region 
            if(not newClients.get("region")):
                region = input("Region /ej: Santander/: ")
                region = region.title()
                newClients["region"] = region
            #validacion pais
            if(not newClients.get("pais")):
                pais = input("Pais /ej: Colombia/: ")
                if(re.match(r'^\D+$', pais) is not None):
                    pais = pais.title()
                    newClients["pais"] = pais
                else:
                    raise Exception("El pais del cliente no cumple con el estandar establecido, no puedo ser vacio ni contener numeros")
            #validacion codigo postal
            if(not newClients.get("codigo_postal")):
                codigoPostal = input("Codigo postal /ej: 170435/: ")
                if(re.match(r"^[^a-zA-Z]+$", codigoPostal) is not None):
                    newClients["codigo_postal"] = codigoPostal
                else:
                    raise Exception("El codigo postal del cliente no cumple con el estandar establecido, debe contener solo numeros")
            #validacion codigo empleado rep ventas
            if(not newClients.get("codigo_empleado_rep_ventas")):
                codigoEmpleadoRepVentas = input("Codigo empleado representane de ventas /ej: 19/: ")
                if(re.match(r"^[^a-zA-Z]+$", codigoEmpleadoRepVentas) is not None):
                    newClients["codigo_empleado_rep_ventas"] = int(codigoEmpleadoRepVentas)
                else:
                    raise Exception("El codigo empleado rep de ventas del cliente no cumple con el estandar establecido, debe contener solo numeros")
            #validacion limite credito
            if(not newClients.get("limite_credito")):
                limiteCredito = input("Limite de credito /ej: 3000/: ")
                if(re.match(r"^[^a-zA-Z]+$", limiteCredito) is not None):
                    newClients["limite_credito"] = int(limiteCredito)
                else:
                    raise Exception("El limite de credito del cliente no cumple con el estandar establecido, debe contener solo numeros")

            peticion = requests.post("http://154.38.171.54:5001/cliente", data=json.dumps(newClients))
            res = peticion.json()
            res["Mensaje"] = "Empleado guardado"
            return [res]
            # LOCAL                    
            # peticion = requests.post("http://192.168.1.39:5502", data=json.dumps(newClients))
            # res = peticion.json()
            # res["Mensaje"] = "Empleado guardado"
            # return [res]
        
        except Exception as error:
            print(error)      

def deleteClient():
    print(tabulate(gCli.getAllData(),headers="keys", tablefmt="github"))
    id = input("Ingrese el id que desea eliminar: ")
    data = gCli.getIdOffice(id)
    if(len(data)):
        peticion = requests.delete(f"http://154.38.171.54:5001/cliente/{id}")
        if(peticion.status_code == 204 or peticion.status_code == 200):
            return("Cliente eliminado correctamente")
        else:
            return peticion.status_code
    else:
        return("Cliente no encontrado")
                
def menu():
    flag = 1
    while flag == 1:
        os.system("cls")
        print(f"""
            --- Administrar datos de cliente ---
            
            1. Guardar un cliente nuevo
            2. Eliminar cliente
            0. Atras
            """)
        
        op = input("Seleccione una opcion: ")
        
        if op == "1":
            print(tabulate(postEmpleado(),headers="keys", tablefmt="github"))
            input("Oprima una tecla para ingresar nueva opcion....")
        elif op == "2":
            print(deleteClient())
            input("Oprima una tecla para ingresar nueva opcion....")
        elif op == "0":
            flag = 0    
        else:
            print("No es una opcion valida") 