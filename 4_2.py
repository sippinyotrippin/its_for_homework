# Без использования collections, написать программу,
# которая будет создавать словарь
# для подсчитывания количества вхождений каждой буквы
# в текст введенный с клавиатуры

text = input('enter: ').lower()
count_dict = {}
for i in text:
    if i in count_dict:
        count_dict[i] += 1
    else:
        count_dict[i] = 1
print(count_dict)
