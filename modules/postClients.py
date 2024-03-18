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
                    raise Exception("El codigo de empleado no cumple con el estandar establecido, debe ser un numero")
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
                    raise Exception("El apellido del empleado no cumple con el estandar establecido, debe contener la primera letra en mayuscula") 
            #validacion telefono
            if(not newClients.get("telefono")):
                telefono = input("Telefono /ej: 1234567890/: ")
                if(re.match(r'^\d{10}$', telefono) is not None):
                    data = gCli.getEmployeeExtension(telefono)
                    if (data):
                        print(tabulate(data, headers="keys", tablefmt="github"))
                        raise Exception("La extension de empleado ya existe")
                    else:
                        newClients["extension"] = ext
                else:
                    raise Exception("La extension del empleado no cumple con el estandar establecido, debe contener 4 numeros")                
             #validacion email
            if(not newClients.get("email")):
                email = input("Email /ej: correo@gmail.com/: ")
                if(re.match(r'.*@.*', email) is not None):
                    data = gEmpl.getEmployeeEmail(email)
                    if (data):
                        print(tabulate(data, headers="keys", tablefmt="github"))
                        raise Exception("El email del empleado ya existe")
                    else:
                        newClients["email"] = email
                else:
                    raise Exception("El email del empleado no cumple con el estandar establecido, debe contener @")                
            #validacion codigo oficina
            if(not newClients.get("codigo_oficina")):
                codigoOficina = input("Codigo oficina /ej: ABC-DE/: ")
                if(re.match(r'^[A-Z]{3}-[A-Z]{2}$', codigoOficina) is not None):
                    newClients["codigo_oficina"] = codigoOficina
                else:
                    raise Exception("El codigo de oficina del empleado no cumple con el estandar establecido, debe contener cumplir el formato ABC_DE")                
            #validacion codigo jefe
            if(not newClients.get("codigo_jefe")):
                codigoJefe = input("Codigo jefe /ej: 23/: ")
                if(re.match(r'^[0-9]+$', codigoJefe) is not None):
                    newClients["codigo_jefe"] = int(codigoJefe)
                else:
                    raise Exception("El codigo de oficina del empleado no cumple con el estandar establecido, debe ser un numero")
            #validacion puesto
            if(not newClients.get("puesto")):
                puesto = input("Puesto o cargo /ej: Ingeniero/: ")
                if(re.match(r'^\D*$', puesto) is not None):
                    newClients["puesto"] = puesto
                else:
                    raise Exception("El codigo de oficina del empleado no cumple con el estandar establecido, no puede tener numeros")
            
            peticion = requests.post("http://172.16.100.132:5501", data=json.dumps(newClients))
            res = peticion.json()
            res["Mensaje"] = "Empleado guardado"
            return [res]
        
        except Exception as error:
            print(error)      
            
def menu():
    flag = 1
    while flag == 1:
        os.system("cls")
        print(f"""
            --- Administrar datos de empleado ---
            
            1. Guardar un cliente nuevo
            0. Atras
            """)
        
        op = input("Seleccione una opcion: ")
        
        if op == "1":
            print(tabulate(postEmpleado(),headers="keys", tablefmt="github"))
            input("Oprima una tecla para ingresar nueva opcion....")
        elif op == "0":
            flag = 0    
        else:
            print("No es una opcion valida") 