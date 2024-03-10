import folium

from map import addMarkers
from loader import load, save_to_excel
from two_gis_parser import parse_pages
from k_means import k_means

import pandas as pd

# Глобальные настройки
# Желаемые индексы для кластеров
CLUSTER_INDEXES = [0, 1, 2]
# Используемые цвета на карте
COLORS = ['red', 'orange', 'green']
# Начальный зум для карты
START_ZOOM = 12
# Координаты г.Челябинска
START_LOCATION = [55.159901, 61.402547]

if __name__ == '__main__':

    # Подтягиваю данные из 2gis
    save_to_excel(parse_pages(49), '2gis.xlsx')

    # Путь до файла и их имена
    # file_path = 'Data.xlsx'
    file_path = '2gis.xlsx'
    map_name = 'Map.html'

    # Кластеризация
    data = k_means(load(file_path), 3, CLUSTER_INDEXES)

    # Поиск средней цены в каждом кластере и назначение ему цвета в зависимости от цены
    means = data.groupby('cluster')['Цена_м^2'].mean().sort_values().to_dict()
    colors_map = dict()
    for elem in means.keys():
        colors_map[elem] = COLORS.pop()

    # Cоздаю карту, добавляю маркеры и сохраняю
    map = folium.Map(location=START_LOCATION, zoom_start=START_ZOOM)
    addMarkers(data, map, colors_map, means)
    map.save(map_name)

    # Сохраняю результаты в excel
    save_to_excel(data, 'Result.xlsx')