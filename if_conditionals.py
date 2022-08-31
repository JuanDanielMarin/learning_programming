'''
pedir notas
calcular promedio
si prom > 6 entonces
    apruebo
sino
    repruebo
'''
nota1 = int(input('Introduzca su primera nota: '))
nota2 = int(input('Introduzca su segunda nota: '))
nota3 = int(input('Introduzca su tercera nota: '))

prom = (nota1 + nota2 + nota3)/3
print(f'El promedio de notas es: {prom}')

if(prom >= 6):
     print('Usted está APROBADO')
else:
    print('Usted está REPROBADO')