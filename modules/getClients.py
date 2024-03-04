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