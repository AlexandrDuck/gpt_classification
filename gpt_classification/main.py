import csv

from g4f.Provider import You

from gpt_classification.classification import filtration
from gpt_classification.utils import files


if __name__ == '__main__':
    #providers = Providers.check_providers()
    providers = [You]
    print(f'Working providers: {providers}')
    files.configure()
    file = files.read_csv_file()
    texts = []
    for row in file:
        texts.append(row['Пост'])
    _filter = filtration.Filtration(files.__promt, providers)
    _filter.classify_garbage(list_of_texts=texts)
    to_csv_file = open('data/classified_texts.csv', 'w', newline='', encoding='utf-8')
    headers = ['Текст', 'Классификация']
    writer = csv.DictWriter(to_csv_file, delimiter=';', fieldnames=headers)
    for chunks in _filter.get_result_list():
        for chunk in chunks:
            writer.writerow({'Текст': chunk['text'], 'Классификация': chunk['response']})
    to_csv_file.close()
