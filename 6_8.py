# Дан словарь, ключ - Название страны, значение - список городов, на вход
# поступает город, необходимо сказать из какой он страны

data = {
    'Russia': ['Moscow', 'Saint Petersburg', 'Omsk'],
    'Belarus': ['Minsk', 'Brest', 'Gomel'],
    'Ukraine': ['Kiev', 'Kharkiv', 'Lviv']
}
city = input('city: ')
for key, val in data.items():
    if city in val:
        print(key)
