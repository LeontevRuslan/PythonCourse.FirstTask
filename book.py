import csv
import sys
import os

filename = 'results.csv'


def set_new():
    while True:
        keyy = input("Какой ключ хотите добавить? ")
        valuee = input("Укажите значения для ключа: ")
        if set(keyy) & set('@/*#!$%^?\[]-_)+=;`~.,<>\'"|'):
            print('\nНедопустимые символы!')
            print('Введите другой ключ\n')
        elif keyy == '' or valuee == '':
            print('\nКлюч или значение не могут быть пустыми')
            print('Введите новые ключ или значение\n')
        else:
            break

    with open("results.csv", "a", newline='') as file:
        csv_file = csv.writer(file)
        csv_file.writerow([keyy, valuee])

    return keyy


def keys():
    with open('results.csv', mode='r') as file:
        csv_reader = csv.reader(file)
        data = {}
        for row in csv_reader:
            data[row[0]] = row[1]
        return data


def get_keys(value):
    data = keys()
    return data.get(' '.join(value[2:]))


if __name__ == "__main__":
    file_is_not_exist = ('Файла не существует.'
                         '\nИспользуйте команду set_new'
                         '\nдля создания файла.')
    if 'set_new' in sys.argv:
        set_new()
        print('OK')
    elif 'keys' in sys.argv:
        if os.path.exists(filename):
            print('\n'.join(list(keys().keys())))
        else:
            print(file_is_not_exist)
    elif 'get' in sys.argv:
        if os.path.exists(filename):
            print(get_keys(sys.argv))
        else:
            print(file_is_not_exist)
    else:
        print('Такой команды не существует!')
