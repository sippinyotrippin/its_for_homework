# Дан список строк, наобходимо реализовать пагинатор:
#Если пользователь вводит ">" то выводится следующий  элемент из списка,
# если вводит пользователь "<" то предыдущий по этому списку,
# а так же предусмотреть, что если пользователь сейчас находится на последнем элементе,
# то следующий это первый, а если находится на первом элементе, то предыдущий это последний,
# чтобы пользователь мог прокручивать список по кругу в любом направлении
paginator = [1, 2, 3, 4]
action: str = input('> <: ')
index = 0
step = len(action)
if step:
    print(paginator[index + step])
elif step