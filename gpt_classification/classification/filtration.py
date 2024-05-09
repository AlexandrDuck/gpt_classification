import asyncio
import time
import g4f


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

    async def __if_garbage(self, text, provider):
        #print(f'Try to classify text.')
        try:
            response = await g4f.ChatCompletion.create_async(
                model='gpt-3.5-turbo',
                provider=provider,
                messages=[{"role": "user", "content": f"В этом тексте есть реклама? - {text}"}]
            )
            ans = ''
            for token in response:
                ans += token
            return {'text': text, 'response': self.__check_response(response)}
        except Exception as ex:
            print(f'Classification of text failed. {ex}')
            return {'text': text, 'response': 'Проверить вручную'}

    async def __classify_garbage(self, chunks):
        tasks = []
        i = 0
        time0 = time.time()
        for chunk in chunks:
            provider = self.providers[i]
            tasks.append(await asyncio.gather(
                *[self.__if_garbage(text, provider) for text in chunk]))
            i += 1
            if i >= len(self.providers):
                i = 0
        for task in tasks:
            self.result_list.append(task)
        print(f'Time spent: {time.time()-time0}')

    def classify_garbage(self, list_of_texts):
        list_of_texts = list_of_texts[:100]
        chunk_size = 20
        chunks = [list_of_texts[i:i + chunk_size] for i in range(0, len(list_of_texts), chunk_size)]
        print(f'Classification started...')
        asyncio.run(self.__classify_garbage(chunks))
