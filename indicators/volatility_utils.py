import numpy as np
from scipy.ndimage import gaussian_filter
from scipy.signal import argrelextrema


def max_min_locals(data: list, att='closePrice'):
    try:
        prices = np.array([float(kline[att]) for kline in data])
        (max_index,) = argrelextrema(prices, np.greater)
        (min_index,) = argrelextrema(prices, np.less)
        max_index = max_index.tolist()
        min_index = min_index.tolist()
        res = {
            'max': [data[index] for index in max_index],
            'min': [data[index] for index in min_index]
        }
        return res
    except ValueError as e:
        print("Bad Request")


def gaussian_smooth(data: list, sigma: int, att='closePrice'):
    try:
        prices = np.array([float(kline[att]) for kline in data])
        gfs = gaussian_filter(prices, sigma, 0)
        for index, kline in enumerate(data):
            data[index]['gfs'] = gfs[index]
        return data
    except ValueError as e:
        print("Bad Request")


def gaussian_smooth_typical_price(data: list, sigma: int):
    try:
        prices = np.array([((float(kline['highestPrice'])+float(
            kline['lowestPrice'])+float(kline['closePrice']))/3) for kline in data])
        gfs = gaussian_filter(prices, sigma, 0)
        for index, kline in enumerate(data):
            data[index]['gfs'] = gfs[index]
        return data
    except ValueError as e:
        print("Bad Request")
