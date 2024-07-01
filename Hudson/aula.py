numeros = [5, 2,8,1,9]
print(max(numeros))

print(max(10, 20, 30))

numeros = [28392, 1828, 192823 ,1828,]
print(max(numeros))

print(min(10, 20, 30))
numeros = [5, 2,8,1,9]
print(min(numeros))

lista = [False, True, False]
print(any(lista))

lista_vazia = []
print(any(lista_vazia))

lista = [True, True, True]
print(all(lista))

lista = [True, False, True]
print(all(lista))

texto = "meu cachorro cagou no pátio"
print(len(texto))

texto = "olá, mundo!"
print(len(texto))

lista = [1, 2, 3, 4, 5, 6, 7, 8]
print(len(lista))

dicionario = dict(nome="hudson" , idade=20)
print(dicionario)

print(abs(-5))
print(abs(3.14))

print(bin(5))
print(bin(992292241))

def quadrado(numero):
    return numero **2

numeros = [1, 2, 3, 4, 5]
quadrado = map(quadrado, numeros)
print(list(quadrado))
