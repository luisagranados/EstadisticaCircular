import pandas as pd
import calendar
import numpy as np
import matplotlib.pyplot as plt

month_names=[]
for x in range(1,13):
    month_names.append(calendar.month_abbr[x])

month_angles=[]
for x in range(0,12):
    month_angles.append(15+30*x)

data = [21, 23, 32, 31, 29, 20, 19, 18, 15, 17, 21, 16]

# df = pd.DataFrame(list(zip(month_names,month_angles,data)),columns = ['month','month_angle','data'])
# print(df)

width = np.pi / 4 * .5

ax = plt.subplot(projection='polar')
ax.bar(month_angles, data, width=width, bottom=0.0, alpha=0.5)

plt.savefig('test.png')