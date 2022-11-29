# Дан словарь словарей, ключ внешнего словаря - id пользователя, значение -
# словарь с данными о пользователе (имя, фамилия, телефон, почта), вывести
# имена тех, у кого не указана почта (нет ключа email или значение этого ключа -
# пустая строка)
data = {
    1: {'name': 'Alex',
        'surname': 'Fomenko',
        'phone': 354_22_98,
        'email': ''
        },
    2: {'name': 'Petr',
        'surname': 'Yan',
        'phone': 252_88_43,
        'email': 'petr@killer.ru'
        },
    3: {'name': 'Maxim',
        'surname': 'Fadeev',
        'phone': 742_53_11
        },
    4: {'name': 'Ivan',
        'surname': 'Lobkov',
        'phone': 328_04_20,
        'email': 'justine@maul.com'}
}
dicts = list(data.values())
for i in range(0, len(dicts)):
    if 'email' not in dicts[i] or dicts[i]['email'] == '':
        print(dicts[i]['name'])
