from tabulate import tabulate
import modules.getClients as cliente

#print(cliente.getClientCredito(3000))

#head = ["Codigo", "Nombre","",""]
#headers=head
#print(tabulate(cliente.getClientPaisCredito("Spain", 50000), tablefmt="grid"))
letraInicial = input("Escriba nombre a buscar: ")
print(tabulate(cliente.getClientName(letraInicial), tablefmt="grid"))
