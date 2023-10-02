import pandas as pd

"""
อธิบายข้อมูล ของรายชั่วโมง
และรายวัน และทำเป็นไฟล์
"""

data_daily = pd.read_csv("archive\stations_daily_merge.csv", index_col=0)

group_daily = data_daily.groupby("network_id")
#print(group_daily.describe())
group_daily.describe().to_csv("describe daily.csv")

data_hourly = pd.read_csv("archive/stations_hourly_merge.csv", index_col=0)
group_hourly = data_hourly.groupby("network_id")
group_hourly.describe().to_csv("describe houry.csv")