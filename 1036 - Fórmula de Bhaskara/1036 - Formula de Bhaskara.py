import math
a, b, c = [float(k) for k in input().split()]

delta = (b ** 2) - (4 * a * c)
if delta < 0 or a == 0:
    print("Impossivel calcular")
    exit()

R1 = (-b + math.sqrt(delta)) / (2 * a)
R2 = (-b - math.sqrt(delta)) / (2 * a)
print(f"R1 = {R1:.5f}")
print(f"R2 = {R2:.5f}")