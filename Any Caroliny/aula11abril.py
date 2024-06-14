numeros = [5, 2, 8, 1, 9]
print(max(numeros))

print(max(10, 20, 30))

numeros = [5, 16, 23, 1942, 56]
print(max(numeros))


numeros = [5, 2, 8, 1, 9]
print(min(numeros))

print(min(10, 20, 30))


lista = [False, True, False]
print(any(lista))

lista_vazia = []
print(any(lista_vazia))


lista = [True, True, True]
print(all(lista))

lista = [True, False, True]
print(all(lista))

texto = "Olá, mundo!"
print(len(texto))

texto = "Meu cachorro cagou no pátio"
print(len(texto))

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(len(lista))


dicionario = dict(nome="Any", idade=22)
print(dicionario)

print(abs(-5))
print(abs(3.14))

print(bin(5))
print(bin(10))

print(bin(156))
print(bin(69992438915))


def quadrado(numero):
    return numero ** 2

numeros = [1, 2, 3, 4, 5]
quadrados = map(quadrado, numeros)
print(list(quadrados))

def quadrado(numero):
    return numero ** 3

numeros = [6, 8, 9, 4, 16]
quadrados = map(quadrado, numeros)
print(list(quadrados))