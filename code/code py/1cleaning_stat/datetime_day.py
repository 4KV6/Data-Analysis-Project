import pandas as pd

"""
แปลง datetime ของไฟล์รายชั่วโมง
"""

data_daily = pd.read_csv("archive\stations_daily_merge.csv", index_col=0)
data_daily["datetime"] = pd.to_datetime(data_daily["datetime"])
print(data_daily["datetime"])
data_daily.to_csv("archive\stations_daily_merge.csv")