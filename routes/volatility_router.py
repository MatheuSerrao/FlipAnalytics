from app import app
from flask import jsonify, request
from indicators.volatility_utils import gaussian_smooth, max_min_locals


class VolatilityRouter():

    base_path = '/volatility'

    def apply(self):
        @app.route(f'{self.base_path}/min-max-locals', methods=['GET'])
        def max_min_locals_route():
            data = request.json
            klines = data['klines']
            res = max_min_locals(klines)
            return jsonify(res)

        @app.route(f'{self.base_path}/gaussian-smooth', methods=['GET'])
        def gaussian_smooth_route():
            data = request.json
            klines = data['klines']
            att = data['att'] if 'att' in data else 'highestPrice'
            sigma = data['sigma'] if 'sigma' in data else 1
            res = gaussian_smooth(klines, sigma, att)
            res = max_min_locals(res, 'gfs')
            res = {
                'max': max_min_locals(res['max'], 'highestPrice')['max'],
                'min': max_min_locals(res['min'], 'lowestPrice')['min'],
            }
            return jsonify(res)


volatility_router = VolatilityRouter()
