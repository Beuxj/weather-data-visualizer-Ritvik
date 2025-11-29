# Weather Data Analysis Project

## 📌 Overview
This project analyzes a real-like weather dataset using Python, Pandas, NumPy, and Matplotlib.  
The analysis includes data loading, cleaning, processing, statistical calculations, visualizations, and seasonal/monthly grouping.

The goal is to understand temperature trends, rainfall patterns, humidity relationships, and overall climate behavior.

---

## 📂 Dataset Description
File: **raw_weather.csv**

Columns:
- `date` – Daily timestamp  
- `temperature` – Daily temperature (°C)  
- `rainfall` – Daily rainfall (mm)  
- `humidity` – Daily humidity (%)  

A cleaned version of the dataset is provided: **cleaned_weather.csv**  
Missing values were handled using forward-fill.

---

## 🛠️ Tools & Technologies
- **Python 3.9+**
- **Pandas** – Data cleaning and processing  
- **NumPy** – Statistical calculations  
- **Matplotlib** – Data visualization  
- **Jupyter Notebook / VS Code**

---

## 📊 Visualizations Included
The following charts are included as PNG files:

1. `daily_temp.png` – Daily temperature trend  
2. `monthly_rainfall.png` – Monthly rainfall totals  
3. `humidity_vs_temp.png` – Humidity vs. temperature scatter plot  
4. `combined.png` – Combined subplot figure  

---

## 📈 Results Summary
- Temperature fluctuates gradually throughout the year with seasonal effects.  
- Rainfall shows high month-to-month variation with clear peaks.  
- Humidity has a loose correlation with temperature.  
- Aggregation by month and season shows clear climate patterns.

---

## 📁 Repository Contents
📦 Weather-Analysis
┣ 📜 README.md
┣ 📜 weather_analysis.ipynb / weather.py
┣ 📂 data
│ ┣ raw_weather.csv
│ ┗ cleaned_weather.csv
┣ 📂 plots
│ ┣ daily_temp.png
│ ┣ monthly_rainfall.png
│ ┣ humidity_vs_temp.png
│ ┗ combined.png
┗ 📜 summary_report.md
