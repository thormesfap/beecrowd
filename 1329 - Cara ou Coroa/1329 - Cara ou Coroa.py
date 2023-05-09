# incializa os casos
cases = []

#cria loop que deve se encerrar quando o usuário digitar 0 como número de jogos
while True:

    N = int(input())
    # se o número de jogos for 0, sai do loop
    if N == 0:
        break

    #pega a lista de jogos e adiciona na lista de casos (sem necessidade em converter em inteiro, pois a comparação será por string também)
    games = input().split()
    cases.append(games)

#itera os casos. Cada "case" será uma lista de jogos, então será feito outro loop dentro deste
for case in cases:
    #inicializa as variáveis
    mary = 0
    john = 0

    #itera em cada jogo ("0" ou "1")
    for i in case:
        # comparação com string, já que não foi feita conversão em inteiro
        if i == "0":
            mary += 1
        else:
            john += 1
    #ao final de cada caso, imprime o resultado
    print(f"Mary won {mary} times and John won {john} times")