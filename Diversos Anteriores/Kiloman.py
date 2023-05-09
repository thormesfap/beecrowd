cases = []
N = int(input())
for i in range(N):
    T = int(input())
    alturas = [int(x) for x in input().split()]
    pulos = input()
    cases.append([T, alturas, pulos])


for case in cases:
    T, alturas, pulos = case[0], case[1], case[2]
    acertos = 0
    for i in range(T):
        if pulos[i] == "J":
            if alturas[i] > 2:
                acertos += 1
        else:
            if alturas[i] < 3:
                acertos +=1
    print(acertos)