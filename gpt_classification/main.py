import csv

from g4f.Provider import You

from gpt_classification.classification import filtration
from gpt_classification.utils import files


if __name__ == '__main__':
    #providers = Providers.check_providers()
    providers = [You]
    models = ['gpt-3.5-turbo']
    print(f'Working providers: {providers}')
    files.configure()
    file = files.read_csv_file()
    texts = []
    for row in file:
        for model in models:
            texts.append({
                'Text': str(row[files.get_text_column()]),
                'Model': model,
                'Provider': You,
                'Response': ''
            })

    _filter = filtration.Filtration(files.__promt, providers)
    _filter.classify_garbage(list_of_texts=texts)
    to_csv_file = open(files.get_data_file('classified_texts.csv'), 'w', newline='', encoding='utf-8')
    headers = ['Текст', 'Классификация']
    writer = csv.DictWriter(to_csv_file, delimiter=';', fieldnames=headers)
    writer.writeheader()
    for chunks in _filter.get_result_list():
        for chunk in chunks:
            writer.writerow({'Текст': chunk['Text'], 'Классификация': chunk['Response']})
    to_csv_file.close()
