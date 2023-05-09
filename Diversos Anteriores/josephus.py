def josephus(size, skip):
    #list = [*range(1, size + 1)]
    i = 1
    ans = 0
    while i <= size:
        ans = (ans + skip) % i
        i += 1

    return ans + 1


cases = []
N = int(input())
for i in range(N):
    n,m = [int(x) for x in input().split()]
    cases.append([n,m])

for i in range(N):
    ncase = i + 1
    n,m = cases[i][0], cases[i][1]
    survivor = josephus(n, m)
    print(f'Case {ncase}: {survivor}')