"""NOAA Philippines Precipitation Analysis (2000-2026)

This project analyzes precipitation data from various weather stations 
in the Philippines spanning from 2000 to 2026. The primary goal is to gain 
a deeper understanding of precipitation patterns, variations, and trends 
influenced by geographic region, month, and year.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ============================================================================
# DATA LOADING AND INITIAL EXPLORATION
# ============================================================================

# Load the dataset from a CSV file into a pandas DataFrame
df = pd.read_csv('4353509.csv')

# Display the dimensions of the DataFrame (rows, columns)
print(f"DataFrame Shape: {df.shape}")

# Display the names of all columns in the DataFrame
print(f"DataFrame Columns: {df.columns.tolist()}")

# Display the first few rows of the DataFrame to get a quick overview of the data
print("\nFirst few rows:")
print(df.head())

# Display a concise summary of the DataFrame, including data types and non-null values
print("\nDataFrame Info:")
df.info()

# ============================================================================
# STATION DATA COMPLETENESS ANALYSIS
# ============================================================================

print("\n" + "="*70)
print("STATION DATA COMPLETENESS ANALYSIS")
print("="*70)

# Group by 'NAME' (station name) and count the non-null 'PRCP' entries
print("\nStations with most precipitation records:")
print(df.groupby('NAME')['PRCP'].count().sort_values(ascending=False))

# ============================================================================
# STATIONS WITH HIGHEST AVERAGE PRECIPITATION
# ============================================================================

print("\n" + "="*70)
print("STATIONS WITH HIGHEST AVERAGE PRECIPITATION")
print("="*70)

# Identify the stations with the highest average precipitation
print("\nStations ranked by average precipitation:")
print(df.groupby('NAME')['PRCP'].mean().sort_values(ascending=False))

# ============================================================================
# MONTHLY PRECIPITATION PATTERNS
# ============================================================================

print("\n" + "="*70)
print("MONTHLY PRECIPITATION PATTERNS")
print("="*70)

# Convert the 'DATE' column to datetime objects
df['DATE'] = pd.to_datetime(df['DATE'], format='%Y-%m')

# Extract the month number from the 'DATE' column
df['month_number'] = df['DATE'].dt.month

# Calculate the mean precipitation for each month
mean_prcp = df.groupby('month_number')['PRCP'].mean()

print("\nMean Precipitation per Month:")
print(mean_prcp)

print("\nMonths with Most Rain (sorted by mean precipitation):")
print(mean_prcp.sort_values(ascending=False))

# ============================================================================
# GEOGRAPHICAL PRECIPITATION DIFFERENCES
# ============================================================================

print("\n" + "="*70)
print("GEOGRAPHICAL PRECIPITATION DIFFERENCES")
print("="*70)

# Group by latitude
print("\nMean precipitation by latitude:")
df_region_lat = df.groupby('LATITUDE')['PRCP'].mean()
print(df_region_lat.sort_values(ascending=False).head(10))

# Group by longitude
print("\nMean precipitation by longitude:")
region_long = df.groupby('LONGITUDE')['PRCP'].mean()
print(region_long.sort_values(ascending=False).head(10))

# ============================================================================
# REGIONAL CLASSIFICATION AND ANALYSIS
# ============================================================================

print("\n" + "="*70)
print("REGIONAL CLASSIFICATION AND MEAN PRECIPITATION")
print("="*70)

# Define latitude bins to categorize regions (Mindanao, Visayas, Luzon)
lat_bins = [6, 9, 12, 21]
lat_labels = ["Mindanao", "Visayas", "Luzon"]

# Create a new 'Region' column by categorizing 'LATITUDE'
df["Region"] = pd.cut(df["LATITUDE"], bins=lat_bins, labels=lat_labels)

# Calculate the mean precipitation for each region
regional_PRCP = df.groupby('Region')['PRCP'].mean()
print("\nMean Precipitation by Region (sorted):")
print(regional_PRCP.sort_values(ascending=False))

# ============================================================================
# VISUALIZATION: AVERAGE PRECIPITATION ACROSS REGIONS
# ============================================================================

# Plot a bar graph of mean precipitation by region
plt.figure(figsize=(10, 6))

colors = [(0.6, 0.4, 0.2), (0.1, 0.2, 0.6), (0.1, 0.6, 0.2)]

plt.bar(
    regional_PRCP.index,
    regional_PRCP.values,
    color=colors,
    edgecolor="black",
    width=0.6,
)

plt.title('Average Precipitation Across Philippine Island Regions', 
          fontsize=14, fontweight='bold', pad=15)
plt.xlabel('Geographic Region', fontsize=12, labelpad=10)
plt.ylabel('Precipitation (mm)', fontsize=12, labelpad=10)

plt.grid(axis='y', linestyle='--', alpha=0.5)

# Add text labels on top of each bar
for index, value in enumerate(regional_PRCP.values):
    if not pd.isna(value):
        plt.text(
            index,
            value + 5,
            f"{value:.1f} mm",
            ha="center",
            va="bottom",
            fontsize=10,
            fontweight="bold",
        )

plt.tight_layout()
plt.show()

# ============================================================================
# MISSING DATA ANALYSIS
# ============================================================================

print("\n" + "="*70)
print("MISSING DATA ANALYSIS")
print("="*70)

# Filter rows where PRCP is missing
missing_values = df[df['PRCP'].isna()]

# Group by Region and STATION
station_regions = missing_values.groupby(["Region", "STATION"], observed=True).size()
station_regions_df = station_regions.reset_index(name="Missing Data Count")

print("\nStations with missing data:")
print(station_regions_df)

# Total missing data by region
total_region_counts = station_regions_df.groupby('Region')['Missing Data Count'].sum()
total_region_counts = total_region_counts.reset_index(name="Missing Data Count")

# Get the total number of data points for each region
total_data = df.groupby('Region', observed=True)['PRCP'].size().values

# Calculate percentage of missing data
percentage_missing = (total_region_counts['Missing Data Count'].values / total_data) * 100
regions = total_region_counts["Region"].values

print("\nPercentage of missing data by region:")
for region, percentage in zip(regions, percentage_missing):
    print(f"  {region}: {percentage:.2f}%")

# ============================================================================
# YEARLY AND REGIONAL YEARLY PRECIPITATION TRENDS
# ============================================================================

print("\n" + "="*70)
print("YEARLY AND REGIONAL YEARLY PRECIPITATION TRENDS")
print("="*70)

# Extract the year from the DATE column
df['Year'] = df['DATE'].astype(str).str[:4]

# Calculate yearly means
yearly_means = df.groupby('Year')['PRCP'].mean()
print("\nYearly mean precipitation:")
print(yearly_means)

# Calculate regional yearly means
region_yearly_means = df.groupby(['Region', 'Year'], as_index=False)['PRCP'].mean()

print("\nWettest region-year combinations:")
print(region_yearly_means.sort_values(by='PRCP', ascending=False).head(10))

# ============================================================================
# VISUALIZATION: YEARLY MEAN PRECIPITATION
# ============================================================================

plt.figure(figsize=(12, 8))

colors = [(0.8, 0.4, 0.2)]
plt.bar(
    yearly_means.index,
    yearly_means.values,
    color=colors,
    edgecolor="black",
    width=1,
)

plt.title('Yearly Mean Precipitation', fontsize=14, fontweight='bold', pad=15)
plt.xlabel('Year', fontsize=12, labelpad=8)
plt.ylabel('Precipitation (mm)', fontsize=12, labelpad=10)

plt.grid(axis='y', linestyle='--', alpha=0.5)

for index, value in enumerate(yearly_means.values):
    if not pd.isna(value):
        plt.text(
            index,
            value + 5,
            f"{value:.1f} mm",
            ha="center",
            va="bottom",
            fontsize=9,
            fontweight="bold",
        )

plt.tight_layout()
plt.show()

# ============================================================================
# VISUALIZATION: YEARLY REGIONAL MEAN PRECIPITATION
# ============================================================================

plt.figure(figsize=(12, 8))

for region in ['Luzon', 'Visayas', 'Mindanao']:
    region_data = region_yearly_means[region_yearly_means['Region'] == region]
    plt.plot(region_data['Year'], region_data['PRCP'], marker='o', label=region, linewidth=2)

plt.title('Yearly Regional Mean Precipitation', fontsize=14, fontweight='bold', pad=15)
plt.xlabel('Year', fontsize=12, labelpad=8)
plt.ylabel('Precipitation (mm)', fontsize=12, labelpad=10)
plt.legend(fontsize=11)

plt.grid(axis='y', linestyle='--', alpha=0.5)

plt.tight_layout()
plt.show()

# ============================================================================
# PROJECT CONCLUSION
# ============================================================================

print("\n" + "="*70)
print("PROJECT CONCLUSION")
print("="*70)

print("""
This analysis of NOAA precipitation data across the Philippines (2000-2026) 
revealed the following key insights:

**Key Findings:**
  • Station Reliability: LEGASPI and HINATUAN have the most consistent records
  • Wettest Stations: HINATUAN and BAGUIO show highest average precipitation
  • Monthly Seasonality: August is wettest, April is driest
  • Regional Differences: Mindanao > Luzon > Visayas (by avg precipitation)
  • Missing Data: Significant gaps especially in Luzon (~40%)
  • Yearly Trends: Precipitation fluctuates year to year with identifiable patterns

**Future Work:**
  • Implement missing data imputation techniques
  • Create interactive visualizations (Plotly, Folium)
  • Analyze correlations with other environmental factors
  • Develop precipitation forecasting models
""")
