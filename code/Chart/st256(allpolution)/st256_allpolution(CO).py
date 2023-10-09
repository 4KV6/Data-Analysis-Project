import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.dates import YearLocator

data = pd.read_csv('data_hourly_clean_daily.csv')
data["datetime"] = pd.to_datetime(data["datetime"])

station256 = data.loc[data["station_id"] == 256].groupby([pd.Grouper(freq="Y", key="datetime")]).mean()
CO_256_data = station256['CO']

plt.figure(figsize=(10, 6))

plt.plot(CO_256_data.index, CO_256_data, label='CO', color='darkgreen')
years = CO_256_data.index.year
plt.xticks(CO_256_data.index, years, rotation=45)
plt.xlabel('Date')
plt.ylabel('Value')
plt.title('Station 256 all polution')
plt.legend()
plt.grid(True)
plt.savefig("st256(allpolution(CO)).png")
plt.show