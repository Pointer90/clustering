import folium

from map import addMarkers
from loader import load, save_to_excel
from k_means import k_means

# Глобальные настройки
# CLUSTER_INDEXES должны быть обязательно числа в формате str!!!
CLUSTER_INDEXES = ['0', '1', '2']
START_ZOOM = 12
START_LOCATION = [55.159901, 61.402547]

if __name__ == '__main__':

    # Путь до файла
    file_path = 'Data.xlsx'

    # Производится кластеризация
    data = k_means(load('Data.xlsx'), 3, CLUSTER_INDEXES)

    # Cоздаю карту, добавляю маркеры и сохраняю
    map = folium.Map(location=START_LOCATION, zoom_start=START_ZOOM)
    addMarkers(data, map)
    map.save('test.html')

    # Сохраняю результаты в excel
    save_to_excel(data, 'Result.xlsx')
