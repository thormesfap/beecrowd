while True:
    try:
        n, m = input().split()
        n = int(n)
        soma = 0
        for i in m:
            soma += int(i)
        if soma % 3 == 0:
            print(f'{soma} sim')
        else:
            print(f'{soma} nao')
    except:
        break