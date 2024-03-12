import modules.getClients as cliente
import modules.getOffice as office
import modules.getEmployee as employee
import modules.getOrder as order

if (__name__=="__main__"):
    flag = 1
    while flag == 1:
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
            cliente.menu()
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
                     


