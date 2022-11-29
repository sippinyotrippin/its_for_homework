# Дан список чисел и на вход поступает число N, необходимо сместить список на
# указанное число, пример: [1,2,3,4,5,6,7] N=3 ответ: [5,6,7,1,2,3,4]

def remove_elements(numbers: list, n: int) -> list:
    is_needed = numbers[:n+1]
    del numbers[:n+1]
    numbers.extend(is_needed)
    return numbers


a_list = [i for i in range(1, 8)]  # [1, 2, 3, 4, 5, 6, 7]
n = int(input('enter N: '))
print(remove_elements(a_list, n))
