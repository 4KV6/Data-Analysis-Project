import numpy as np
import pandas as pd

"""
ดูข้อมูลคร่าวๆ
"""

weather_hourly = pd.read_csv('archive/stations_daily.csv')
print("rows & columms :")
print(weather_hourly.shape)
weather_hourly.info()
print("=== head ===")
print(weather_hourly.head())
ListStation = weather_hourly.groupby("station_id")
print("=== station id ===")
print(ListStation.count())
ListStation.count().to_csv("Station count daily.csv")