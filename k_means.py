'''
Алгоритм k-means
================
- Шаг 1: Выбираем число кластеров, k
- Шаг 2: Выбираем k случайных значений
- Шаг 3: Создать k кластеров
- Шаг 4: Вычисляем новый центроид каждого кластера
- Шаг 5: Оценить качество каждого кластера
- Шаг 6: повторяем шаги

Ссылки на источники:
--------------------
- https://proglib.io/p/obyasnite-tak-kak-budto-mne-10-let-prostoe-opisanie-populyarnogo-algoritma-klasterizacii-k-srednih-2022-12-07
- https://en.wikipedia.org/wiki/K-means_clustering
'''

import numpy as np
import pandas as pd


def get_random_index(data, n):
    ''' Возвращает n рандомных индексов из массива data.\n 
        n - желаемое количество кластеров (количество разбиений)
    '''

    return (np.random.randint(0, data, size=n))


def get_clusters(data, centers, lebels):
    ''' Делает перерасчет центра кластера для каждой точки.\n
        centers — текущие центры кластеров массива data\n
        lebels — названия кластеров
    '''

    A = data.iloc[:, 0:2].to_numpy()
    B = centers.iloc[:, 0:2].to_numpy()

    distances = np.sqrt(((A - B[:, np.newaxis]) ** 2).sum(axis=2))

    return ([lebels[i] for i in distances.argmin(axis=0)])


def get_centers(data):
    ''' Возвращает новый центр кластера '''

    return data.groupby("cluster").mean().reset_index(drop=True)


def k_means(data: pd.DataFrame, count_clusters: int, lebels: list) -> pd.DataFrame:
    ''' Алгоритм кластеризации данных в 2D '''

    # Делаю парсинг данных
    data = pd.concat([data, pd.DataFrame(
        np.zeros(data.shape[0], dtype=int), columns=['cluster'])], axis=1)

    end: bool = False
    data = pd.DataFrame(data, columns=('Широта', 'Долгота', 'Цена_м^2'))

    # Вычисляю начальные значения
    indexes = get_random_index(data.shape[0], count_clusters)
    centers = data.iloc[indexes, 0:2]
    data.loc[indexes, 'cluster'] = lebels
    data.cluster = get_clusters(data.iloc[:, 0:2], centers, lebels)
    centers = get_centers(data)

    # Делаю перерасчет центров кластеров.
    # WCSS (within-cluster sum of squares) – cумму квадратов внутрикластерных расстояний до центра кластера.

    # Если кластеры перестают меняться, то это значит, что алгоритм сошелся и мы останавливаем процесс.
    # Затем мы выбираем кластеры с наименьшим WCSS. Они и становятся нашими финальными кластерами.

    while not end:
        old_clusters = data.cluster
        data.cluster = get_clusters(data.iloc[:, 0:2], centers, lebels)

        end = np.array_equal(data.cluster, old_clusters)
        centers = get_centers(data)

    # Конвертирую столбец cluster str -> int и сортирую по возрастанию
    data['cluster'] = pd.to_numeric(data['cluster'])
    data.sort_values(by='cluster')

    return data
