cases = []
while True:
    N = int(input())
    if N == 0:
        break
    games = input().split()
    cases.append(games)

for case in cases:
    mary = 0
    john = 0
    for i in case:
        if i == "0":
            mary += 1
        else:
            john += 1

    print(f"Mary won {mary} times and John won {john} times")