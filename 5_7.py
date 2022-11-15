#  Дан список чисел, отсортировать его по возрастанию без использования sort и sorted

unsorted_list = [10, 9, 7, 6, 8, 4, 5, 3, 1, 2]
sorted_list = []
while unsorted_list:
    element = min(unsorted_list)
    unsorted_list.remove(element)
    sorted_list.append(element)
print(sorted_list)