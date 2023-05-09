#importa classe Counter, para contar o número de letras da palavra
from collections import Counter

#Processamento entre try/except, porque a questão informa que o fim da entrada se dá por EOF, o que gera erro ao buscar input. Então enquanto houver input, processa, sai quando não houver mais
while True:
    try:
        #recebe a palavra
        palavra = input()

        #se a palavra estiver em branco, sai do loop
        if palavra == "":
            break

        #cria um contador, com estrutura de dicionário com a contagem de cada letra na palavra
        contagem = Counter(palavra)

        #para ser considerado um palíndromo (no caso um anagrama que forme um palíndromo, de forma que a ordem das letras não importa), tem que ter um número par de cada letra, já que, dividindo-se o anagrama ao meio, o número de letras de cada lado deve ser igual, com exceção de 1 letra, que pode ser a do meio
        adicao = 0
        #itera cada letra da contagem, verificando sua quantidade
        for l, c in contagem.items():
            # se a quantidade de letras na palavra for ímpar, então há necessidade de adição de mais uma letra dessa, para formar o "par" necessário para fazer o palíndromo
            if c % 2 != 0:
                adicao += 1

        #verifica se o número de adições é maior que 0. Para o caso de a palavra já ser um anagrama de palíndromo (todas as letras em números pares). Se não, retira uma letra da necessidade de adição, já que o anagrama pode ter pelo menos uma letra solitária, que poderia ser a do meio.
        if adicao > 0:
            adicao -= 1

        #imprime a quantidade de letras necessárias de serem adicionadas
        print(adicao)
    except:
        break