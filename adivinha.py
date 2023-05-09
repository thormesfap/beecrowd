cases = []
N = int(input())
for i in range(N):
    QT, S = [int(x) for x in input().split()]
    guess = [int(x) for x in input().split()]
    cases.append([QT, S, guess])

for case in cases:
    QT, S, guess = case[0], case[1], case[2]
    dist = 9999999999999999
    pos_dist = 0
    for i in range(QT):
        if guess[i] == S:
            pos_dist = i + 1
            break
        if dist > abs(guess[i] - S):
            dist = abs(guess[i] - S)
            pos_dist = i + 1

    print(pos_dist)