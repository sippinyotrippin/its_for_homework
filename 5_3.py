# Вывести четные числа от 2 до N по 5 в строку
n = int(input())
for i in range(2, n + 1):
    i = str(i)
    i = [i]*5
    i = ' '.join(i)
    print(i)