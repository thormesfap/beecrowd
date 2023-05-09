from collections import Counter
while True:
    try:
        palavra = input()
        if palavra == "":
            break
        contagem = Counter(palavra)
        adicao = 0
        for l, c in contagem.items():
            if c % 2 != 0:
                adicao += 1
        if adicao > 0:
            adicao -= 1
        print(adicao)
    except:
        break