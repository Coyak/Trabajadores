import csv
#Registrar Trabajador
def RegistrarTrabajador():
    nombre=input("ingrese nombre y apellido del trabajador: ")
    cargo=input("ingrese cargo del trabajador: ")
    sueldo=int(input("ingrese Sueldo Bruto del trabajador: "))
    with open('trabajadores.csv', 'a', newline='\n') as archivo_csv:
        escritor_csv = csv.writer(archivo_csv)
        escritor_csv.writerow([nombre,cargo,sueldo])
    print("\nTrabajador registrado exitosamente :)")
#listado de trabajadores
def ListadoTrabajadores():
    with open('trabajadores.csv', mode='r', newline='',encoding='Utf-8') as archivo_csv:
        lector_csv = csv.DictReader(archivo_csv)
        print("Listado de todos los trabajadores\n")
        for fila in lector_csv:
            print(fila['Trabajador'])
