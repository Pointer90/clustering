'''
2gis
---
Набор функций для парсинга цен на недвижимость города Челябинск из карт 2gis
'''

import requests
import pandas as pd

# Названия колонок, которые будут в таблице
COLUMNS = ['address', 'lat', 'lon', 'type', 'count_rooms',
           'lvl', 'square', 'price', 'price_per_meter']


def parse_page(apartments: dict) -> list[dict]:

    ''' Парсит страницу из 2gis'''
    
    result = []

    for index in range(0, len(apartments)):

        address = []

        # Убираю лишние символы из названия
        for elem in apartments[index]['building']['adm_div']:
            address.append(elem['name'].replace('\xa0', ' '))

        try:
            address.append(apartments[index]['building']['address_name'])
        
            # Какой тип студия или квартира?
            if 'Студия' in apartments[index]['product']['name']:
                type = 'Студия'
                square = apartments[index]['product']['attributes'][1]['value']
                lvl = apartments[index]['product']['attributes'][2]['value']
                count_rooms = 1
            else:
                type = apartments[index]['product']['attributes'][0]['value']
                count_rooms = apartments[index]['product']['attributes'][1]['value']
                square = apartments[index]['product']['attributes'][2]['value']
                lvl = apartments[index]['product']['attributes'][3]['value']

            # Добавляю информацию о квартире в список
            result.append(
                {
                    'Адрес': ', '.join(address),
                    'Широта': float(apartments[index]['building']['lat']),
                    'Долгота': float(apartments[index]['building']['lon']),
                    'Тип': type,
                    'Комнаты': int(count_rooms),
                    'Этаж': int(lvl),
                    'Площадь': float(square),
                    'Цена': float(apartments[index]['offer']['price']),
                    'Цена_м^2': int(float(apartments[index]['offer']['price_per_meter_value']['fixed']['value'])),
                }
            )
        # Если не получилось отпарсить запись, то, просто, не добавляю эту информацию в итоговый список
        except Exception:
            continue    

    return result


def parse_pages(count_pages: int) -> pd.DataFrame:

    ''' Парсит n страниц из 2gis по данным из (ДомКлик, Циан, Самолет плю)'''

    result = []

    providers = ['ДомКлик', 'Циан', 'Самолет плюс']
    provider = {
        'ДомКлик': '0KHQsNC80L7Qu9C10YIg0J_Qu9GO0YE,0JTQvtC80LrQu9C40Lo',
        'Циан': '0KbQmNCQ0J0',
        'Самолет плюс': '0KHQsNC80L7Qu9C10YIg0J_Qu9GO0YE'
    }

    for name in providers:
        for page in range(1, count_pages + 1):
            url = f'https://market-backend.api.2gis.ru/5.0/realty/items?platform_code=34&category_ids=70241201812761646&point1=61.097838415461034,55.32328219224489&point2=61.70757958453897,54.991495807755115&page={page}&locale=ru_RU&page_size=20&provider={provider[name]}'
            r = requests.get(url)

            if r.status_code == 200:
                data = r.json()
                apartments = data['result']['items']

                parsed_apartments = parse_page(apartments)
                result.extend(parsed_apartments)

    return pd.DataFrame(result)