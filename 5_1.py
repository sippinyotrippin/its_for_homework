# Вывести первые N чисел кратные M и больше K
n = int(input())
m = int(input())
k = int(input())
for i in range(k, k + m * n + 1):
    if i % m == 0 and i > k:
        print(i)
