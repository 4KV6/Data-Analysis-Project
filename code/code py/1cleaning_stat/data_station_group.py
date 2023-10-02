import pandas as pd
import numpy as np

"""
จับกลุ่มว่า สถานีไหนอยู่ในโครงข่าย network ใด
"""

Data_station = pd.read_csv("archive\stations_rsinaica_fixed.csv")

stationNetWorkID = Data_station["network_id"]
stationID = Data_station["station_id"]
stationNetwork = Data_station["network_name"]

data_group = Data_station[["network_id","network_name","station_id"]]
data_group.sort_values("network_id",inplace=True)
data_group.index = np.arange(0,data_group.shape[0])
data_group.to_csv("archive/staion_group_networkID.csv")
data_group.to_json("archive/staion_group_networkID.json")
print(data_group)