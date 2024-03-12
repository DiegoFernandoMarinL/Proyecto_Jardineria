from tabulate import tabulate 
import storage.oficina as of

def getOfficeCity(pais):
    cityOffice = []
    for val in of.oficina:
        if (val.get("pais") == pais):
            ciudadOficina = ({
                "ciudad": val.get('ciudad'),
                "oficina": val.get('codigo_oficina')
            })
            cityOffice.append(ciudadOficina)
    return cityOffice        

def getcityTel(pais):
    cityOffice = []
    for val in of.oficina:
        if (val.get("pais") == pais):
            ciudadOficina = ({
                "ciudad": val.get('ciudad'),
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
            2. Obetner ...
            0. Menu principal  
            """)
        
        op = input("Seleccione una opcion: ")
        
        if op == "1":
            pais = input("Pais: ")
            print(tabulate(getOfficeCity(pais),headers="keys",tablefmt="github"))
            flag = int(input("Desea realizar otra consulta: 1=Si  0=No: ")) 
        elif op == "2":
            pais = input("Pais: ")
            print(tabulate(getcityTel(pais),headers="keys",tablefmt="github"))
            flag = int(input("Desea realizar otra consulta: 1=Si  0=No: "))
        elif op == "0":
            return
