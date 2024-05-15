import csv
import os

global __promt, __csv_file_name, __delimiter, __text_column
PROJECT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(PROJECT_PATH, 'data')


def get_promt() -> str:
    return __promt


def get_text_column() -> str:
    return __text_column


def get_data_file(filename: str) -> str:
    return os.path.join(DATA_PATH, filename)


def get_n_texts() -> int:
    return __n_texts


def configure():
    global __promt, __csv_file_name, __delimiter, __text_column, __n_texts
    with open(get_data_file('configuration.txt'), 'r', encoding='utf-8') as conf_file:
        __promt = conf_file.readline().strip()[6:]
        __csv_file_name = conf_file.readline().strip()[9:]
        __delimiter = conf_file.readline().strip()[10:]
        __text_column = conf_file.readline().strip()[12:]
        __n_texts = int(conf_file.readline().strip()[8:])


def read_csv_file():
    with open(get_data_file(__csv_file_name), 'r', encoding='utf-8-sig') as csv_file:
        csvfile = csv.DictReader(csv_file, delimiter=__delimiter)
        rows = [row for row in csvfile]
        return rows
