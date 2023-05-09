N = int(input())
paises = []
for i in range(N):
    pais, O, P, B = input().split()
    paises.append({"pais": pais, "ouro": int(O), "prata": int(P), "bronze": int(B)})


paises.sort(key= lambda x: (x['ouro'], x['prata'], x['bronze'], x['pais']), reverse=True)
for pais in paises:
    print(pais['pais'], pais['ouro'], pais['prata'], pais['bronze'])
