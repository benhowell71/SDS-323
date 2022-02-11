import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
# Q10, a, b, c, d, e, f
df = pd.read_csv('boston.csv')

rows = len(df)
cols = len(df.columns)
########################### A
print("There are " + str(rows) + " rows in the Boston dataset.")
print("There are " + str(cols) + " columns in the Boston dataset.")

sns.pairplot(df[['crim', 'rm', 'age', 'dis', 'tax', 'ptratio']])
plt.show()

########################### B
# we can see that age is very heavily concentrated towards the older end of things, with the 90-100 yr group the most heavily represented
# It's interest to see that the distance from the 5 Boston employment centers decrease with the older the house is
# was also surprised to see that per capita crime rate by town was very low overall, though there are some outliers

########################### C
sns.pairplot(df[['crim', 'zn', 'indus', 'nox', 'rm', 'rad', 'tax', 'ptratio', 'lstat']])
plt.show()

# it was hard to find any variables w/ strong relationships to crime rate, but you can see that's there's a small positive relationship
# between lstat and crim
# can also see that higher nox numbers usually trends towards a higher crim rate

########################### D
df[['crim', 'tax', 'ptratio']].describe()
# some of the census tracts have strangely high crime rates that we saw in the pairplots
# you can see that the maximum crime is 88.98, which is a whopping 14828% higher than the minimum rate of 0.006%
# Crime Rate Boxplot
sns.boxplot(x = df['crim'])
plt.show()

# Tax Rate Boxplot
sns.boxplot(x = df['tax'])
plt.show()

df.sort_values(by = 'tax', ascending = False)
# tax rate has outliers in tax rate at a few specific values, particularly at 711 and 666

# P-T Ratio Boxplot
sns.boxplot(x = df['ptratio'])
plt.show()
# the ptratio makes a lot more sense because there are just a few low ratio tracts, most of them are concentrated around the 18-20 range

########################### E
river_border = df['chas'].sum()
print(str(river_border) + ' census tracts border the river.')

########################### F
median_ratio = df['ptratio'].median()
print("The median ratio of P-T Ratios in the Boston dataset is " + str(median_ratio))