import pandas as pd
import numpy as np
import os
import pytz
import datetime

"""
ทดสอบการเปลี่ยน format ของ datetime
"""

fileListDataHourly = os.listdir("data_group_hourly/")
stationData = pd.read_csv("archive\stations_rsinaica.csv")

ListDataStationID = stationData.loc[stationData["station_id"] == 32]
DataThatID = pd.read_csv("data_group_hourly/stations_hourly_id32.csv", index_col=1)
DataThatID.index = pd.to_datetime(DataThatID.index)
DataThatID.drop(DataThatID.columns[0], axis=1, inplace=True)
infer_dst = np.array([False] * DataThatID.shape[0])
DataThatID.index = DataThatID.index.tz_localize("America/Mexico_City", nonexistent='shift_forward', ambiguous=infer_dst)
DataThatID.info()
DataThatID.index = DataThatID.index.tz_convert("UTC")
print(DataThatID)
for name in pytz.country_timezones["MX"]:
    print(name, ":", pytz.timezone(name).localize(datetime.datetime(2015,1,1)).strftime('%z'))

print(ListDataStationID["timezone"].values[0])