numeros = [5,2,8,1,9]
print(max(numeros))

print(max(10,20,30))

numeros=[5,2,8,1,9]
print(min(numeros))

print(min(10,20,30))

numeros = [52,25,81,61,18]
print(max(numeros))

print(max(20,40,80))

numeros=[54,22,80,18,90]
print(min(numeros))

print(min(8,60,20))

lista=[False,True,False]
print(any(lista))

lista_vazia = []
print(any(lista_vazia))

lista = [True, True, True, True]
print(all(lista))

lista = [True, False, True]
print(all(lista))

lista = [1, 2, 3, 4, 5,6]
print(len(lista))

texto = "olá, mundo!"
print(len(texto)) #saída: 11

texto = "meu cachorro fez cocô no patio"
print(len(texto))

dicionario = dict(nome="Micheli", idade=23)
print(dicionario)

print(abs(-5))
print(abs(3.14))

print(bin(5))
print(bin(10))
print(bin(15))
print(bin(23))
print(bin(4598433))

def quadrado(numero):
    return numero **2
numeros = [1, 2, 3, 4, 5, 6, 7, 8,]
quadrados = map(quadrado, numeros)
print(list(quadrados))