import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.dates import YearLocator

data = pd.read_csv('data_hourly_clean_daily.csv')
data["datetime"] = pd.to_datetime(data["datetime"])

station102 = data.loc[data["station_id"] == 102].groupby([pd.Grouper(freq="Y", key="datetime")]).mean()
HR_102_data = station102['HR']
PM25_102_data = station102['PM2.5']
PM10_102_data = station102['PM10']
NO_102_data = station102['NO']
NO2_102_data = station102['NO2']
NOx_102_data = station102['NOx']
CO_102_data = station102['CO']
O3_102_data = station102['O3']
TMP_102_data = station102['TMP']
plt.figure(figsize=(10, 6))
plt.plot(HR_102_data.index, HR_102_data, label='HR', color='blue')
plt.plot(PM25_102_data.index, PM25_102_data, label='PM2.5', color='red')
plt.plot(PM10_102_data.index, PM10_102_data, label='PM10', color='green')
plt.plot(TMP_102_data.index, TMP_102_data, label='TMP', color='grey')
years = HR_102_data.index.year
plt.xticks(HR_102_data.index, years, rotation=45)
plt.xlabel('Date')
plt.ylabel('Value')
plt.title('Station 102 all polution')
plt.legend()
plt.grid(True)
plt.savefig("st102(all_Polution).png")
plt.show