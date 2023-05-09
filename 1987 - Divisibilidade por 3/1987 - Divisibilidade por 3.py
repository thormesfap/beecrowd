#Processamento entre try/except, porque a questão informa que o fim da entrada se dá por EOF, o que gera erro ao buscar input. Então enquanto houver input, processa, sai quando não houver mais
while True:
    try:
        #pega n e m, a partir do input, sem converter em inteiro, já que o m deve ser recebido como string
        n, m = input().split()
        #converte apenas o n em inteiro
        n = int(n)
        #inicializa a soma
        soma = 0
        #itera em cada número da string "m"
        for i in m:
            #incrementa a soma com o valor inteiro do dígito
            soma += int(i)
        # é divisível por 3 se o resto da divisão da soma por 3 for igual a zero
        if soma % 3 == 0:
            print(f'{soma} sim')
        else:
            print(f'{soma} nao')
    except:
        break