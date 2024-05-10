import csv

global __promt, __csv_file_name, __delimiter, __text_column


def configure():
    global __promt, __csv_file_name, __delimiter, __text_column
    with open('C:/Users/Home/PycharmProjects/Gpt/gpt_classification/data/configuration.txt', 'r',
              encoding='utf-8') as conf_file:
        __promt = conf_file.readline().strip()[6:]
        __csv_file_name = conf_file.readline().strip()[9:]
        __delimiter = conf_file.readline().strip()[10:]
        __text_column = conf_file.readline().strip()[13:]


def read_csv_file():
    with open(f'C:/Users/Home/PycharmProjects/Gpt/gpt_classification/data/{__csv_file_name}', 'r',
              encoding='utf-8-sig') as csv_file:
        csvfile = csv.DictReader(csv_file, delimiter=__delimiter)
        rows = [row for row in csvfile]
        return rows
