import asyncio
import time
import g4f

from gpt_classification.utils import files


class Filtration:

    def __init__(self, promt, providers):
        self.promt = promt
        self.providers = providers
        self.provider_iterator = iter(self.providers)
        self.result_list = []

    def get_result_list(self):
        return self.result_list

    def __check_response(self, text):
        categories = ['поздравления', 'спорт', 'культура', 'благотворительность', 'реклама', 'контент интернет-магазинов', 'покупка', 'продажа', 'обмен', 'вакансии', 'поиск знакомств', 'путешествия', 'религия']
        positive_keys = ['текст можно отнести', 'текст можно однозначно отнести', 'он относится к теме', 'текст оносится к теме']
        negative_keys = ['не удалось найти', 'не подпадает', 'не ясно', 'не подходит', 'не относится', 'нельзя однозначно', 'сложно однозначно', 'трудно однозначно', 'невозможно однозначно', 'не могу однозначно', 'не может быть однозначно', 'нет информации', 'не содержит достаточно', 'не содержит явной', 'не содержит явных', 'не является однозначно', 'не является явным']
        text = str(text).lower()
        if text != '':
            if text == 'да':
                return 'Мусор'
            if text == 'нет':
                return 'Не мусор'
            for neg_key in negative_keys:
                if neg_key in text:
                    return 'Не мусор'

            for pos_key in positive_keys:
                if pos_key in text:
                    for word in text.split('"'):
                        if word in categories:
                            return 'Мусор'
                    for word in text.split("'"):
                        if word in categories:
                            return 'Мусор'
                    for word in text.split('*'):
                        if word in categories:
                            return 'Мусор'
                    for word in text.split('**'):
                        if word in categories:
                            return 'Мусор'
                    return 'Не мусор'

            return 'Проверить вручную'
        else:
            return 'Провермть вручную'

    async def __if_garbage(self, _dict):
        try:
            response = await g4f.ChatCompletion.create_async(
                model=_dict['Model'],
                provider=_dict['Provider'],
                messages=[{"role": "user", "content": f'Мне нужно классифицировать текст. У меня есть такой текст: {_dict["Text"]}. Можно ли однозначно отнести его к одной из следующих тем: поздравления, спорт, культура, благотворительность, реклама, контент интернет-магазинов, покупка, продажа, обмен, вакансии, путешествия, религия?'}]
            )
            ans = ''
            for token in response:
                ans += token
            _dict['Response'] = ans
            _dict['Response_clear'] = self.__check_response(ans)
            return _dict
        except Exception as ex:
            print(f'Classification of text failed. {ex}')
            _dict['Response'] = 'Проверить вручную'
            return _dict

    async def __classify_garbage(self, chunks):
        tasks = []
        time0 = time.time()
        for chunk in chunks:
            tasks.append(await asyncio.gather(
                *[self.__if_garbage(_dict) for _dict in chunk]))
        for task in tasks:
            self.result_list.append(task)
        print(f'Time spent: {time.time()-time0}')

    def classify_garbage(self, list_of_texts):
        list_of_texts = list_of_texts[:100]
        chunk_size = 20
        chunks = [list_of_texts[i:i + chunk_size] for i in range(0, len(list_of_texts), chunk_size)]
        print(f'Classification started...')
        asyncio.run(self.__classify_garbage(chunks))
