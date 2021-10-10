def mean_average(data: list, n_series: int):
    try:
        base = int((n_series - 1) / 2)
        center = base
        lenght = len(data)
        start = (center - base)
        end = (center + base + 1)
        res = []

        for i in range(base):
            res.append(None)

        while end < lenght:
            windows = data[start:center] + data[center:end]
            ma = sum(float(kline['closePrice']) for kline in windows) / n_series
            obj = {
                'point': float(data[center]['closePrice']),
                'datetime': data[center]['openTime'],
                'ma': ma
            }
            res.append(obj)
            center += 1
            start = (center - base)
            end = (center + base + 1)

        for i in range(base):
            res.append(None)

        return res
    except ValueError:
        print("Bad Request")


def weighted_mean_average(data: list, n_series: int, weight: str = 'volume'):
    try:
        base = int((n_series - 1) / 2)
        center = base
        lenght = len(data)
        start = (center - base)
        end = (center + base + 1)
        res = []

        for i in range(base):
            res.append(None)

        while end < lenght:
            windows = data[start:center] + data[center:end]
            wma = sum((float(kline['closePrice']) * float(kline[weight])) for kline in windows) / n_series
            obj = {
                'point': float(data[center]['closePrice']),
                'datetime': data[center]['openTime'],
                'ma': wma
            }
            res.append(obj)
            center += 1
            start = (center - base)
            end = (center + base + 1)

        for i in range(base):
            res.append(None)

        return res
    except ValueError:
        print("Bad Request")
