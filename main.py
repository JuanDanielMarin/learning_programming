# saludo = 'Hola'
# nombre = 'Juan'

# print(f'{saludo} {nombre}')

# #Funciones
# salida = input('Ingrese su nombre:')

# num1 = int(input('Ingrese el numero 1:')) #Casteo. Input devuelve por default un string.
# num2 = int(input('Ingrese el numero 2:'))
# print(num1 + num2)

'''
pedir promedio por input
si prom > 6 entonces
    apruebo
sino
    repruebo
'''

# prom = int(input('Introduzca su promedio '))

# if(prom >= 6):
#     print('Usted está Aprobado')
# else:
#     print('Ustes está Reprobado')

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

