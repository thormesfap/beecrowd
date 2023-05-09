aposta = [int(x) for x in input().split()]
jogo = [int(x) for x in input().split()]

acertos = 0
for n in jogo:
    if aposta.count(n) > 0:
        acertos += 1


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