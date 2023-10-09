import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.dates import YearLocator

data = pd.read_csv('data_hourly_clean_daily.csv')
data["datetime"] = pd.to_datetime(data["datetime"])

station256 = data.loc[data["station_id"] == 256].groupby([pd.Grouper(freq="Y", key="datetime")]).mean()
NO_256_data = station256['NO']
NO2_256_data = station256['NO2']
NOx_256_data = station256['NOx']
O3_256_data = station256['O3']
fig, ax = plt.subplots(figsize=(10, 6))
ax = plt.gca()
fig.set_facecolor('lightgrey')

plt.plot(O3_256_data.index, O3_256_data, label='O3', color='crimson')
plt.plot(NO_256_data.index, NO_256_data, label='NO', color='cyan')
plt.plot(NO2_256_data.index, NO2_256_data, label='NO2', color='purple')
plt.plot(NOx_256_data.index, NOx_256_data, label='NOx', color='orange')
years = NO_256_data.index.year
plt.xticks(NO_256_data.index, years, rotation=45)
plt.xlabel('Date')
plt.ylabel('Value')
plt.title('Station 256 all polution')
plt.legend()
plt.grid(True)

plt.savefig("st256(allpolution(NO,NO2,NOx,O3)).png")
plt.show