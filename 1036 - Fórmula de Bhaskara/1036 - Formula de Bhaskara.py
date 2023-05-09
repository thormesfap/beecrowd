import math
# recebe os números a, b e c do input, já transformando em inteiro cada um deles
a, b, c = [float(k) for k in input().split()]

#calcula o delta
delta = (b ** 2) - (4 * a * c)

#verifica se o delta é menor que zero (raiz de número negativo) ou se a é igual a zero (divisão por zero) para determinar se é impossível calcular. Se for, imprime e sai do script
if delta < 0 or a == 0:
    print("Impossivel calcular")
    exit()

# calcula as duas raízes e imprime ao final
R1 = (-b + math.sqrt(delta)) / (2 * a)
R2 = (-b - math.sqrt(delta)) / (2 * a)
print(f"R1 = {R1:.5f}")
print(f"R2 = {R2:.5f}")