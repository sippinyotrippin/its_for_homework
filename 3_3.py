#Пользователь вводит Имя, Возраст и Город, сформировать приветственное сообщение путем форматирования 3-мя способами
name = input('Enter your name: ')
age = int(input('Enter your age: '))
city = input('Enter the city you are from: ')
greeting_1 = 'Hello %s from %s aged %d'% (name, city, age)
print(greeting_1)

name = input('Enter your name: ')
age = int(input('Enter your age: '))
city = input('Enter the city you are from: ')
greeting_2 = 'Hello {} from {} aged {}'.format(name, city, age)
print(greeting_2)

name = input('Enter your name: ')
age = int(input('Enter your age: '))
city = input('Enter the city you are from: ')
greeting_3 = f'Hello {name} from {city} aged {age}'
print(greeting_3)