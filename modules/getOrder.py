import storage.pedido as ord

def getState():
    estado = []
    for val in ord.pedido:
        if (val.get("estado") not in estado):
            estado.append({
                "estado": val.get("estado")    
            })
    return estado        

