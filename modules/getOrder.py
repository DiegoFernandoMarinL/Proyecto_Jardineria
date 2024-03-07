from datetime import datetime
import storage.pedido as ord

def getState():
    estado = []
    for val in ord.pedido:
        if (val.get("estado") not in estado):
            estado.append({
                "estado": val.get("estado")    
            })
    return estado        

#-------------------
def getAllOrderEntregadosAtrasados():
    pedidosEntregados = []
    for val in ord.pedido:
        if val.get("estado") == "Entregado" and val.get("fecha_entrega") is None:
            val["fecha_entrega"] = val.get("fecha_esperada")
        if val.get("estado") == "Entregado":
            date_1 = val.get("fecha_entrega")
            date_2 = val.get("fecha_esperada")
            start = datetime.strptime(date_1, "%Y-%m-%d")
            end = datetime.strptime(date_2, "%Y-%m-%d")
            diff = end.date() - start.date()
            if (diff.days < 0):
                pedidosEntregados.append({
                    "codigo_de_pedido": val.get("codigo_pedido"),  
                    "codigo_de_cliente": val.get("codigo_cliente"),
                    "fecha_esperada": val.get("fecha_esperada"),
                    "fecha_de_entrega": val.get("fecha_entrega") 
                })
    return pedidosEntregados    

def getAllOrderEntregadosDosDiasAntes():
    pedidosEntregados = []
    for val in ord.pedido:
        if val.get("estado") == "Entregado" and val.get("fecha_entrega") is None:
            val["fecha_entrega"] = val.get("fecha_esperada")
        if val.get("estado") == "Entregado":
            date_1 = val.get("fecha_entrega")
            date_2 = val.get("fecha_esperada")
            start = datetime.strptime(date_1, "%Y-%m-%d")
            end = datetime.strptime(date_2, "%Y-%m-%d")
            diff = end.date() - start.date()
            if (diff.days >= 2):
                pedidosEntregados.append({
                    "codigo_de_pedido": val.get("codigo_pedido"),  
                    "codigo_de_cliente": val.get("codigo_cliente"),
                    "fecha_esperada": val.get("fecha_esperada"),
                    "fecha_de_entrega": val.get("fecha_entrega") 
                })
    return pedidosEntregados    

def getAllRechazados2009():
    pedidos = []
    for val in ord.pedido:
        if val.get("estado") == "Rechazado":
            date_1 = val.get("fecha_pedido")
            date_1 = datetime.strptime(date_1, "%Y-%m-%d")
            if (date_1.year == 2009):
                pedidos.append(val)
    return pedidos            