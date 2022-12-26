# Вычислить число c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$

from math import pi
count = 0
d = (input("Введите число :\n"))
for i in range(0, len(d)):
    if d[i].isdigit() == False:
        i += 1
        for j in range(i, len(d)):
            count += 1

print(f'число Пи с заданной точностью {d} равно {round(pi, count)}')
