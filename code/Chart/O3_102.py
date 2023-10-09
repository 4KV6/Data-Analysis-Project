import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.dates import YearLocator

data = pd.read_csv('data_hourly_clean_daily.csv')
data["datetime"] = pd.to_datetime(data["datetime"])

station102 = data.loc[data["station_id"] == 102].groupby([pd.Grouper(freq="Y", key="datetime")]).mean()
station256 = data.loc[data["station_id"] == 256].groupby([pd.Grouper(freq="Y", key="datetime")]).mean()
O3_102_data = station102['O3']
O3_256_data = station256['O3']
plt.figure(figsize=(10, 6))
plt.plot(O3_102_data.index, O3_102_data, label='st102', color='blue')
plt.plot(O3_256_data.index, O3_256_data, label='st256', color='red')
years = O3_102_data.index.year
plt.xticks(O3_102_data.index, years, rotation=45)
plt.xlabel('Date')
plt.ylabel('Value')
plt.title('O3 Levels for Station 102 and Station 256')
plt.legend()
plt.grid(True)
plt.savefig("st102(O3).png")