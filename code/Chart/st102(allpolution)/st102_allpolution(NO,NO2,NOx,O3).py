import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.dates import YearLocator

data = pd.read_csv('data_hourly_clean_daily.csv')
data["datetime"] = pd.to_datetime(data["datetime"])

station102 = data.loc[data["station_id"] == 102].groupby([pd.Grouper(freq="Y", key="datetime")]).mean()
NO_102_data = station102['NO']
NO2_102_data = station102['NO2']
NOx_102_data = station102['NOx']
O3_102_data = station102['O3']
fig, ax = plt.subplots(figsize=(10, 6))
ax = plt.gca()
fig.set_facecolor('lightgrey')

plt.plot(O3_102_data.index, O3_102_data, label='O3', color='crimson')
plt.plot(NO_102_data.index, NO_102_data, label='NO', color='cyan')
plt.plot(NO2_102_data.index, NO2_102_data, label='NO2', color='purple')
plt.plot(NOx_102_data.index, NOx_102_data, label='NOx', color='orange')
years = NO_102_data.index.year
plt.xticks(NO_102_data.index, years, rotation=45)
plt.xlabel('Date')
plt.ylabel('Value')
plt.title('Station 102 all polution')
plt.legend()
plt.grid(True)

plt.savefig("st102(allpolution(NO,NO2,NOx,O3)).png")
plt.show