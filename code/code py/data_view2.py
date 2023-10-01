import pandas as pd
import matplotlib.pyplot as plt
import os

"""
ทำกราฟของไฟล์รายชั่วโมง/สถานี แบบคร่าวๆ (จะดูข้อมูลแบบองค์รวม)
"""

fileListDataDay = os.listdir("data_group_hourly/")
list_column = ['PM2.5','PM10','NOx','O3','CO','HR','NO','NO2',\
'TMP','BEN','CH4','CN','CO2','H2S','HCNM','HCT','HRI','IUV','PB','PP',\
'PST','RS','TMPI','UVA','XIL']

All_file = len(fileListDataDay)
done_file = 0

for file in fileListDataDay:
    data = pd.read_csv("data_group_hourly/" + file,index_col=0)

    for col in list_column:
        plot = data[col].plot.hist()
        #plt.show()
        plt.title( col + " from " + file)
        plt.savefig("plot_pic_hour/" + col + "/" + file[:-4] + "_" + col + ".pdf")

    print(file + " is done ploting.")
    done_file += 1
    print("progress : " + str(done_file) + "/" + str(All_file))