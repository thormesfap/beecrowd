while True:
    #Processamento entre try/except, porque a questão informa que o fim da entrada se dá por EOF, o que gera erro ao buscar input. Então enquanto houver input, processa, sai quando não houver mais
    try:
        # pega o número de voluntários e de sobreviventes (convertendo em inteiro)
        N, R = [int(x) for x in input().split()]

        # pega a lista de sobreviventes (convertendo cada um em inteiro)
        sobreviventes = [int(x) for x in input().split()]

        #cria lista de voluntários, iniciando por 1 e terminando em N
        voluntarios = list(range(1, N + 1))

        #itera os sobreviventes, removendo-os da lista de voluntários
        for i in sobreviventes:
            #identifica o índice na lista de voluntários do sobrevivente (a lista e seus índices mudam quando se faz o pop)
            index = voluntarios.index(i)

            #remove da lista de voluntários o sobrevivente (conforme índice já identificado)
            voluntarios.pop(index)

        #se o tamanho da lista de voluntários não sobreviventes for igual a 0, então todos sobreviveram
        if len(voluntarios) == 0:
            print("*")
        else:
            #iter a lista de não sobreviventes, imprimindo cada valor, usando como parâmetro de fim um espaço ao invés de quebra de linha, para impressão lado a lado
            for vol in voluntarios:
                print(vol, end=" ")
            #imprime uma quebra de linha
            print()
    except:
        break