# Заполнить словарь где ключами будут выступать числа от 0 до n, а
# значениями вложенный словарь с ключами "name" и "email", а значения
# для этих ключей будут браться с клавиатуры
n = int(input())
data = {i: {'name': input('name: '), 'email': input('email: ')} for i in range(1, n+1)}
print(data)
