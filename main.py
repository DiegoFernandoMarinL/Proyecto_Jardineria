import os
import modules.getClients as cliente
import modules.getOffice as office
import modules.getEmployee as employee
import modules.getOrder as order
i

def menuCliente():
    flag = 1
    while flag == 1:
        os.system("clear")
        print(f"""
            --- Bienvenido al menu de clientes ---
            
            1. Reportes de clientes
            2. Guardar, actualizar y eliminar clientes
            0. Regresar al menu principal
            """)
        
        op = input("Seleccione una opcion: ")
        
        if op == "1":
            cliente.menu()
        elif op == "2":    
            employee.menu()
        elif op == "0":
            flag = 0    
        else:
            print("No es una opcion valida")
    
    
if (__name__=="__main__"):
    flag = 1
    while flag == 1:
        os.system("clear")
        print(f"""
            --- Menu Principal ---
            
            1. Clientes
            2. Empleados
            3. Oficina
            4. Pago
            5. Pedido
            6. Producto
            0. Salir
            """)
        
        op = input("Seleccione una opcion: ")
        
        if op == "1":
            menuCliente()
        elif op == "2":    
            employee.menu()
        elif op == "3":    
            office.menu()
        elif op == "4":  
            print("falta anexar")
            #cliente.menu()  
        elif op == "5":    
            order.menu()
        elif op == "6":    
            print("falta anexar")
            #cliente.menu()
        elif op == "0":
            print("Gracias por utilizar el programa")
            flag = 0    
        else:
            print("No es una opcion valida")
                     


