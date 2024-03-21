import os
import re
import json
import requests
import modules.getEmployee as gEmpl
from tabulate import tabulate

def postEmpleado():
    newEmpleado = dict()
    while True:
        try: 
            #Validacion codigo empleado
            if(not newEmpleado.get("codigo_empleado")):
                codigo = input("Codigo de empleado /ej: 37/: ")
                if(re.match(r'^[0-9]+$', codigo) is not None):
                    data = gEmpl.getEmployeeCodigo(codigo)
                    if (data):
                        print(tabulate(data, headers="keys", tablefmt="github"))
                        raise Exception("El codigo de empleado ya existe")
                    else:
                        newEmpleado["codigo_empleado"] = int(codigo)
                else:
                    raise Exception("El codigo de empleado no cumple con el estandar establecido, debe ser un numero")
            #validacion nombre empleado    
            if(not newEmpleado.get("nombre")):
                nombre = input("Nombre(s) empleado /ej: Diego Fernando/: ")
                if(re.match(r'^[A-Z][a-zA-Z]*(?: [A-Z][a-zA-Z]*)?$', nombre) is not None):
                    newEmpleado["nombre"] = nombre
                else:
                    raise Exception("El nombre del empleado no cumple con el estandar establecido, debe contener la primera letra en mayuscula") 
            #validacion primer apellido
            if(not newEmpleado.get("apellido1")):
                apellido1 = input("Primer apellido /ej: Marin Larrota/: ")
                if(re.match(r'^[A-Z][a-zA-Z]*(?: [A-Z][a-zA-Z]*)?$', apellido1) is not None):
                    newEmpleado["apellido1"] = apellido1
                else:
                    raise Exception("El apellido del empleado no cumple con el estandar establecido, debe contener la primera letra en mayuscula") 
            #validacion segundo apellido    
            if(not newEmpleado.get("apellido2")):
                apellido2 = input("Segundo apellido /ej: Marin Larrota/: ")
                if(re.match(r'^(?:[A-Z][a-zA-Z]*(?: [A-Z][a-zA-Z]*)?)?$', apellido2) is not None):
                    newEmpleado["apellido2"] = apellido2
                else:
                    raise Exception("El apellido del empleado no cumple con el estandar establecido, debe contener la primera letra en mayuscula")     
            #validacion extension
            if(not newEmpleado.get("extension")):
                ext = input("Extension /ej: 1234/: ")
                if(re.match(r'^\d{4}$', ext) is not None):
                    data = gEmpl.getEmployeeExtension(ext)
                    if (data):
                        print(tabulate(data, headers="keys", tablefmt="github"))
                        raise Exception("La extension de empleado ya existe")
                    else:
                        newEmpleado["extension"] = ext
                else:
                    raise Exception("La extension del empleado no cumple con el estandar establecido, debe contener 4 numeros")                
            #validacion email
            if(not newEmpleado.get("email")):
                email = input("Email /ej: correo@gmail.com/: ")
                if(re.match(r'.*@.*', email) is not None):
                    data = gEmpl.getEmployeeEmail(email)
                    if (data):
                        print(tabulate(data, headers="keys", tablefmt="github"))
                        raise Exception("El email del empleado ya existe")
                    else:
                        newEmpleado["email"] = email
                else:
                    raise Exception("El email del empleado no cumple con el estandar establecido, debe contener @")                
            #validacion codigo oficina
            if(not newEmpleado.get("codigo_oficina")):
                codigoOficina = input("Codigo oficina /ej: ABC-DE/: ")
                if(re.match(r'^[A-Z]{3}-[A-Z]{2}$', codigoOficina) is not None):
                    newEmpleado["codigo_oficina"] = codigoOficina
                else:
                    raise Exception("El codigo de oficina del empleado no cumple con el estandar establecido, debe contener cumplir el formato ABC_DE")                
            #validacion codigo jefe
            if(not newEmpleado.get("codigo_jefe")):
                codigoJefe = input("Codigo jefe /ej: 23/: ")
                if(re.match(r'^[0-9]+$', codigoJefe) is not None):
                    newEmpleado["codigo_jefe"] = int(codigoJefe)
                else:
                    raise Exception("El codigo de oficina del empleado no cumple con el estandar establecido, debe ser un numero")
            #validacion puesto
            if(not newEmpleado.get("puesto")):
                puesto = input("Puesto o cargo /ej: Ingeniero/: ")
                if(re.match(r'^\D*$', puesto) is not None):
                    newEmpleado["puesto"] = puesto
                else:
                    raise Exception("El codigo de oficina del empleado no cumple con el estandar establecido, no puede tener numeros")
            
            peticion = requests.post("http://192.168.1.39:5501", data=json.dumps(newEmpleado))
            res = peticion.json()
            res["Mensaje"] = "Empleado guardado"
            return [res]
        
        except Exception as error:
            print(error)      
            
def deleteEmployee():
    print(tabulate(gEmpl.getAllData(),headers="keys", tablefmt="github"))
    id = input("Ingrese el id que desea eliminar: ")
    data = gEmpl.getIdEmployee(id)
    if(len(data)):
        peticion = requests.delete(f"http://192.168.1.39:5501/{id}")
        if(peticion.status_code == 204):
            return("Empleado eliminado correctamente")
        else:
            return peticion.status_code
    else:
        return("Empleado no encontrado")
    
def menu():
    flag = 1
    while flag == 1:
        os.system("cls")
        print(f"""
            --- Administrar datos de empleado ---
            
            1. Guardar empleado nuevo
            2. Eliminar empleado
            0. Atras
            """)
        
        op = input("Seleccione una opcion: ")
        
        if op == "1":
            print(tabulate(postEmpleado(),headers="keys", tablefmt="github"))
            input("Oprima una tecla para ingresar nueva opcion....")
        elif op == "2":
            print(deleteEmployee())
            input("Oprima una tecla para ingresar nueva opcion....")    
        elif op == "0":
            flag = 0    
        else:
            print("No es una opcion valida") 