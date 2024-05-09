import concurrent.futures

import g4f
import requests
from bs4 import BeautifulSoup
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


def find_proxies():
    cookies = {
        'sbjs_migrations': '1418474375998%3D1',
        'sbjs_first_add': 'fd%3D2024-01-13%2011%3A08%3A49%7C%7C%7Cep%3Dhttps%3A%2F%2Fhidemy.io%2Fru%2Fproxy-list%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.google.com%2F',
        'sbjs_current': 'typ%3Dorganic%7C%7C%7Csrc%3Dgoogle%7C%7C%7Cmdm%3Dorganic%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29',
        'sbjs_first': 'typ%3Dorganic%7C%7C%7Csrc%3Dgoogle%7C%7C%7Cmdm%3Dorganic%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29',
        'PAPVisitorId': '64e05c8c9924484e56c9eefdfd4j0g9u',
        '_ym_uid': '1705118930242418742',
        '_ym_d': '1705118930',
        'cjConsent': 'MHxOfDB8Tnww',
        'cjUser': '4c9c053a-113c-4760-9259-fea52f8beeb8',
        '_tt_enable_cookie': '1',
        '_ttp': '1Gg00A7Bgs6u3-UzdzWNWIBdQbD',
        '_ga_42493SHRVC': 'GS1.2.1709463028.4.1.1709463053.35.0.0',
        't': '376787400',
        'sbjs_current_add': 'fd%3D2024-04-13%2010%3A30%3A34%7C%7C%7Cep%3Dhttps%3A%2F%2Fhidemy.io%2Fru%2Fproxy-list%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.google.com%2F',
        'CookieConsent': '{stamp:%27-1%27%2Cnecessary:true%2Cpreferences:true%2Cstatistics:true%2Cmarketing:true%2Cmethod:%27implied%27%2Cver:1%2Cutc:1712979035628%2Cregion:%27RU%27}',
        '_ga': 'GA1.1.1786902581.1705118929',
        '_ym_isad': '2',
        'cf_clearance': 'HZrlCfqbaIZATE15do.VkFV9FCeCrkMqeP07a2xcHT8-1713004975-1.0.1.1-qvgoSYXbvYAEpEVQinxt19pP07nWD25fkEPX_20yH4h3p1AwuiIQdnWGl_OssTy_ck8oVDRv_OxD9Xkhf8Utaw',
        'sbjs_udata': 'vst%3D7%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F123.0.0.0%20Safari%2F537.36%20Edg%2F123.0.0.0',
        '_ga_KJFZ3PJZP3': 'GS1.1.1713006818.10.0.1713006818.60.0.0',
        'cf_chl_3': '4898c563a0b5df6',
    }

    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'ru,en;q=0.9,en-GB;q=0.8,en-US;q=0.7,mt;q=0.6',
        'cache-control': 'max-age=0',
        'content-type': 'application/x-www-form-urlencoded',
        # 'cookie': 'sbjs_migrations=1418474375998%3D1; sbjs_first_add=fd%3D2024-01-13%2011%3A08%3A49%7C%7C%7Cep%3Dhttps%3A%2F%2Fhidemy.io%2Fru%2Fproxy-list%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.google.com%2F; sbjs_current=typ%3Dorganic%7C%7C%7Csrc%3Dgoogle%7C%7C%7Cmdm%3Dorganic%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29; sbjs_first=typ%3Dorganic%7C%7C%7Csrc%3Dgoogle%7C%7C%7Cmdm%3Dorganic%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29; PAPVisitorId=64e05c8c9924484e56c9eefdfd4j0g9u; _ym_uid=1705118930242418742; _ym_d=1705118930; cjConsent=MHxOfDB8Tnww; cjUser=4c9c053a-113c-4760-9259-fea52f8beeb8; _tt_enable_cookie=1; _ttp=1Gg00A7Bgs6u3-UzdzWNWIBdQbD; _ga_42493SHRVC=GS1.2.1709463028.4.1.1709463053.35.0.0; t=376787400; sbjs_current_add=fd%3D2024-04-13%2010%3A30%3A34%7C%7C%7Cep%3Dhttps%3A%2F%2Fhidemy.io%2Fru%2Fproxy-list%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.google.com%2F; CookieConsent={stamp:%27-1%27%2Cnecessary:true%2Cpreferences:true%2Cstatistics:true%2Cmarketing:true%2Cmethod:%27implied%27%2Cver:1%2Cutc:1712979035628%2Cregion:%27RU%27}; _ga=GA1.1.1786902581.1705118929; _ym_isad=2; cf_clearance=HZrlCfqbaIZATE15do.VkFV9FCeCrkMqeP07a2xcHT8-1713004975-1.0.1.1-qvgoSYXbvYAEpEVQinxt19pP07nWD25fkEPX_20yH4h3p1AwuiIQdnWGl_OssTy_ck8oVDRv_OxD9Xkhf8Utaw; sbjs_udata=vst%3D7%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F123.0.0.0%20Safari%2F537.36%20Edg%2F123.0.0.0; _ga_KJFZ3PJZP3=GS1.1.1713006818.10.0.1713006818.60.0.0; cf_chl_3=4898c563a0b5df6',
        'origin': 'https://hidemy.io',
        'referer': 'https://hidemy.io/ru/proxy-list/?type=s&__cf_chl_tk=UVZ0wgV2bG3FvnSNcONhqXsO54KGx_ysiCxh0ctOZn0-1713006818-0.0.1.1-1322',
        'sec-ch-ua': '"Microsoft Edge";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
        'sec-ch-ua-arch': '"x86"',
        'sec-ch-ua-bitness': '"64"',
        'sec-ch-ua-full-version': '"123.0.2420.97"',
        'sec-ch-ua-full-version-list': '"Microsoft Edge";v="123.0.2420.97", "Not:A-Brand";v="8.0.0.0", "Chromium";v="123.0.6312.123"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-model': '""',
        'sec-ch-ua-platform': '"Windows"',
        'sec-ch-ua-platform-version': '"15.0.0"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0',
    }

    params = {
        'type': 's',
    }

    data = {
        'be371a26c0abe4fb331c4d889dc47da67bfa1058ecf3e02aebb8eb6538ecdbe6': 'GdI8tMdy_7UD1M5XbzrsepGRylvvxh0QTYmzmmQeK_c-1713006818-1.1.1.1-wdOSRAAZZuOimrwh6o12WpCozL3kX9CF0_IuI.HKcx2zWOeWH3WiqJviAr6XcH8uOcTfWlCyn5TtHoS1jk0WyAulSsWEuxM1wPa0eAV9XGNMfLsGb1xpn3fmZgfogWNR4CTOjMZbjdO.cNdn.wFXmYhZdLIgpmxc.b6HcU67iRADRFYL3TZphiT5xnYc5FUE3MBmYqlJIqOBfS5Kkvnk6kc4w92orK2eG7ZxXGi6ZWWHbAodmm19Vzrwqb7F.DsgtczEGSmUocRV94vBBlgnHETR38BCNsxEC1U6nXi4aivvCJQSlR.l_tZd1dIZnVjkZyuHtsuS3bL1ydNsz.COxufEyHtCfcsB5LeWUTbnMEDh3vjY8tBI8OxqnO6J5jlk5TSROVRZqChizlacsgb7DdhzfHjgQXoHGtkDw5MUQdsZX.1RipwQd41e8haov9Rdw7RizLV6kfwBHdqc0eLJqbbUJa9b5glGgSKrtj7s5gtG9ywWBFHIHSBZLRDBvXdAtey6IAFyeflgFFh1dHhUvr3jRWM9VKym8BjD.V9mHWU.8s3ha.zqdoQU7456vSPS4ZdwGZAwxxBGSnUeehI9ua8N3.rzJNkc5Ws2gLJQGE1GNe_AA9ss5dZsXUGsQGhSzmmmWAqkBkCB.Wc8tJuxF3CGYcHiXz1XauNFr2dyRiPnn3PWUFcjCN5NReVaRVdopSY3CgzK6_6mNw67zPbzEOnSxAEWS.JusUyByWQ3k6PDMc52mqaN2iByC5YzYHJk_AnLoPzqqxcbj_vtkbBk5j2plsnPLPgGHy5tcv48e9iuQLWqKj2HTBrZDGTHw5rpPMWHjkyaexWNpAImzcYkChCv307sFmYJrTlY3.gBVQzpN_YJYQozR6Zvy1p6KXdOoB7rYlZ899a2TdBAueTlYCouOIwkPrbvQ4SWw_6n1wwYV6ccJo4BhDlfHTWEFW7f7hYuWeIvC2nJppkQZjuljlu2xHaHAJ1V0V.ALNcOrRIhNMlikPEGmI_tPkHWHxrsekDfg8H5gH4k7DnC_J1UG_1DXgqR0VgRf0x1z8Vh8qku_IxSbJBW5dbtzx8zdakTIfVkKbd1in5SZoFs1VuH9K4cd354iHlyoRX2exaPPQ6i42eu_OYxQmlSbCaABqDlx0oy68gcigDHqGy8zmuyQzppYuinqpgN8TySESCINacOZb9bBZtdazxsdpuMJb8dwfNdrIytdlN_tGr64U6Q50OwZfo3hrVhxOvzqooYsmQ',
        '179be4149e26f3a1b8ff78bcdae4748683674d079fbfc31690527f7a23f2f55a': '4EUYNkAjF2ktCh_4Sf_c_IhTetx7UowaciLVYF2Gggc-1713006818-1.1.1.1-jWlznWE3eGtYtzgqkFOhRl62LYrIObn3ivwgWTDmd_rTImp_aEcMFXGqUZL1mHTC.KtFEWxh9P6AdjE4Iwx7omE757dzQyK4k6KSVTfEMAqkkoAsSuW2rbmvt6YzkUnaw7HxrKA4LT1DON6kc.sHNxrvkz7u.wWyn2M4r2vDRBlgaSF0WuYrW7QipGDVLO.Re86vycJMMuyG60hjl_.zRgMv2HRYZ.kZbS_.eZ0cnEE0aPKvzuZj.sb3NhZi3pqbVkwLOVFpSgknFd4Uv4jK2Rb7DvXocnoq_v8i2_w6mHztz5zg1tWVrwzmeTwMNfOTGn7IX_zsRlNFbcv3QsiNBQlVtMG41BojQ5RHSBey_o2xdn3N4TBh4r4vIWeYvvantnoNMNuEZ_IY3mHhe7vGGc6BIcytSWM4hTGr603UeF0Xm1ExzOyxbcQ3RHw2nvsqktjTM96TpFpv3syRcRtd0k4Xgy15ihDVlVaCMFhrsIgWKTR9BKOuQM66vpusXoDUFPZ5d6rN9GzjBqgx52QeCSOO6bGoxbGbEQ7mxMHfwZmgLwFykCFMAkeFXOOK1a8fpJ2rrwLctYidrP2BmdCwDT1agQ2N.1Gs5lb3MwlfZw4vCeJZM8cZNBDxQDSGUT5POACMAgnyViwWE5L5lRisAmBR..nR.ktE1i3hUboCVrpHX5jC_dfqhvB.7ZRPKZMfbi8YUWjvnV_a7_14m98F1rsxTU99Oyo3paE_Pl.Aq7ihvdC07dxdb5t6eeomNWH9UaN2gHs2SpGXo3LWyVO6JOvI3_hzYBJEhQmzuNPKcvQS4hqclXCIZFvHv4SFvIBGbhOp0cFK_MuAMowrL6CCtdutpDSQkTjBU2I2R9vvltsv1JM6ChKZg1kVpioJZkrBMxXu8R0O.PM395ui6nMTiz8U20swAhV_Se1OtKW3afkg59Q7DGGTZfRUgwafr5ltE1jmmCyAeqktg1kTsXvmiM93edRQbvmLpx4qVK37y3hNSWSX_7CR.g0t19Abs6wGpBCEbKMkNQhF_NMgH0u6SqD4SWygVuKroL2Zxzc0Ct0sPgP5gA0.p9FtHODxg.cLQGQzWlLdVnVebHrOnqrtDzrmwP14k0ndMkMnpUu5rECOEkBq_NJbkpReOdw31bJBtgcbFfCpPD6t1NqQWjHzt92ZKbTIEkeS4iTbCbKKk9MR5SS_OBcq1YJnywCrw17wZ_RKP.TuyRLViOe7Bh5KkoDVfenjkv7BFPzCoqEWzh8FaV1.rFx6V2ykTB2.XsndLlmDDsasCVW0lRr4N7heWm7Q3h4AI4iXRB6GpRHDDJ3_tBTEeWb2HDvS2rmXu.3z_do_R.nZfZlU96XUf3raAqY7pQ8lCE6NOQue.xwV3lNSeBjuSKGpe1SBhhU.WEW0NQlHCQUZyKvXHtnGPC.nB1ie5YDtcQv_44gQRM8tiLOv_BbXMqH9f0ObyYktYgPhHpte3z5AIKl01Q78Whgio8Ho.YVJQCMpdl4V5ZhKiO4gQ6gUTCQybnSrzckuQDa9CLwCzdTpFMAMWOd0k_YaDTALk8zb3KsmZXZCj2H78kl182Ay7cqlS7Ykcy1tfG4Ezm5dKX8l2tC0ohTj7MgqnR5Md6jmCfBTIg6nTQwCV1.pe1q5D8UvjoECBGSbtjfpZMRbxnEZRtAxDUkxDWSTVGveYw6sLUPnx1Q.P2.MPB5J.O89dHqXiwyFqvlwsV0OWwrj7yoLSqf1kLkho9HCTp5xQBS27lkIZKDzznwjkGUEfR7yxXarICMknYZyjKLP4ygMh60pbI8_LKacb9gTt349cFcdq.AWlxgZnaj0nhSBv74hxkNtq5KJHSXH9qgeoYCXSn2DA9lrYNCcdEy27s97nfKp3ad0iR9Tz2HoElVCy3Nvq5oO6Sj9Zkobi_ut_.djCszceti7piMjO6Odp_aaOAC0ZcQ9tqXEgPgvz3tY0w8tPqp0aeifdP4D7x4pCKEwNrIRUMRXQJo1J93aHTr5uXYx7rWPbzbTjksrD2pSfvUT4ek9rLCSEaM_GSaFjPmkGigJZsidV7tJmTtVQrSm1lvU._zzFCXpniB7HKo2Rshm86mRnYudHdce0wTAjoYHNmJmQx1oz2yu9yYhybI5OliC6EiIy9s1N2KBvv1vq5g4Xz4VJvcrRUEIYPjxTP1uptydKl2ie3Y2LAla2JjkxCv1P5Jo68b.vRmt8VBN5w5XEWcg6W6nKeLt9yPJGbyTxkR5mbSVDCOg6D8ncoQ_PtJriMEs84uj0LLxznLe2WlMcl0qAK1o8pDkZrDmAYFZiEPuNYmGFGB7et7VXCo3KTHFUauLnpZLjYqSsukToe7W9CiNkCoErUhELlD6O3hAZQxMHxoV_n.BRdT9tn_grQFrEUapjOjin21v0dw2AsgI6YV5h2.11LqV7YD7jCYd0A46pxulTSEgEEMny1OTS1lEB.YknfqvSGvAS5Yxi5C4haGW8rP.Byn4BXmF1fKlgyggHqH7v.2kavr4kBXBPkP7lL1x8QgmCIuLpzKYLtm.Y4LTzDNCkTKzU44SYUHaY_M4wEm9xWAar52HFK4t1yUz_yZqVlht.JYy_pUpvDwN2uQYd0sHG8jWM70ZL.weDs70uNb5jqAZE1sRb8KK2Nq2pJeBRBFE5Gd3p5XGWr2LOnCZmKtELTrvRVTamVd9tX84X05E9J3rCMnklw.Vfs_BVYOZbS9bOLOdfz.U4TbhF08ZrLQcuJylDu6PL10UjlKIkLKQ_yjXnE667lmQW.Cdfrob6pPerVLOEUHdDemI9.DElbCjBux1WrY9QkHb7GuOYUv8p2UrXG0kSuu8DP6F8Ibg4KgGXqlTjReY5Tkp44k53M70TUEl8ExAiBmwSarhqokHCEQW.yvmYSyBT_T0GGwlryVsH8evwSTz252aafpHBlCvD7JMVYyMql1vurEE525Eml1yFiJNjQhReRJ1DSZWAEGQ0CGgpbyTK570a0YCSFH2B_h9vS0SGsfssZ3UNHUd5WmbZEGwbSNGVIItYNmLseIOgCGnoXHG_FYKF5VQ43UkL10YIe_Z2Bab1HYc1nOXKibVx1feC4kjDFUS_gWyARzYAPmQwq0bNzOrdPDQzNE2ZKHFLQ7pM.Q9rZwNeh9zv8sT3KOdAvTW3sKOT7MhsG4EIBAryU_1zDe4xgyn8MhVffMBeSX6FuiF8.HgFxumEyGVB0eDIEO853h2gGHH4kGYiKte1czRMXpUCdqz8GalJLq2gN4hqVI8.c_A3PufYHAAhvWLBcdFrZr28zeYDJWJlXBU21kenSH14_AwKOSTLS8_zIy_FWy24hwTpYFvRiNiErs1L1tHvx2.IrYVkUISgBFaaeNGEtd4u8J2r9H28xUq4OEZvgdesnyMhIcWIoRBSJcQDbfNIjJZKb1PUL16by.LyI8TX00eUaB02hRdmAnvFjTc2K2X.f7t_9g9rgdY6e0xd27U5y5H5FIrswPnfh.saA_wGsBLTIda.fAxsPLaS1VjxKcbc9j5vD0ChCT9Tv4rQk7TogdY5qIlx.Ryu_SfhIv9seLZtfKJFA2MMqIXFkA2f14PDNewhurcZW9dGcjDDgWdgoGhW3vqyEWBrReCBFgd2QO3r7APG_hG0CJ8j0w6RClufUkoRIVUnnUMDFFFpKksWscpmtQRDHCFgTEsqZm1rHqFn6r232l_WfVYKXOY41fbPDyMlDzlYTkFD_tmUreuGCoD9H6yGphXxa82f.v8n2j3xWIC0dsKlOpFnJ5w1k4RUelzy4DChPyfPHRtzfpheI.nnnU2y6TqSuHEMoYlOvBC9Ds8TInuG7gl0K6I1nFG3QA2Gc5BWB2WS0S5Xkk0Du9SGO.LyOYnoCvBSeDZYfjpPiBiaRgasayrJjID5BuLsZDreSJYiHhQR_ygqJ0q7Tij.6V7wrMo5IMJ3wDO3jhH..to2m92Ld4kCDJQ6qwQQ2KljlkVp9jDV4yE8A',
        '04e1128ef6676760ee5fc47cfab9aa30f90caad855537fcc524cae4e1886d278': 'a2c215a69ee6993dce4a86677e3157b3',
        '10b09292fcceecd2b340ea017f30a6826b4d0c5cf90a6ed156f04b0112888bf4': 'KqalKGNIPHhm-1-873b07293d5c10bd',
    }

    response = requests.post('https://hidemy.io/ru/proxy-list/', params=params, cookies=cookies, headers=headers,
                             data=data)
    proxy_list = []
    soup = BeautifulSoup(response.text, 'lxml')
    for row in soup.select('.table_block tbody tr'):
        proxy_list.append(f'{row.select("td")[0].text}:{row.select("td")[1].text}')
    return proxy_list
