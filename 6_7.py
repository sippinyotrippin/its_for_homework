# Дан список чисел, необходимо для каждого элемента посчитать сумму его
# соседей, для крайних чисел одним из соседей является число с противоположной
# стороны списка

def neighbour_sum(alist: list) -> list:
    new_list = []
    for i in range(0, len(alist) - 1):
        a = alist[i - 1] + alist[i + 1]
        new_list.append(a)
    last = alist[len(alist)-2] + alist[0]
    new_list.append(last)
    return new_list


num = [1, 3, 5, 6, 10]
print(neighbour_sum(num))
print(num[-1])