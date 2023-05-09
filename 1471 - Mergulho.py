while True:
    try:
        N, R = [int(x) for x in input().split()]
        sobreviventes = [int(x) for x in input().split()]
        voluntarios = list(range(1, N + 1))
        for i in sobreviventes:
            index = voluntarios.index(i)
            voluntarios.pop(index)

        if len(voluntarios) == 0:
            print("*")
        else:
            for vol in voluntarios:
                print(vol, end=" ")
            print()
    except:
        break