
alumnos = {}
datos_alumno = {}

def mostrar_lista():
    print("Lista de alumnos")
    for nombre in alumnos:
        print(nombre)

while True:

    ingresar = input("Ingresar el nombre del alumno (* para salir) ")

    if ingresar == "*":
        break

    elif ingresar.lower() == "+":
        mostrar_lista()

    else:

        nombre = ingresar

        if nombre in alumnos:
            print(f"{nombre} ya esta en la lista de alumnos")
        else:
            apellido = input("Ingresar el apellido: ")
            dni = input("ingresar el DNI: ")
            fecha_de_nacimiento = input("Ingresar la fecha de nacimiento: ")
            tutor = input("Ingresar el tutor: ")
            notas = input("Ingresar notas del alumno: ")
            faltas = input("Ingresar faltas: ")
            amonestaciones = input("Igresar amonestaciones: ")

            alumnos[nombre] = nombre

            datos_alumno[nombre] = {
                "Apellido" : apellido,
                "DNI" : dni,
                "Fecha de nacimiento" : fecha_de_nacimiento,
                "Tutor" : tutor,
                "Notas" : notas,
                "Faltas" : faltas,
                "Amonestaciones" : amonestaciones
            }
        print(f"{nombre} ha sido agregado a la lista Alumnos")

for nombre, datos in datos_alumno.items():
    print(f"Nombre: {nombre}")
    for clave, valor in datos.items():
        print(f"{clave}: {valor}")