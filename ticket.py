import random


tickets = {}


def generar_ticket():
    while True:  
        print("\n--- Generar un Nuevo Ticket ---")
        nombre = input("Ingrese su Nombre: ")
        sector = input("Ingrese su Sector: ")
        asunto = input("Ingrese el Asunto: ")
        mensaje = input("Ingrese un Mensaje: ")

    
        numero_ticket = random.randint(1000, 9999)

      
        tickets[numero_ticket] = {
            "Nombre": nombre,
            "Sector": sector,
            "Asunto": asunto,
            "Mensaje": mensaje,
        }

        print("\n¡Ticket generado!")
        print("===============================")
        print(f"Nombre: {nombre}")
        print(f"Número de Ticket: {numero_ticket}")
        print(f"Sector: {sector}")
        print(f"Asunto: {asunto}")
        print(f"Mensaje: {mensaje}")
        print("===============================")
        print("Recuerde su número de ticket para futuras consultas.")

      
        respuesta = input("¿Desea generar otro ticket? (s/n): ").strip().lower()
        if respuesta != 's':  
            break


def leer_ticket():
    while True:  
        print("\n--- Leer un Ticket ---")
        try:
            
            numero_ticket = int(input("Ingrese el número de Ticket: "))

            if numero_ticket in tickets:
                print("\n¡Ticket encontrado!")
                print("===============================")
                print(f"Número de Ticket: {numero_ticket}")
                print(f"Nombre: {tickets[numero_ticket]['Nombre']}")
                print(f"Sector: {tickets[numero_ticket]['Sector']}")
                print(f"Asunto: {tickets[numero_ticket]['Asunto']}")
                print(f"Mensaje: {tickets[numero_ticket]['Mensaje']}")
                print("===============================")
            else:
                print("\nEl ticket no existe. Intente con otro número.")
        except ValueError:
           
            print("\nPor favor, ingrese un número válido.")

       
        respuesta = input("¿Desea leer otro ticket? (s/n): ").strip().lower()
        if respuesta != 's':  
            break


def menu_principal():
    while True: 
        print("\n--- Menú Principal ---")
        print("1 - Generar un Nuevo Ticket")
        print("2 - Leer un Ticket")
        print("3 - Salir")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == '1':
            generar_ticket()
        elif opcion == '2':
            leer_ticket()
        elif opcion == '3':
            confirmar = input("¿Está seguro que desea salir? (s/n): ").strip().lower()
            if confirmar == 's':
                print("\nGracias por usar el sistema de tickets. ¡Adiós!")
                break  
        else:
          
            print("\nOpción no válida. Intente nuevamente.")


menu_principal()
