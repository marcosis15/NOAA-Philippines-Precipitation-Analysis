# NOAA Philippines Precipitation Analysis (2000-2026)

## 📊 Project Overview

This project analyzes precipitation data collected from various weather stations across the Philippines spanning from 2000 to 2026. The analysis uncovers key precipitation patterns, seasonal variations, regional differences, and long-term trends.

## 🎯 Objectives

- Identify which regions receive the most precipitation
- Determine wet and dry seasons in the Philippines
- Analyze which weather stations have the most reliable data
- Understand how precipitation varies by geography and time
- Identify data gaps and missing values

## 📈 Key Findings

- **Consistently Wet Stations**: HINATUAN, RP and BAGUIO, RP recorded the highest average precipitation
- **Clear Wet & Dry Seasons**: August is the wettest month (~800mm), while April is the driest (~200mm)
- **Regional Disparities**: Mindanao receives the highest average precipitation, followed by Luzon, then Visayas
- **Data Limitations**: Significant portions of precipitation data are missing, especially in Luzon (~40% missing)
- **Yearly Trends**: Precipitation fluctuates year to year, with some years showing notably higher rainfall than others

## 🛠️ Technologies Used

- **Python 3**
- **pandas** - Data manipulation and analysis
- **matplotlib** - Data visualization
- **numpy** - Numerical operations

## 📦 Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/marcosis15/NOAA-Philippines-Precipitation-Analysis.git
   cd NOAA-Philippines-Precipitation-Analysis
   ```

2. **Install required packages:**
   ```bash
   pip install -r requirements.txt
   ```

## ▶️ How to Run

1. Make sure you have the dataset file `4353509.csv` in the project directory
2. Run the analysis script:
   ```bash
   python "noaa_data_prcp_2000_2026 (1).py"
   ```
3. The script will generate visualizations and print analysis results to the console

## 📊 Analysis Sections

The analysis includes:
- **Data Overview**: Understanding the structure and completeness of the dataset
- **Station Analysis**: Identifying which stations have the most data and highest precipitation
- **Monthly Patterns**: Determining wet and dry seasons
- **Regional Comparison**: Comparing precipitation across Mindanao, Visayas, and Luzon
- **Missing Data Analysis**: Quantifying data gaps by region
- **Yearly Trends**: Visualizing precipitation changes over time

## 📝 Dataset Source

Data is sourced from NOAA (National Oceanic and Atmospheric Administration) weather stations across the Philippines.

## 🔮 Future Improvements

- Handle missing data through imputation techniques
- Create interactive visualizations using Plotly or Folium
- Analyze correlation with other environmental factors
- Add predictive modeling for precipitation forecasting
- Improve visualization styling and add more detailed charts

## 📧 Author

marcosis15
