import pandas 
import numpy 
import requests
import binance_connect
import time

# get and transform data 
def get_and_transform_data(symbol,timeframe,number):
    raw_data = binance_connect.get_candleSticks_data(symbol,timeframe,number)
    df = pandas.DataFrame(raw_data)
    df['time'] = pandas.to_datetime(df['date'], unit='ms')
    df['close_time'] = pandas.to_datetime(df['close_time'], unit='ms')
    df['RedOrGreed'] = numpy.where(df['close'] > df['open'], 'GREEN', 'RED')

    return df