import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.dates import YearLocator

data = pd.read_csv('data_hourly_clean_daily.csv')
data["datetime"] = pd.to_datetime(data["datetime"])

station102 = data.loc[data["station_id"] == 102].groupby([pd.Grouper(freq="Y", key="datetime")]).mean()
station256 = data.loc[data["station_id"] == 256].groupby([pd.Grouper(freq="Y", key="datetime")]).mean()
TMP_102_data = station102['TMP']
TMP_256_data = station256['TMP']
plt.figure(figsize=(10, 6))
plt.plot(TMP_102_data.index, TMP_102_data, label='st102', color='blue')
plt.plot(TMP_256_data.index, TMP_256_data, label='st256', color='red')
years = TMP_102_data.index.year
plt.xticks(TMP_102_data.index, years, rotation=45)
plt.xlabel('Date')
plt.ylabel('Value')
plt.title('TMP Levels for Station 102 and Station 256')
plt.legend()
plt.grid(True)
plt.savefig("st102(TMP).png")