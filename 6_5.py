# Дан список чисел, необходимо его развернуть без использования метода revese и
# функции reversed, а так же дополнительного списка и среза

def special_reverse(numbers):
    for i in range(0, len(numbers) - 1):
        numbers.insert(i, numbers[-1])
        del numbers[-1]
    return numbers


num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(special_reverse(num_list))
