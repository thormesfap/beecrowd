import re

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
    bold_pattern = '\*(.*?)\*'
    italic_pattern = '_(.*?)_'
    case = re.sub(bold_pattern,r"<b>\1</b>", case)
    case = re.sub(italic_pattern,r"<i>\1</i>", case)
    print(case)