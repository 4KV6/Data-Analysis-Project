import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.dates import YearLocator

data = pd.read_csv('data_hourly_clean_daily.csv')
data["datetime"] = pd.to_datetime(data["datetime"])

station102 = data.loc[data["station_id"] == 102].groupby([pd.Grouper(freq="Y", key="datetime")]).mean()
CO_102_data = station102['CO']

plt.figure(figsize=(10, 6))

plt.plot(CO_102_data.index, CO_102_data, label='CO', color='darkgreen')
years = CO_102_data.index.year
plt.xticks(CO_102_data.index, years, rotation=45)
plt.xlabel('Date')
plt.ylabel('Value')
plt.title('Station 102 all polution')
plt.legend()
plt.grid(True)
plt.savefig("st102(allpolution(CO)).png")
plt.show