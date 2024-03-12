from tabulate import tabulate
import storage.cliente as cli

def getAllClienteName():
    clienteName = list()
    for val in cli.cliente:
        codigoName = ({
            "codigo_cliente": val.get('codigo_cliente'),
            "nombre_cliente": val.get('nombre_cliente')
        })
        clienteName.append(codigoName)
    return clienteName        

def getOneClienteCodigo(codigo):
    client= list()
    for val in cli.cliente:
        if (val.get("codigo_cliente") == codigo):
            client.append({
                "codigo_cliente": val.get('codigo_cliente'),
                "nombre_cliente": val.get('nombre_cliente')
            })
    return client        
        
def getClientCredito(Credito):
    client = list()
    for val in cli.cliente:
        if (val.get("limite_credito") >= Credito):
             client.append({
                "codigo_cliente": val.get('codigo_cliente'),
                "nombre_cliente": val.get('nombre_cliente'),
                "pais": val.get('pais'),
                "ciudad": val.get('ciudad'),
                "region": val.get('region'), 
                "limite_credito": val.get('limite_credito')
             })
    return client

def getClientPaisCiudadRegion(pais, ciudad, region):
    client = list()
    for val in cli.cliente:
        if (val.get("pais") == pais and val.get("ciudad") == ciudad and val.get("region") == region):
            client.append({
                "codigo_cliente": val.get('codigo_cliente'),
                "nombre_cliente": val.get('nombre_cliente'),
                "pais": val.get('pais'),
                "ciudad": val.get('ciudad'),
                "region": val.get('region')
            })

    return client 

def getClientPaisCredito(pais, credito):  
    clienteCompleto = list()
    for val in cli.cliente:
        if (val.get("pais") == pais and val.get("limite_credito") >= credito):
            clienteCompleto.append({
                "codigo_cliente": val.get('codigo_cliente'),
                "nombre_cliente": val.get('nombre_cliente'),
                "pais": val.get('pais'),
                "limite_credito": val.get('limite_credito')
            })
    return clienteCompleto        

def getClientNameLetter(letraInicial):
    clienteName = list()
    for val in cli.cliente:
        nombreDataDividido = list(val.get("nombre_cliente"))
        if (nombreDataDividido[0] == letraInicial):
            codigoName = ({
                "codigo_cliente": val.get('codigo_cliente'),
                "nombre_cliente": val.get('nombre_cliente')
            })
            clienteName.append(codigoName)
        nombreDataDividido = ""
    return clienteName 

def getCountry(pais):
    clientePais = list()
    for i, val in enumerate(cli.cliente):
        if (val.get("pais") == pais):
            clientePais.append({
                "clave": i,
                "nombre": val.get("nombre_cliente"),
                "pais": val.get("pais")
            })
    return clientePais       

def menu():
    flag=1
    while flag == 1:
        print(f"""
            --- Reportes ---
            
            1. Obtener todos los clientes codigo y nombre
            2. Obtener cliente por codigo
            3. Obtener clientes por limite de credito
            4. Obtener clientes por pais ciudad region
            5. Obtener clientes por pais limite de credito
            6. Obtener clientes por letra inicial
            7. Obtener clientes por pais
            0. Menu Principal 
            """)
        
        op = input("Seleccione una opcion: ")
    
        if op == "1":
            print(tabulate(getAllClienteName(),headers="keys",tablefmt="github"))
            flag = int(input("Desea realizar otra consulta: 1=Si  0=No: "))
        elif op == "2":
            codigo = int(input("Digite el codigo del cliente: "))
            print(tabulate(getOneClienteCodigo(codigo),headers="keys",tablefmt="github"))
            flag = int(input("Desea realizar otra consulta: 1=Si  0=No: "))
        elif op == "3":
            credito = int(input("Digite limite de credito: "))
            print(tabulate(getClientCredito(credito),headers="keys",tablefmt="github"))
            flag = int(input("Desea realizar otra consulta: 1=Si  0=No: ")) 
        elif op == "4":
            pais = input("Pais: ")
            ciudad = input("Ciudad: ")
            region = input("Region: ")
            print(tabulate(getClientPaisCiudadRegion(pais,ciudad,region),headers="keys",tablefmt="github")) 
            flag = int(input("Desea realizar otra consulta: 1=Si  0=No: "))
        elif op == "5":
            pais = input("Pais: ")
            credito = int(input("Digite limite de credito: "))
            print(tabulate(getClientPaisCredito(pais,credito),headers="keys",tablefmt="github"))
            flag = int(input("Desea realizar otra consulta: 1=Si  0=No: "))
        elif op == "6":
            letra = input("Escriba letra a buscar: ")
            print(tabulate(getClientNameLetter(letra),headers="keys",tablefmt="github"))
            flag = int(input("Desea realizar otra consulta: 1=Si  0=No: ")) 
        elif op == "7":
            pais = input("Pais: ")
            print(tabulate(getCountry(pais),headers="keys",tablefmt="github"))
            flag = int(input("Desea realizar otra consulta: 1=Si  0=No: ")) 
        elif op == "0":
            return

    
