# Дан словарь, ключ - Название страны, значение - список городов, на вход
# поступает город, необходимо сказать из какой он страны

# Дан словарь, ключ - Название страны, значение - список городов, на вход
# поступает город, необходимо сказать из какой он страны

data = {
    'Russia': ['Moscow', 'Saint Petersburg', 'Omsk'],
    'Belarus': ['Minsk', 'Brest', 'Gomel'],
    'Ukraine': ['Kiev', 'Kharkiv', 'Lviv'],
    'Poland': ['Warsaw', 'Gdansk', 'Krakow']
}


def city_country(city):
    for key, val in data.items():
        if city in val:
            return key


my_city = input('city: ')
print(city_country(my_city))
