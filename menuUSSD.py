saldo = 100.0

def ussd_menu():
    global saldo
    
    menu_text = "Bienvenido al menú USSD.\n"
    menu_text += "1. Ver saldo\n"
    menu_text += "2. Recargar saldo\n"
    menu_text += "3. Salir \n"

    while True:
        try:
            user_response = input(menu_text)

            if user_response == "1":
                saldo_text = f"Su saldo es ${saldo}\n"
                print(saldo_text)
            elif user_response == "2":
                recarga_text = "Ingrese el monto a recargar: "
                monto = float(input(recarga_text))
                saldo += monto
                respuesta_text = f"Recarga exitosa de ${monto}. Saldo actual: ${saldo}\n"
                print(respuesta_text)
            elif user_response == "3":
                print("¡Gracias por utilizar nuestro servicio USSD!\n")
                break
            else:
                print("Opción inválida. Por favor, seleccione una opción válida.\n")
        except ValueError:
            print("Error: Ingrese un valor numérico para la recarga.\n")
        except KeyboardInterrupt:
            print("Se ha interrumpido la ejecución.\n")
            break

if __name__ == '__main__':
    ussd_menu()
