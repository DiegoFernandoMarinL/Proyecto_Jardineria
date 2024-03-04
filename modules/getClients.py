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

