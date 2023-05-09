#recebe o número inteiro
n = int(input())

#calcula raiz quadrada de 5 (que será aplicada na fórmula)
raiz = 5 ** (1/2)

#parte esquerda do numerador, conforme fórmula
esq = ((1 + raiz) /2) ** n

#parte direita do numerador, conforme fórmula
dir = ((1 - raiz) /2) ** n

#aplica a fórmula
fib = (esq - dir) / raiz

#imprime valor com uma casa decimal
print(f'{fib:.1f}')
