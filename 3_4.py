# Пользователь вводит 3 числа, сказать сколько из них положительных и сколько отрицательных

num1 = int(input())
num2 = int(input())
num3 = int(input())
plus = (num1 > 0) + (num2 > 0) + (num3 > 0)
minus = (num1 < 0) + (num2 < 0) + (num3 < 0)
print(plus, 'положительных чисел')
print(minus, 'отрицательных чисел')
