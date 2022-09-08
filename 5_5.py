# Дан список строк, наобходимо реализовать пагинатор:
#Если пользователь вводит ">" то выводится следующий  элемент из списка,
# если вводит пользователь "<" то предыдущий по этому списку,
# а так же предусмотреть, что если пользователь сейчас находится на последнем элементе,
# то следующий это первый, а если находится на первом элементе, то предыдущий это последний,
# чтобы пользователь мог прокручивать список по кругу в любом направлении
paginator = [1, 2, 3, 4]
counter = 0
while True:
    action = input()
    if action == '>':
        counter += 1
        print(paginator[counter])
    elif action == '<':
        counter -= 1
        print(paginator[counter])
    elif counter == len(paginator) - 1 and action == '>':
        counter = 0
        print(paginator[counter])
    elif counter == 0 and action == '<':
        counter = len(paginator) - 1
        print(paginator[counter])
