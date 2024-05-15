1. Добавляем .csv файл с текстами в папку gpt_classification/data
2. Редактируем файл gpt_classification/data/configuration.txt:
    promt - запрос для модели. В место, где должен быть классифицируемый текст, нужно вставить <text>.
    csv-file - название .csv файла с текстами;
    delimiter - разделитель, используемый в *csv-file*;
    tex_column - название колонки из *csv-file* по которой делать классификацию.

Все поля заполняются без кавычек сразу после знака =
Пример:
***
promt=Сколько букв в этом тексте? Текст: <text>.
csv_file=csv_test.csv
delimiter=;
text_column=Пост
***

3. Запускаем gpt_classification/main.py
На выходе получаем файл gpt_classification/data/classified_texts.csv