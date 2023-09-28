
# Ts Introduccion a la programacion
#28/09/20223
#Kevin Garcia 1228423
#Objetivos: que los objetivos tengan exito utilizando for y while
                   
# Ejercicio 1: FOR - Mostrar la secuencia de números en un rango de 1 a 25, incrementando de 1 en 1
for i in range(1, 26):
    print(i, end=", ")
print()

# Ejercicio 2: WHILE - Mostrar la secuencia de números en un rango de 1 a 25, incrementando de 1 en 1
i = 1
while i <= 25:
    print(i, end=", ")
    i += 1
print()

# Ejercicio 3: FOR - Mostrar la secuencia de números en un rango de 5 a 50, incrementando de 5 en 5
for i in range(5, 51, 5):
    print(i, end=", ")
print()

# Ejercicio 4: WHILE - Mostrar la secuencia de números en un rango de 5 a 50, incrementando de 5 en 5
i = 5
while i <= 50:
    print(i, end=", ")
    i += 5
print()

# Ejercicio 5: FOR - Mostrar la secuencia de números en un rango de 20 a 0, decrementando de 2 en 2
for i in range(20, -1, -2):
    print(i, end=", ")
print()

# Ejercicio 6: WHILE - Mostrar la secuencia de números en un rango de 20 a 0, decrementando de 2 en 2
i = 20
while i >= 0:
    print(i, end=", ")
    i -= 2
print()
