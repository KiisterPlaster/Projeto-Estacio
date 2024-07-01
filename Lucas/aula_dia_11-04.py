numeros=[5,2,8,1,9]
print(max(numeros))
print(max(10,20,30))

numeros=[5,2,8,1,9]
print(min(numeros))
print(min(10,20,30))

lista=[False, True, False]
print(any(lista))
lista_vazia=[]
print(any(lista_vazia))

lista = [True, True, True]
print(all(lista))
lista = [True, False, True]
print(all(lista))

texto = "meu cachorro cagou no patio!"
print(len(texto))

lista = [1,2,3,4,5,19,79]
print(len(lista))

dicionario = dict(nome="Lucas", idade=26)
print(dicionario)

print(abs(-5))
print(abs(3.14))

print(bin(5))
print(bin(10))

def quadrado(numero):
    return numero **2
numeros = [1,2, 3, 4, 5,]
quadrados = map(quadrado, numeros)
print(list(quadrados))

def quadrado(numero):
    return numero **2
numeros = [10,20, 30, 40, 50,]
quadrados = map(quadrado, numeros)
print(list(quadrados))

def quadrado(numero):
    return numero /2
numeros = [10,20, 30, 40, 50,]
quadrados = map(quadrado, numeros)
print(list(quadrados))