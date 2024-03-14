# Алгоритм кластеризации k-means и web parsing
## Установка и использование
> - Рекомендуется использовать Python v3.11.1
> - Установить виртуальное окружение venv или его аналоги
>   - Для установки виртуального окружения venv необходимо в консоли набрать `python -m venv venv`
>   - Для активации виртуального окружения в ОС Windows `call venv\Scripts\activate.bat` и для ОС Linux `source venv/bin/activate`, если активация прошла успешно, то должна появиться преписка (venv) возле пути к файлу в консоле.
>   - Установка библиотек для работы `pip install -r requirements.txt`
> - Использовать парсер, если необходимы данные
>   - В файле main.py необходимо запустить функцию `save_to_excel(parse_pages(42), 'name_file.xlsx')` для получения excel с данными
> - Использовать алгоритм кластеризации
>   - `k_means(load('name_file.xlsx'), int_number_clusters, list_cluster_indexes)` кластеризует данные
>   - `save_to_excel(data, 'result_name.xlsx')` сохраняет кластеризованные данные в формате xlsx

### Важно!
> - Парсер и кластеризация могут работать независимо друг от друга, но названия полей обрабатываемой таблицы должны совпадать
> - Количество кластеров, цвета маркеров для карты и CLUSTER_INDEXES должны быть одинаковой длинны (размера)
> - Парсер работает только с картой 2gis

## Ссылки на ресурсы
> - [Python v3.11.1] https://www.python.org/downloads/release/python-3111/
> - [Статья о кластеризации № 1] https://proglib.io/p/obyasnite-tak-kak-budto-mne-10-let-prostoe-opisanie-populyarnogo-algoritma-klasterizacii-k-srednih-2022-12-07
> - [Статья о кластеризации № 2] https://en.wikipedia.org/wiki/K-means_clustering
> - [Пример работы с библиотекой folium] https://www.youtube.com/watch?v=9nmvDPiBtcc
