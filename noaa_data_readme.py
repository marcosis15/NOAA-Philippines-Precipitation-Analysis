# NOAA-Philippines-Precipitation-Analysis
This project provides a comprehensive data analysis of precipitation data collected from various weather stations across the Philippines, spanning from the year 2000 to 2026. The primary objective is to uncover and understand key precipitation patterns, variations, and trends influenced by geographic region, month, and year.

# Precipitation Pattern Analysis in the Philippines (2000-2026)

This project conducts an exploratory data analysis (EDA) of precipitation data across the Philippines from 2000 to 2026, aiming to uncover key patterns, variations, and trends influenced by geographic region, month, and year.

### Project Goal

To gain a deeper understanding of historical and recent rainfall distributions, identify areas prone to high/low precipitation, seasonal variations, and long-term changes.

### Methodology

The analysis involves data loading, assessing station data completeness, identifying wettest stations, analyzing monthly seasonality, geographical regional analysis, and assessing missing data. Visualization is performed using `matplotlib`.

### Key Findings

*   **Consistently Wet Stations**: 'HINATUAN, RP' and 'BAGUIO, RP' recorded the highest average precipitation.
*   **Clear Wet and Dry Seasons**: August is the wettest month, while April is the driest.
*   **Regional Disparities**: Mindanao generally receives the highest average precipitation, followed by Luzon and Visayas.
*   **Data Gaps**: A significant challenge is the high percentage of missing precipitation data across all regions, particularly in Luzon.

### Tools & Libraries Used

*   **Python** with **pandas** for data manipulation and **matplotlib** for visualization.

### Future Work

Future work includes missing data imputation, interactive visualizations (e.g., with `folium` or `plotly`), and correlation analysis with other environmental factors.
