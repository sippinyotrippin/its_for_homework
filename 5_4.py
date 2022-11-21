# Написать программу генерации треугольника Паскаля указанной глубины

n = int(input('enter: '))
triangle = []
for i in range(n):
    row = [1 for j in range(i + 1)]
    print(row)
    triangle.append(row)