import os
import modules.getOrder as order
import modules.getOffice as office
import modules.getClients as repoCliente
import modules.postClients as CRUDClient
import modules.getEmployee as repoEmployee
import modules.postEmployee as CRUDEmployee
import modules.getOffice as repoOffice
import modules.postOffice as CRUDOffice

# def menuProducto():
#     flag = 1
#     while flag == 1:
#         os.system("cls")
#         print(f"""
#             --- Bienvenido al menu de producto ---
            
#             1. Reportes de productos
#             2. Guardar, actualizar y eliminar prodcutos
#             0. Regresar al menu principal
#             """)
        
#         op = input("Seleccione una opcion: ")
        
#         if op == "1":
#             repoProduct.menu()
#         elif op == "2":    
#             CRUDProduct.menu()
#         elif op == "0":
#             flag = 0    
#         else:
#             print("No es una opcion valida")
#             input("Oprima una tecla para ingresar nueva opcion....")

def menuOficina():
    flag = 1
    while flag == 1:
        os.system("cls")
        print(f"""
            --- Bienvenido al menu de Oficina ---
            
            1. Reportes de oficinas
            2. Guardar, actualizar y eliminar oficinas
            0. Regresar al menu principal
            """)
        
        op = input("Seleccione una opcion: ")
        
        if op == "1":
            repoOffice.menu()
        elif op == "2":    
            CRUDOffice.menu()
        elif op == "0":
            flag = 0    
        else:
            print("No es una opcion valida")
            input("Oprima una tecla para ingresar nueva opcion....")

def menuEmpleado():
    flag = 1
    while flag == 1:
        os.system("cls")
        print(f"""
            --- Bienvenido al menu de Empleado ---
            
            1. Reportes de empleados
            2. Guardar, actualizar y eliminar empleados
            0. Regresar al menu principal
            """)
        
        op = input("Seleccione una opcion: ")
        
        if op == "1":
            repoEmployee.menu()
        elif op == "2":    
            CRUDEmployee.menu()
        elif op == "0":
            flag = 0    
        else:
            print("No es una opcion valida")
            input("Oprima una tecla para ingresar nueva opcion....")

def menuCliente():
    flag = 1
    while flag == 1:
        os.system("cls")
        print(f"""
            --- Bienvenido al menu de clientes ---
            
            1. Reportes de clientes
            2. Guardar, actualizar y eliminar clientes
            0. Regresar al menu principal
            """)
        
        op = input("Seleccione una opcion: ")
        
        if op == "1":
            repoCliente.menu()
        elif op == "2":    
            CRUDClient.menu()
        elif op == "0":
            flag = 0    
        else:
            print("No es una opcion valida")  
            input("Oprima una tecla para ingresar nueva opcion....")          
    
if (__name__=="__main__"):
    flag = 1
    while flag == 1:
        os.system("cls")
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
            menuEmpleado()
        elif op == "3":    
            menuOficina()
        elif op == "4":  
            print("falta anexar")
            #cliente.menu()  
        elif op == "5":    
            order.menu()
        elif op == "6":   
            menuProducto()
            #cliente.menu()
        elif op == "0":
            print("Gracias por utilizar el programa")
            flag = 0    
        else:
            print("No es una opcion valida")
            input("Oprima una tecla para ingresar nueva opcion....")
                     


