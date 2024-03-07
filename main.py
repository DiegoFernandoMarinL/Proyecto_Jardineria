from tabulate import tabulate
import modules.getClients as cliente
import modules.getOffice as office
import modules.getEmployee as employee
import modules.getOrder as order


print(tabulate(order.getAllRechazados2009(),tablefmt="grid"))


