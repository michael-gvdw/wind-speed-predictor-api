from flask import Flask
from flask_restful import Resource, Api, reqparse

import pandas as pd

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

@app.route('/get-wind-speed-data')
def get_wind_speed_data():
    return wind_speeds


if __name__ == '__main__':
    print()
    app.run(debug=True)
