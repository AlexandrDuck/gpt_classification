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
        positive_keys = ['есть реклама', 'присутствует реклама', 'содержит рекламу']
        negative_keys = ['нет рекламы', 'отсутствует реклама', 'не ясно', 'не нашел', 'нет информации о наличии рекламы в тексте', 'не содержит', 'не обнаружил информации']
        text = str(text).lower()
        if text != '':
            for neg_key in negative_keys:
                if neg_key in text:
                    return 'Не реклама'
            for pos_key in positive_keys:
                if pos_key in text:
                    return 'Реклама'
            return 'Проверить вручную'
        else:
            return 'Не реклама'

    async def __if_garbage(self, _dict):
        try:
            response = await g4f.ChatCompletion.create_async(
                model=_dict['Model'],
                provider=_dict['Provider'],
                messages=[{"role": "user", "content": f"{files.get_promt()} - {_dict['Text']}"}]
            )
            ans = ''
            for token in response:
                ans += token
            _dict['Response'] = ans
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
