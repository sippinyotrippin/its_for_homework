# Написать программу генерации треугольника Паскаля указанной глубины
from math import factorial


def pascal(n):
    row = []
    for i in range(n):
        element = factorial(n) // (factorial(i) * factorial(n - i))
        row.append(element)
    row.append(1)
    return row


n_str = int(input('enter the deep of triangle: ')) + 1
for j in range(n_str):
    line = pascal(j)
    print(line)

