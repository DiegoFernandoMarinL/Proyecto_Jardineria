from tabulate import tabulate
import modules.getClients as cliente
import modules.getOffice as office
import modules.getEmployee as employee
import modules.getOrder as order

#print(cliente.getClientCredito(3000))

#head = ["Codigo", "Nombre" ,"",""]
#headers=head
#print(tabulate(cliente.getClientPaisCredito("Spain", 50000), tablefmt="grid"))
#letraInicial = input("Escriba nombre a buscar: ")
print(tabulate(order.getState(), tablefmt="grid"))
