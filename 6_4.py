# Дан список содержащий в себе различные типы данных, отфильтровать таким
# образом, чтобы остались только строки, использование дополнительного списка
# незаконно

def filter_str(some_list):
    i = 0
    while i != len(some_list):
        if type(some_list[i]) != str:
            del some_list[i]
        else:
            i += 1
    return some_list


my_list = [1, 2, 3, 'prodam', 4, 5, 'rpg', 6]
print(filter_str(my_list))
