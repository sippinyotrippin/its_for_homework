#  Дан список чисел, отсортировать его по возрастанию без использования sort и sorted

unsorted_list = [3, 6, 9, 7, 4, 5, 8]
sorted_list = []
while unsorted_list:
    element = min(unsorted_list)
    unsorted_list.remove(element)
    sorted_list.append(element)
print(sorted_list)
