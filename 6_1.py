# Написать функцию перевода десятичного числа в двоичное и обратно, без
# использования функции int
def is_int_bin(int_num: int) -> None:
    remainder1 = ''
    while int_num > 0:
        remainder1 = str(int_num % 2) + remainder1
        int_num = int_num // 2
    return print(remainder1)


number10 = int(input('Введите число в десятичной системе исчисления для перевода в двоичную: '))
is_int_bin(number10)

def is_bin_int(bin_num: str) -> None:
    remainder2 = 0
    while bin_num != '':
        remainder2 = remainder2 * 2 + int(bin_num[0])
        bin_num = bin_num[1:]
    return print(remainder2)


number2 = input('Введите число в двоичной системе исчисления для перевода в десятичную: ')
is_bin_int(number2)

