n = int(input())

raiz = 5 ** (1/2)

esq = ((1 + raiz) /2) ** n
dir = ((1 - raiz) /2) ** n
fib = (esq - dir) / raiz
print(f'{fib:.1f}')
