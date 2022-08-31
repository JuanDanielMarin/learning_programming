nota = int(input('Introduzca su nota: '))

prom = 0
cant = 0

while(nota !=0):
    if (nota >= 1 and nota <= 10):
        prom = prom + nota
        cant = cant + 1
        nota = int(input('Introduzca su nota: '))
    else:
        nota = int(input('La nota está fuera de rango, por favor introduzca una nota entre 1 y 10 (Presione 0 para salir: '))

prom_final = round((prom/cant),2)
print(f'El promedio final de las {cant} notas es {prom_final}')
