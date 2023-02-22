import pandas as pd
import calendar

month_names=[]
for x in range(1,13):
    month_names.append(calendar.month_abbr[x])

month_angles=[]
for x in range(0,12):
    month_angles.append(15+30*x)

data = [21, 23, 32, 31, 29, 20, 19, 18, 15, 17, 21, 16]

df = pd.DataFrame(list(zip(month_names,month_angles,data)),columns = ['month','month_angle','data'])
print(df)