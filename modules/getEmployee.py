import storage.empleado as emp

def getCodManager(codigoJefe):
    jefeCod = []
    for val in emp.empleado:
        if (val.get("codigo_jefe") == codigoJefe):
            addEmployee = ({
                "nombre": val.get("nombre"),
                "apellidos": f'{val.get("apellido1")} {val.get("apellido2")}',
                "email": val.get("email")    
            })  
            jefeCod.append(addEmployee)  
    return jefeCod

def getManagerGeneral(codigoJefe):
    jefeCod = []
    for val in emp.empleado:
        if (val.get("codigo_jefe") == codigoJefe):
            jefeCod.append({
                "cargo": val.get("puesto"),
                "nombre": val.get("nombre"),
                "apellidos": f'{val.get("apellido1")} {val.get("apellido2")}',
                "email": val.get("email")     
            })
    return jefeCod

def getPlacework(puesto):
    puestos = []
    for val in emp.empleado:
        if (val.get("puesto") != puesto):
            puestos.append({
                "nombre": val.get("nombre"),
                "apellidos": f'{val.get("apellido1")} {val.get("apellido2")}',
                "cargo": val.get("puesto") 
            })  
    return puestos         
