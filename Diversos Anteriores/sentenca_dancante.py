cases = []

while(True):
    try:
        sentence = input()
        if sentence == "":
            break
        cases.append(sentence)

    except:
        break

for case in cases:
    sentenca = case
    direction = 1
    sentenca = sentenca.lower()
    nova_sentenca = ""
    for i in sentenca:
        if i == " ":
            nova_sentenca += " "
            continue

        if direction > 0:
            nova_sentenca += i.upper()
        else:
            nova_sentenca += i

        direction -= (2 * direction)

    print(nova_sentenca)