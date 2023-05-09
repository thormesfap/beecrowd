# importar a classe Counter, que realiza contagem de itens
from collections import Counter

#pega o número de números
N = int(input())

#inicializa a lista
lista = []


for i in range(N):
    #adiciona cada número à lista
    lista.append(int(input()))


#ordena a lista de forma crescente, para que na contagem, cada chave já esteja ordenada de forma crescente
lista.sort()

#gera um Contador, com estrutura de dicionário, cuja chave é o número e o valor é a contagem de aparições
aparicoes = Counter(lista)

#itera nos itens contados, pegando cada número(chave - k) e sua contagem(valor - v), printando-os
for k, v in aparicoes.items():
    print(f'{k} aparece {v} vez(es)')
