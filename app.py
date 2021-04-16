from flask import Flask, request
from flask_cors import CORS
from flask_restful import Resource, Api, reqparse

import pandas as pd
from datetime import datetime

df = pd.read_csv('./wind_forecast.csv', usecols=['ds', 'yhat', 'yhat_lower', 'yhat_upper'])
df = df.loc[df['ds'] > '2020-12-31']
wind_speeds_temp = df.to_dict(orient='index')

wind_speeds = dict()
temp_keys = wind_speeds_temp.keys()
for old_key in temp_keys:
    wind_speeds[wind_speeds_temp[old_key].get('ds')] = {
        'wind': wind_speeds_temp[old_key].get('yhat'),
        'lower': wind_speeds_temp[old_key].get('yhat_lower'),
        'upper': wind_speeds_temp[old_key].get('yhat_upper')
    }


app = Flask(__name__)
api = Api(app)
CORS(app)


class Wind(Resource):
    def get(self, date):
        date = datetime.fromtimestamp(date/1000.0).strftime('%Y-%m-%d')
        print(date)
        return wind_speeds[date]

api.add_resource(Wind, '/wind-speed-data/<int:date>')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
