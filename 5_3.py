# Вывести четные числа от 2 до N по 5 в строку

n = int(input('enter N: '))  # 30
my_list = [str(i) for i in range(2, n+1) if i % 2 == 0]
for i in range(0, round(n / 9)+1):
    print(' '.join(my_list[i*5:5*i + 5]))
