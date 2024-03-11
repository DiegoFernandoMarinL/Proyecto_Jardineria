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
    for val in cli.cliente:
        if (val.get("codigo_cliente") == codigo):
            return {
                "codigo_cliente": val.get('codigo_cliente'),
                "nombre_cliente": val.get('nombre_cliente')
            }
        
def getClientCredito(Credito):
    clienteCompleto = list()
    for val in cli.cliente:
        if (val.get("limite_credito") >= Credito):
             clienteCompleto.append(val)
    return clienteCompleto

def getClientPaisCiudadRegion(pais, ciudad, region):
    clienteCompleto = list()
    for val in cli.cliente:
        if (val.get("pais") == pais and val.get("ciudad") == ciudad and val.get("region") == region):
            clienteCompleto.append(val)
    return clienteCompleto  

def getClientPaisCredito(pais, credito):  
    clienteCompleto = list()
    for val in cli.cliente:
        if (val.get("pais") == pais and val.get("limite_credito") >= credito):
            clienteCompleto.append(val)
    return clienteCompleto        

def getClientName(letraInicial):
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
    clientePais = []
    for i, val in enumerate(cli.cliente):
        if (val.get("pais") == pais):
            clientePais.append({
                "clave": i,
                "nombre": val.get("nombre_cliente"),
                "pais": val.get("pais")
            })
    return clientePais       

def menu():
    print(f"""
        
        --- Menu Principal ---
        
        1. Obtener todos los clientes codigo y nombre
        2. Obtener cliente por codigo
        3. Obtener clientes por limite de credito
        4. Obtener clientes por pais ciudad region
        5. Obtener clientes por pais limite de credito
        6. Obtener clientes por letra inicial
        7. Obtener clientes por pais
        """)
    
    op = input("Seleccione una opcion: ")
    
    if op == "1":
        print(tabulate(getAllClienteName(),headers="keys",tablefmt="github"))
    elif op == "2":
        codigo = int(input("Digite el codigo del cliente: "))
        print(tabulate(getOneClienteCodigo(codigo),headers="keys",tablefmt="github"))
    elif op == "3":
        credito = int(input("Digite limete de credito: "))
        print(tabulate(getClientCredito(credito),headers="keys",tablefmt="github")) 
    elif op == "4":
        pais = input("Pais: ")
        ciudad = input("Ciudad: ")
        region = input("Region: ")
        print(tabulate(getClientPaisCiudadRegion(pais,ciudad,region),headers="keys",tablefmt="github")) 
    elif op == "5":
        print(tabulate(getClientPaisCredito(),headers="keys",tablefmt="github"))
    elif op == "6":
        print(tabulate(getClientName(),headers="keys",tablefmt="github")) 
    elif op == "7":
        print(tabulate(getCountry(),headers="keys",tablefmt="github")) 
                                 