# Пользователь вводит предложение, заменить все пробелы на '-' 2-мя способами

# Первый способ:

sentence = input('Enter the sentence at first time: ')
sentence = sentence.split()
sentence = '-'.join(sentence)
print(sentence)