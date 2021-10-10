from flask import request, jsonify
from app import app
from indicators.means_utils import mean_average, weighted_mean_average


class MeansRouter():
    base_path = '/means'


    def apply(self):
        @app.route(f'{self.base_path}/sma', methods=['GET'])
        def mean_average_route():
            data = request.json
            window = data['window']
            klines = data['klines']
            res = mean_average(klines, window)
            return jsonify(res)

        @app.route(f'{self.base_path}/wma', methods=['GET'])
        def weighted_mean_average_route():
            data = request.json
            window = data['window']
            klines = data['klines']
            weight = data['weight']
            res = weighted_mean_average(klines, window, weight)
            return jsonify(res)


means_router = MeansRouter()
