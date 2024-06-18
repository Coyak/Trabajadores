import csv
#Registrar Trabajador
def RegistrarTrabajador():
    nombre=input("ingrese nombre y apellido del trabajador: ")
    cargo=input("ingrese cargo del trabajador: ")
    sueldo=int(input("ingrese Sueldo Bruto del trabajador: "))
    desAFP=sueldo*0.1
    desSalud=sueldo*0.07
    sueldoLiquido=sueldo-(desAFP+desSalud)
    with open('trabajadores.csv', 'a', newline='\n', encoding='Utf-8') as archivo_csv:
        reg_csv = csv.writer(archivo_csv)
        reg_csv.writerow([nombre,cargo,sueldo,desSalud,desAFP,sueldoLiquido])
    print("\nTrabajador registrado exitosamente :)")
#listado de trabajadores
def ListadoTrabajadores():
    with open('trabajadores.csv', mode='r', newline='',encoding='Utf-8') as archivo_csv:
        Listado = csv.reader(archivo_csv)
        for lista in Listado:
            print(lista,())
#plantilla de sueldos
def PlantillaSueldos():
    with open('plantilla-de-sueldos.txt', 'r') as archivo:
        contenido = archivo.read()
        print("\nPlantilla de sueldos:\n")
        print(contenido)
    archivo.close()
