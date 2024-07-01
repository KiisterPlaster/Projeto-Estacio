numeros = [8, 2, 4, 19] 
print(max(numeros))  

print(max(10, 20, 30))  


numeros = [8, 2, 4, 19] 
print(min(numeros))  

print(min(10, 20, 30))  


lista = [False, True, False]
print(any(lista))

lista_vazia = []
print(any(lista_vazia))

lista = [True, True, True]
print(all(lista))

lista_vazia = [False, True, False]
print(all(lista))

texto = "meu cachorro fez coco no patio"
print(len(texto))

texto = "Ola, mundo!"
print(len(texto))

dicionario = dict(nome="Geizikelly", idade=20)
print(dicionario)

print(abs(-5))
print(abs(3.14))

print(bin(5))
print(bin(10))
print(bin(2024))

def quadrado(numero):
    return numero ** 2

numeros = [1, 2, 3, 4, 5]
quadrados = map(quadrado, numeros)
print(list(quadrados))