# Дан список рандомных чисел, необходимо отсортировать его в виде, сначала
# четные, потом нечётные

def random_sort(numbers: list) -> list:
    even = list(filter(lambda x: x % 2 == 0, numbers))
    odd = list(filter(lambda x: x % 2, numbers))
    result = even + odd
    return result


num_list = [3, 4, 2, 6, 9, 34, 21, 45, 69, 80, 43, 33]
print(random_sort(num_list))
