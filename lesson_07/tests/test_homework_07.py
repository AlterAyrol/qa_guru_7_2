import os
import csv
import pypdf
# TODO оформить в тест, добавить ассерты и использовать универсальный путь

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

with open('resources/new_csv.csv', 'w') as csv_file:
    csvwriter = csv.writer(csv_file, delimiter=';')
    csvwriter.writerow(['Bonny', 'Born', 'Peter'])
    csvwriter.writerow(['Alex', 'Serj', 'Yana'])

with open('resources/new_csv.csv') as csv_file:
    csvreader = csv.reader(csv_file, delimiter=';')
    for row in csvreader:
        print(row)


def test_txt():
    pass


def test_pdf():
    pass


def test_xlsx():
    pass


def test_zip():
    pass