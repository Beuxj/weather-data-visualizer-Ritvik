import pandas as pd

df = pd.read_csv("raw_weather.csv")
df.head()
df.info()
df.describe()

print(df.info())
print(df.describe())

df['date'] = pd.to_datetime(df['date'])
df = df.fillna(method="ffill")
df = df[['date','temperature','rainfall','humidity']]
df.head()
print(df.head())

import numpy as np

df['temperature'].mean()
df['temperature'].std()

monthly = df.resample('M', on='date').agg(['mean','min','max','std'])
yearly = df.resample('Y', on='date').agg(['mean','min','max'])
monthly
yearly
print(monthly)
print(yearly)

import matplotlib.pyplot as plt

# Daily temperature
plt.plot(df['date'], df['temperature'])
plt.title("Daily Temperature")
plt.savefig("daily_temp.png")
plt.show()

# Monthly rainfall
monthly_rain = df.resample('M', on='date')['rainfall'].sum()
plt.bar(monthly_rain.index.month, monthly_rain)
plt.title("Monthly Rainfall")
plt.savefig("monthly_rainfall.png")
plt.show()

# Scatter Plot
plt.scatter(df['temperature'], df['humidity'])
plt.title("Humidity vs Temperature")
plt.savefig("humidity_vs_temp.png")
plt.show()

# Combined Figure
plt.figure(figsize=(10,4))
plt.subplot(1,2,1)
plt.plot(df['date'], df['temperature'])
plt.title("Temp Trend")

plt.subplot(1,2,2)
plt.scatter(df['temperature'], df['humidity'])
plt.title("Temp vs Humidity")
plt.savefig("combined.png")
plt.show()


monthly_group = df.groupby(df['date'].dt.month).mean()
season_group = df.groupby(df['date'].dt.quarter).mean()
monthly_group
season_group

print(monthly_group)
print(season_group)

df.to_csv("cleaned_weather.csv", index=False)
