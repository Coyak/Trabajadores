import csv
def ListadoTrabajadores():
    with open('trabajadores.csv', mode='r', newline='',encoding='Utf-8') as archivo_csv:
        lector_csv = csv.DictReader(archivo_csv)
        print("Listado de todos los trabajadores\n")
        for fila in lector_csv:
            print(fila['Trabajador'])