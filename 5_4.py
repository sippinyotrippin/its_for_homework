# Написать программу генерации треугольника Паскаля указанной глубины

n = int(input('enter: '))
triangle = []
for i in range(n):
    row = [str(1) for j in range(i + 1)]
    triangle.append(row)
    print(' ' * (n-i), ' '.join(row))

print()
print(triangle)
