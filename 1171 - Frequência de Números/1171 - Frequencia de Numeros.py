from collections import Counter
N = int(input())
lista = []
for i in range(N):
    lista.append(int(input()))

lista.sort()
aparicoes = Counter(lista)
for k, v in aparicoes.items():
    print(f'{k} aparece {v} vez(es)')
