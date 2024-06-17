import funciones as fun
#ficheros

flag=True

#Login

#Menu
while flag == True:
    print("\n¿Que accion desea realizar?\n1.-Registrar Trabajador\n2.-Listar los todos los trabajadores\n3.-Imprimir planilla de sueldos\n4. Salir del Programa")
    opc=int(input("Elija una opcion:"))
    if opc == 1:
        fun.registrar_trabajadores()
    elif opc == 4:
        break
