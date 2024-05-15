import concurrent.futures

import g4f
from g4f.Provider import __all__, ProviderUtils

proxies_list = []


def check_providers():
    working_providers = []
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [
            executor.submit(__test_provider, provider)
            for provider in __all__
        ]
        for future in concurrent.futures.as_completed(futures):
            if result := future.result():
                working_providers.append(result)
        return working_providers


def __test_provider(provider):
    try:
        provider = (ProviderUtils.convert[provider])
        if provider.working and not provider.needs_auth:
            print('testing', provider.__name__)
            g4f.ChatCompletion.create(model='gpt-3.5-turbo',
                                      messages=[{"role": "user", "content": "hello"}],
                                      provider=provider,)
            return provider.__name__
    except Exception as e:
        print(f'Failed to test provider: {provider} | {e}')
        return None
