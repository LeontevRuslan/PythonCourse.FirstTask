import csv
import sys

def set_new():
    keyy = input("Какой ключ хотите добавить? ")
    valuee = input("Укажите значения для ключа: ")

    with open("results.csv", "a", newline='') as file:
        csv_file = csv.writer(file)
        csv_file.writerow([keyy, valuee])

    print('OK')

def keys():
    with open('results.csv', mode='r') as file:
        csv_reader = csv.reader(file)
        data = {}
        for row in csv_reader:
            data[row[0]] = row[1]
        return data

def get_keys(value):
    data = keys()
    print(data.get(' '.join(value[2:])))


if __name__ == "__main__":
    if 'set_new' in sys.argv:
        set_new()
    if 'keys' in sys.argv:
        print(list(keys().keys()))
    if 'get' in sys.argv:
        get_keys(sys.argv)