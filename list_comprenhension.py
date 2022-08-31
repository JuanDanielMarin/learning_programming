import random

alumnos=[]
for i in range(30):
    notas = [random.randint(1,10) for i in range(3)]
    alumnos.append(notas)
else:
    print(f'Las notas se han cargado exitosamente')

promedios = []
for i in range(30):
    notas = alumnos[i]
    suma = 0
    for nota in notas:
        suma = nota + suma
        prom = round((suma / 3),2)
        promedios.append(prom)

print(promedios)