import csv
import funciones as fun
flag=True
#Login
nombre="guest"
passw="1234"
print("Inicio de secion\n")
user_login=input("Ingrese usuario: ".lower())
user_passw=input("Ingrese contraseña: ")
if user_login == nombre and user_passw == passw:
#Menu
    while flag == True:
        print("\n¿Que accion desea realizar?\n1.-Registrar Trabajador\n2.-Listar los todos los trabajadores\n3.-Imprimir planilla de sueldos\n4.-Salir del Programa")
        opc=int(input("Elija una opcion:"))
        if opc == 1:
            print("Resgistrar trabajador")
            fun.RegistrarTrabajador()
        elif opc == 2:
            fun.ListadoTrabajadores()
        elif opc == 3:
            print("Plantilla de sueldos")
        elif opc == 4:
            print("Saliendo del programa...")
            break
else:
    print("usuario o/y contraseña incorrectos...\nVuelva interntarlo")