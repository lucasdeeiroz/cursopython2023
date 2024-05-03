# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro.
# def duplicar(numero):
#     return numero * 2


# def triplicar(numero):
#     return numero * 3


# def quadruplicar(numero):
#     return numero * 4

def multiplicador(vezes):
    def numero(numero):
        return numero * (vezes)
    return numero

duplicar = multiplicador(2)
triplicar = multiplicador(3)
quadruplicar = multiplicador(4)

print(duplicar(10))
print(triplicar(7))
print(quadruplicar(5))