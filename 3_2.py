# Пользователь вводит 3 числа, найти среднее арифмитическое с точностью до трёх знаков.

num1 = float(input())
num2 = float(input())
num3 = float(input())
result = (num1 + num2 + num3) / 3 
result = round(result, 3)
print(result)
