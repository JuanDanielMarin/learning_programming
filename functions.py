import random

def get_stats():
    dados = [random.randint(1,6) for i in range(4)]
    dados.sort()
    max_dados = dados[1:]
    return sum(max_dados)

stats = {
    'str': get_stats(),
    'des': get_stats(),
    'int': get_stats(),
    'sab': get_stats(),
    'con': get_stats()
}

print(stats)

def argumentos(*args):
    print(args)

argumentos('Hola', 2, True)

def kwargumentos(**kwargs):
    print(kwargs)

kwargumentos(nombre="Juan", edad=5)