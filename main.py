from tabulate import tabulate
import modules.getClients as cliente

print(cliente.getOneClienteCodigo(3))
#head = ["Codigo", "Nombre","",""]
#headers=head
print(tabulate(cliente.getOneClienteCodigo("3"), tablefmt="grid"))
