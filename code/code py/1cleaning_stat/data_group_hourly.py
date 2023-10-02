import pandas as pd

"""
แยกไฟล์แต่ละสถานี ของข้อมูลรายชั่วโมง
"""

data_import = pd.read_csv("archive/stations_hourly.csv")
stationId = data_import.groupby("station_id")
for station_id_num in data_import["station_id"].drop_duplicates().values :
    ListDataId = data_import.loc[ data_import["station_id"] == station_id_num ]
    ListDataId = ListDataId.rename(columns={0 : "previous_index"})
    filename = "stations_hourly_id" + str(station_id_num)
    ListDataId.to_csv("data_group_hourly/" + filename + ".csv")

print(ListDataId.head())