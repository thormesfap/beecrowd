#recebe números da aposta e do jogo, convertendo cada um deles para inteiro e adicionando a uma lista
aposta = [int(x) for x in input().split()]
jogo = [int(x) for x in input().split()]

#inicializa os acertos
acertos = 0

#itera em cada um dos números do jogo
for n in jogo:
    #verifica se o número do jogo está dentro da lista de números da aposta (contagem maior que 0), se sim, acertou o número
    if aposta.count(n) > 0:
        acertos += 1

#imprime o resultado conforme o número de acertos
if acertos < 3:
    print("azar")
elif acertos == 3:
    print("terno")
elif acertos == 4:
    print("quadra")
elif acertos == 5:
    print("quina")
else:
    print("sena")