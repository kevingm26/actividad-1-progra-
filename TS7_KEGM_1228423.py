
#Trabajo supervisado de introduccion a la programacion 
#21/09/2023
#Kevin Eduardo Garcia Miralda
#Objetivo: hacer que nos de la multiplicacion de cada numero 
# Muestra tu nombre completo
print("Mi nombre completo es: [Kevin Eduardo Garcia Miralda]")

while True:
 
    while True:
        try:
            numero = int(input("Ingresa un número entre 1 y 10: "))
            if 1 <= numero <= 10:
                break
            else:
                print("El número debe estar en el rango de 1 a 10.")
        except ValueError:
            print("Entrada no válida. Ingresa un número válido.")

    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} X {i} = {resultado}")

    opcion = input("¿Deseas generar la tabla de otro número? (SALIR para terminar): ").upper()
    if opcion != "SALIR":
        continue
    else:
        break
