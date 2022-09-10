# Написать функцию перевода десятичного числа в двоичное и обратно, без
# использования функции int
def int_bin(num: int) -> str:
    b = ''
    while num > 0:
        b = str(num % 2) + b
        num = num // 2
    return print(b)

number10 = int(input('Введите число в десятичной системе исчисления для перевода в двоичную: '))
int_bin(number10)

