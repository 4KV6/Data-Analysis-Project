import pandas as pd
import os

"""
รวมข้อมูลที่แยกแต่ละสถานี มารวมกัน พร้อมใส่ column network id
"""

group_id = pd.read_csv("archive\staion_group_networkID.csv", index_col=0)
group_id.sort_values("station_id",inplace=True)

ListFileDaily = os.listdir("data_group_daily/")
ListFileHourly = os.listdir("hourly_time_conv/")

dataMergeDay = ""
dataMergeHour = ""

doit = input("do daily (y/n) :").lower()

if doit == "y":
    print("=== start merging data from daily ===")
    lenday = len(ListFileDaily)
    countday = 0

    for file in ListFileDaily:
        if file == ListFileDaily[0]:
            dataMergeDay = pd.read_csv("data_group_daily/" + file, index_col=0)
            ListNetworkID = [group_id["network_id"].loc[group_id["station_id"] == dataMergeDay["station_id"].values[0]].values[0]] * dataMergeDay.shape[0]
            dataMergeDay["network_id"] = ListNetworkID
            countday += 1
            print("done : " + str(countday) + "/" + str(lenday))
            continue
        
        dataRead = pd.read_csv("data_group_daily/" + file, index_col=0)
        ListNetworkID = [group_id["network_id"].loc[group_id["station_id"] == dataRead["station_id"].values[0]].values[0]] * dataRead.shape[0]
        dataRead["network_id"] = ListNetworkID
        dataMergeDay = pd.concat([dataMergeDay, dataRead])
        countday += 1
        print("done : " + str(countday) + "/" + str(lenday))

    dataMergeDay.sort_values("station_id",inplace=True)
    dataMergeDay.index = range(0, dataMergeDay.shape[0])
    dataMergeDay.to_csv("archive/stations_daily_merge.csv")
    #print(dataMergeDay)
    print("done day")

doit = ""
doit = input("do hourly (y/n) :").lower()

if doit == "y":
    print("=== start merging data from hourly ===")
    lenhour = len(ListFileHourly)
    counthour = 0

    for file in ListFileHourly:
        if file == ListFileHourly[0]:
            dataMergeHour = pd.read_csv("hourly_time_conv/" + file, index_col=0)
            counthour += 1
            ListNetworkID = [group_id["network_id"].loc[group_id["station_id"] == dataMergeHour["station_id"].values[0]].values[0]] * dataMergeHour.shape[0]
            dataMergeHour["network_id"] = ListNetworkID
            print("done : " + str(counthour) + "/" + str(lenhour))
            continue
        
        dataRead = pd.read_csv("hourly_time_conv/" + file, index_col=0)
        ListNetworkID = [group_id["network_id"].loc[group_id["station_id"] == dataRead["station_id"].values[0]].values[0]] * dataRead.shape[0]
        dataRead["network_id"] = ListNetworkID
        dataMergeHour = pd.concat([dataMergeHour, dataRead])
        counthour += 1
        print("done : " + str(counthour) + "/" + str(lenhour))

    dataMergeHour.sort_values("station_id",inplace=True)
    dataMergeHour["datetime"] = dataMergeHour.index
    dataMergeHour.index = range(0, dataMergeHour.shape[0])
    cols = dataMergeHour.columns.to_list()
    cols = cols[-1:] + cols[:-1]
    dataMergeHour = dataMergeHour[cols]
    dataMergeHour.to_csv("archive/stations_hourly_merge.csv")
    #print(dataMergeHour)
    print("done hour")