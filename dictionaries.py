import random 

nombres = ['Juan', 'Carlos', 'Pedro', 'Marta']

alumnos={}
for nombre in nombres:
    notas = [random.randint(1,10) for i in range(3)]
    alumnos[nombre] = notas

promedios={}
for nombre in nombres:
    notas = alumnos[nombre]
    suma = 0
    for nota in notas:
        suma = nota + suma
        promedios[nombre] = round((suma / 3),2)

print(promedios)