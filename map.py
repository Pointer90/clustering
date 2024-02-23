'''
 Map
 ---
 Предоставляет интерфейс кастомизации для работы с картой
'''
import folium
import pandas as pd

# переводит CLUSTER_INDEXES в цвета для добавления цветных маркеров
TO_COLORS = {
    '0': 'red',
    '1': 'green',
    '2': 'blue',
    '3': 'white',
    '4': 'black',
    '5': 'yellow',
    '6': 'orange',
    '7': 'brown'
}


def addMarkers(data: pd.DataFrame, map: object) -> None:
    ''' Добавляет цветные маркеры на карту '''

    for row in data.itertuples():
        folium.Marker([row.Широта, row.Долгота], icon=folium.Icon(color=TO_COLORS[row.cluster])).add_to(map)
