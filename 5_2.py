# Сделать калькулятор: у пользователя спрашивается число, потом действие и второе число
number_1 = int(input())
action = input()
number_2 = int(input())
if action == '+':
    print(number_1, action, number_2, '=', number_1 + number_2)
elif action == '-':
    print(number_1, action, number_2, '=', number_1 - number_2)
elif action == '*':
    print(number_1, action, number_2, '=', number_1 * number_2)
elif action == '/':
    print(number_1, action, number_2, '=', number_1 / number_2)
else:
    print('error')