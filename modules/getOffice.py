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