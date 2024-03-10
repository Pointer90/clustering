'''
 Map
 ---
 Предоставляет интерфейс кастомизации для работы с картой
'''
import folium
import pandas as pd

def addMarkers(data: pd.DataFrame, map: object, colors: dict, popup: dict) -> None:
    ''' Добавляет цветные маркеры на карту '''

    for row in data.itertuples():
        folium.Marker(
            [row.Широта, row.Долгота],
            icon=folium.Icon(color=colors[row.cluster]),
            popup=int(popup[row.cluster]),
        ).add_to(map)
