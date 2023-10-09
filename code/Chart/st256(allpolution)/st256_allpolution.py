import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.dates import YearLocator

data = pd.read_csv('data_hourly_clean_daily.csv')
data["datetime"] = pd.to_datetime(data["datetime"])

station256 = data.loc[data["station_id"] == 256].groupby([pd.Grouper(freq="Y", key="datetime")]).mean()
HR_256_data = station256['HR']
PM25_256_data = station256['PM2.5']
PM10_256_data = station256['PM10']
NO_256_data = station256['NO']
NO2_256_data = station256['NO2']
NOx_256_data = station256['NOx']
CO_256_data = station256['CO']
O3_256_data = station256['O3']
TMP_256_data = station256['TMP']
plt.figure(figsize=(10, 6))
plt.plot(HR_256_data.index, HR_256_data, label='HR', color='blue')
plt.plot(PM25_256_data.index, PM25_256_data, label='PM2.5', color='red')
plt.plot(PM10_256_data.index, PM10_256_data, label='PM10', color='green')
plt.plot(TMP_256_data.index, TMP_256_data, label='TMP', color='grey')
years = HR_256_data.index.year
plt.xticks(HR_256_data.index, years, rotation=45)
plt.xlabel('Date')
plt.ylabel('Value')
plt.title('Station 256 all polution')
plt.legend()
plt.grid(True)
plt.savefig("st256(all_Polution).png")
plt.show