from flask import Flask
from flask_restful import Resource, Api, reqparse


wind_speeds = {
    '01-04-2021': {'wind': 5.6, 'lower': 1.4, 'upper': 6.8},
    '02-04-2021': {'wind': 4.6, 'lower': 0.4, 'upper': 6.8},
    '03-04-2021': {'wind': 4.6, 'lower': 3.5, 'upper': 6.8},
    '04-04-2021': {'wind': 5.2, 'lower': 2.4, 'upper': 6.8},
    '05-04-2021': {'wind': 5.9, 'lower': 2.4, 'upper': 6.8},
    '06-04-2021': {'wind': 3.5, 'lower': 2.4, 'upper': 6.8},
    '07-04-2021': {'wind': 6.1, 'lower': 2.4, 'upper': 6.8},
    '08-04-2021': {'wind': 4.1, 'lower': 2.4, 'upper': 6.8},
    '09-04-2021': {'wind': 5.9, 'lower': 2.4, 'upper': 6.8},
    '10-04-2021': {'wind': 3.6, 'lower': 2.4, 'upper': 6.8},
    '11-04-2021': {'wind': 5.6, 'lower': 1.6, 'upper': 6.8},
    '12-04-2021': {'wind': 5.6, 'lower': 3.1, 'upper': 6.8},
    '13-04-2021': {'wind': 5.6, 'lower': 1.1, 'upper': 6.8},
    '14-04-2021': {'wind': 5.6, 'lower': 1.4, 'upper': 6.8},
    '15-04-2021': {'wind': 5.6, 'lower': 3.4, 'upper': 6.8},
    '16-04-2021': {'wind': 5.6, 'lower': 0.6, 'upper': 6.8},
    '17-04-2021': {'wind': 5.6, 'lower': 1.8, 'upper': 6.8},
    '18-04-2021': {'wind': 5.6, 'lower': 2.4, 'upper': 7.8},
    '19-04-2021': {'wind': 5.6, 'lower': 2.4, 'upper': 9.8},
    '20-04-2021': {'wind': 5.6, 'lower': 2.4, 'upper': 9.1},
    '21-04-2021': {'wind': 5.6, 'lower': 2.4, 'upper': 8.8},
    '22-04-2021': {'wind': 5.6, 'lower': 2.4, 'upper': 11.8},
    '23-04-2021': {'wind': 5.6, 'lower': 2.4, 'upper': 6.5}
}

app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug=True)
