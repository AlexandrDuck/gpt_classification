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
    count = 0
    for chunks in _filter.get_result_list():
        for chunk in chunks:
            if chunk['response'] == 'Проверить вручную':
                count += 1
            print(chunk['response'])
    print(count)
