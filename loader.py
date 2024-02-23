'''
Loader
------
Предоставляет интерфейс для работы с загрузкой/сохранением данных из/в excel
'''
import pandas as pd

def load(path: str):
    ''' Загрузка файла в формате xlsx '''

# Открываю .xlsx файл и забираю данные с первой страницы
    file = pd.ExcelFile(path)
    data = file.parse(file.sheet_names[0])

# Убираю лишние данные
    data = data.drop(['Цена_м^2', '№', 'Номер_Кластера'], axis=1)

    return data


def save_to_excel(data: pd.DataFrame, path: str) -> None:
    ''' Сохранить данные в Excel файл'''

    data.to_excel(path, index=False)
