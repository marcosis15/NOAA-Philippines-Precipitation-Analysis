"""NOAA Data PRCP 2000-2026

Original file is located at
    https://colab.research.google.com/drive/1NOPrtv_wpoBLmNkN2SeaJ5AOS8W_-b7T
"""

# Project Overview

# This project analyzes precipitation data from various weather stations in the Philippines spanning from 2000 to 2026. The primary goal is to gain a deeper understanding of precipitation patterns across the Philippines, specifically examining variations based on geographic region, month, year, and elevation.

import pandas as pd # Import the pandas library for data manipulation

# Load the dataset from a CSV file into a pandas DataFrame
df = pd.read_csv('4353509.csv')

# Mount Google Drive to access files, if necessary (though the CSV is in the local environment)
from google.colab import drive
drive.mount('/content/drive')

# Display the dimensions of the DataFrame (rows, columns)
print(df.shape)

# Display the names of all columns in the DataFrame
print(df.columns)

# Display the first few rows of the DataFrame to get a quick overview of the data
df.head()

# Display a concise summary of the DataFrame, including data types and non-null values
df.info()

import pandas as pd # Import the pandas library for data manipulation

# Load the dataset from a CSV file into a pandas DataFrame
df = pd.read_csv('4353509.csv')

# Mount Google Drive to access files, if necessary (though the CSV is in the local environment)
from google.colab import drive
drive.mount('/content/drive')

# Display the dimensions of the DataFrame (rows, columns)
print(f"DataFrame Shape: {df.shape}")

# Display the names of all columns in the DataFrame
print(f"DataFrame Columns: {df.columns.tolist()}")

# Display the first few rows of the DataFrame to get a quick overview of the data
display(df.head())

# Display a concise summary of the DataFrame, including data types and non-null values
df.info()

"""### Data Overview and Initial Exploration

This section loads the precipitation data and provides an initial glance at its structure, dimensions, and data types, which is crucial for understanding the dataset before proceeding with any analysis.
"""

# This section helps understand which weather stations have the most precipitation (PRCP) data recorded.
# Group by 'NAME' (station name) and count the non-null 'PRCP' entries, then sort in descending order.
print(df.groupby('NAME')['PRCP'].count().sort_values(ascending=False))

"""### Station Data Completeness Analysis

This analysis helps to understand which weather stations have the most recorded precipitation data (`PRCP`). A higher count indicates more reliable data for that specific station.
"""

# This section identifies the stations with the highest average precipitation.
# Group by 'NAME' (station name) and calculate the mean 'PRCP', then sort in descending order.
print(df.groupby('NAME')['PRCP'].mean().sort_values(ascending=False))

"""### Stations with Highest Average Precipitation

This section identifies the weather stations that, on average, receive the most precipitation. This insight can highlight regions that are historically wetter.
"""

# Determination of months with most rain (Wet Season Determination)

# Convert the 'DATE' column to datetime objects for easier time-based operations.
# The format is specified as 'YYYY-MM'.
df['DATE'] = pd.to_datetime(df['DATE'], format='%Y-%m')

# Extract the month number from the 'DATE' column and store it in a new 'month_number' column.
df['month_number'] = df['DATE'].dt.month

# Calculate the mean precipitation (PRCP) for each month.
# This aggregates the data to find the average rainfall for each month across all years and stations.
mean_prcp = df.groupby('month_number')['PRCP'].mean()

# Print the mean precipitation per month.
print("Mean Precipitation per Month:")
print(mean_prcp)

# Print the months sorted by their mean precipitation in descending order to identify the wettest months.
print("\nMonths with Most Rain (sorted by mean precipitation):")
print(mean_prcp.sort_values(ascending=False))

"""### Monthly Precipitation Patterns

Here, we determine which months typically experience the highest levels of precipitation, helping to identify wet and dry seasons across the dataset.
"""

# Determine differences in mean precipitation (PRCP) across different geographical regions by latitude and longitude.

# Group the DataFrame by 'LATITUDE' and calculate the mean 'PRCP' for each latitude.
df_region_lat = df.groupby('LATITUDE')['PRCP'].mean()
print(df_region_lat.sort_values(ascending=False))

# Group the DataFrame by 'LONGITUDE' and calculate the mean 'PRCP' for each longitude.
region_long = df.groupby('LONGITUDE')['PRCP'].mean()
print(region_long.sort_values(ascending=False))

# Group the DataFrame by both 'LATITUDE' and 'LONGITUDE' to get mean 'PRCP' for specific locations.
df_region_lat_long = df.groupby(['LATITUDE', 'LONGITUDE'])['PRCP'].mean()
print(df_region_lat_long.sort_values(ascending=False))

"""### Geographical Precipitation Differences

This part of the analysis explores how precipitation levels vary based on the geographical coordinates (latitude and longitude) of the weather stations, and then groups stations into broader regions (Mindanao, Visayas, Luzon) to understand regional precipitation averages.
"""

# Make a matrix of different regions with Mean PRCP
import numpy as np # Import numpy for numerical operations

# Define latitude bins to categorize regions (Mindanao, Visayas, Luzon)
lat_bins = [6,9,12,21]
# Define labels corresponding to the latitude bins
lat_labels = ["Mindanao","Visayas","Luzon"]

# Create a new 'Region' column by categorizing 'LATITUDE' into the defined bins.
df["Region"] = pd.cut(df["LATITUDE"], bins=lat_bins, labels=lat_labels)

# Calculate the mean precipitation for each defined 'Region'.
regional_PRCP = df.groupby('Region')['PRCP'].mean()
# Print the regional mean precipitation, sorted in descending order.
print(regional_PRCP.sort_values(ascending=False))

"""#### Regional Classification and Mean Precipitation

To better understand regional differences, stations are grouped into Mindanao, Visayas, and Luzon based on their latitude. The mean precipitation for each of these major island groups is then calculated, revealing which regions are, on average, the wettest.
"""

# Plot a bar graph of mean precipitation (PRCP) by region
import matplotlib.pyplot as plt # Import matplotlib for plotting
import pandas as pd # Import pandas (already imported, but good practice for standalone cells)

# Set x and y axis labels from the regional_PRCP Series index and name
x_axis_label = regional_PRCP.index.name
y_axis_label = regional_PRCP.name

# Create a figure with a specified size for the plot
plt.figure(figsize=(10,6))

# Define custom colors for the bars in the bar chart
colors =[(0.6,0.4,0.2),(0.1,0.2,0.6),(0.1,0.6,0.2)]

# Create the bar chart
plt.bar(
    regional_PRCP.index, # x-axis: Region names
    regional_PRCP.values, # y-axis: Mean precipitation values
    color=colors, # Apply custom colors
    edgecolor="black", # Add black borders to bars
    width=0.6, # Set the width of the bars
)

# Set the title of the plot with custom font size and weight
plt.title('Average Precipitation Across Philippine Island Regions', fontsize=14, fontweight='bold', pad=15)
# Set the x-axis label with custom font size and padding
plt.xlabel('Geographic Region', fontsize=12, labelpad=10)
# Set the y-axis label with custom font size and padding
plt.ylabel('Precipitation (mm)', fontsize=12, labelpad=10)

# Add a horizontal grid for better readability
plt.grid(axis='y', linestyle='--', alpha=0.5)

# Add text labels on top of each bar showing the exact precipitation value
for index, value in enumerate(regional_PRCP.values):
    if not pd.isna(value): # Only add label if the value is not NaN
        plt.text(
            index, # x-coordinate for the text
            value + 5, # y-coordinate for the text (slightly above the bar)
            f"{value:.1f} mm", # Formatted text (e.g., "XXX.X mm")
            ha="center", # Horizontal alignment to center the text above the bar
            va="bottom", # Vertical alignment to place text at the bottom of its bounding box
            fontsize=10,
            fontweight="bold",
        )

# Adjust layout to prevent labels and title from overlapping
plt.tight_layout()
# Display the plot
plt.show()

"""#### Visualization of Average Precipitation Across Regions

The bar chart above visually represents the average precipitation across the three main Philippine island regions: Mindanao, Visayas, and Luzon. This visualization clearly shows the comparative rainfall experienced in each area.
"""

# Find stations with the most missing data, regions with missing data, and regions with the highest percentage of missing data.

# Filter the DataFrame to include only rows where 'PRCP' (precipitation) is missing (NaN).
missing_values=df[df['PRCP'].isna()]

# Group the missing values by 'Region' and 'STATION' and count the number of missing entries for each station within each region.
station_regions= missing_values.groupby(["Region","STATION"], observed=True).size()

# Convert the grouped Series into a DataFrame with a column named "Missing Data Count".
station_regions_df= station_regions.reset_index(name="Missing Data Count")
print(station_regions_df)

# Print the total number of missing data points across all stations and regions.
print(station_regions_df['Missing Data Count'].sum())

# Calculate and print the total missing data count per region.
for region in station_regions_df['Region'].unique():
  region_count=station_regions_df['Missing Data Count'][station_regions_df['Region']==region].sum()
  print("Total Missing Count per region: " + str(region_count))

# Group the 'station_regions_df' by 'Region' to get the total missing data count for each region.
total_region_counts=station_regions_df.groupby('Region')['Missing Data Count'].sum()
# Convert the result to a DataFrame.
total_region_counts=total_region_counts.reset_index(name="Missing Data Count")
print(total_region_counts)

# Get the total number of data points (non-missing 'PRCP' values) for each region.
total_data= df.groupby('Region', observed=True)['PRCP'].size().values
print(total_data)

# Calculate the percentage of missing data for each region.
percentage_missing= (total_region_counts['Missing Data Count'].values/total_data)*100

# Get the list of unique regions.
regions = total_region_counts["Region"].values

# Print the percentage of missing data for each region.
for region, percentage in zip(regions, percentage_missing):
  print(f"Percentage of missing data in {region}: {percentage:.2f}%")

"""### Missing Data Analysis

Understanding the extent and distribution of missing data is critical. This section identifies which stations and regions have significant amounts of missing precipitation records and calculates the percentage of missing data per region, which can impact the reliability of regional analyses.
"""

# Analyze yearly precipitation totals per region.

# Extract the year from the 'DATE' column (which is already datetime) and store it as a string in a new 'Year' column.
df['Year'] = df['DATE'].astype(str).str[:4]

# Calculate the mean precipitation for each year across all regions and stations.
yearly_means=df.groupby('Year')['PRCP'].mean()
print(yearly_means)

# Calculate the mean precipitation for each 'Region' and 'Year' combination.
region_yearly_means=df.groupby(['Region','Year'], as_index=False)['PRCP'].mean()
print(region_yearly_means)

# Sort the regional yearly means by 'PRCP' in descending order to see the wettest region-year combinations.
print(region_yearly_means.sort_values(by='PRCP', ascending=False))

# Identify which regions per year have missing precipitation data.
# This is done by filtering the 'region_yearly_means' DataFrame for rows where 'PRCP' is NaN,
# which indicates that there was no valid precipitation data for that specific region and year combination.
missing_yearly_prcp = region_yearly_means[region_yearly_means['PRCP'].isna()]
print("\nRegion-Year combinations with missing Mean PRCP:")
print(missing_yearly_prcp)

"""### Yearly and Regional Yearly Precipitation Trends

This analysis delves into how precipitation levels change over the years, both at a national level and broken down by region. It helps to identify long-term trends, anomalies, or specific years with unusually high or low rainfall.
"""

x_axis_label = 'Year'
y_axis_label = 'Precipitation (mm)'

plt.figure(figsize=(12,8))

colors =[(0.8,0.4,0.2)]
plt.bar(
    yearly_means.index, # x-axis: Region names
    yearly_means.values, # y-axis: Mean precipitation values
    color=colors, # Apply custom colors
    edgecolor="black", # Add black borders to bars
    width=1, # Set the width of the bars
)

plt.title('Yearly Mean Precipitation', fontsize=14, fontweight='bold', pad=15)

plt.xlabel('Time (Yr)', fontsize=12, labelpad=8)

plt.ylabel('Precipitation (mm)', fontsize=12, labelpad=10)


plt.grid(axis='y', linestyle='--', alpha=0.5)

for index, value in enumerate(yearly_means.values):
    if not pd.isna(value): # Only add label if the value is not NaN
        plt.text(
            index, # x-coordinate for the text
            value + 5, # y-coordinate for the text (slightly above the bar)
            f"{value:.1f} mm", # Formatted text (e.g., "XXX.X mm")
            ha="center", # Horizontal alignment to center the text above the bar
            va="bottom", # Vertical alignment to place text at the bottom of its bounding box
            fontsize=10,
            fontweight="bold",
        )
plt.tight_layout()
plt.show()

"""#### Visualization of Yearly Mean Precipitation

This bar chart illustrates the overall average precipitation recorded each year across all stations. It provides a quick visual summary of yearly rainfall variations throughout the dataset's period.
"""

x_axis_label = 'Year'
y_axis_label = 'Regional Precipitation (mm)'

plt.figure(figsize=(12,8))

colors =[(0.8,0.4,0.2)]
for region in ['Luzon', 'Visayas','Mindanao']:
  region_data = region_yearly_means[region_yearly_means['Region'] == region]
  plt.plot(region_data['Year'], region_data['PRCP'], marker='o', label=region, linewidth=2)
plt.title('Yearly Regional Mean Precipitation', fontsize=14, fontweight='bold', pad=15)

plt.xlabel('Time (Yr)', fontsize=12, labelpad=8)

plt.ylabel('Precipitation (mm)', fontsize=12, labelpad=10)


plt.grid(axis='y', linestyle='--', alpha=0.5)

plt.tight_layout()
plt.show()

"""#### Visualization of Yearly Regional Mean Precipitation

This line plot showcases the annual precipitation trends for each of the three main Philippine regions (Luzon, Visayas, Mindanao). It allows for a comparative view of how rainfall patterns have evolved over time in different parts of the country.

## Project Conclusion

This project provided a comprehensive analysis of precipitation data across the Philippines from 2000 to 2026, focusing on identifying patterns based on stations, months, regions, and years.

Key findings include:

*   **Station Reliability:** Certain stations like 'LEGASPI, RP' and 'HINATUAN, RP' have a higher number of precipitation records, indicating more consistent data collection.
*   **Wettest Stations:** 'HINATUAN, RP' and 'BAGUIO, RP' consistently showed the highest average precipitation, suggesting these locations are prone to heavy rainfall.
*   **Monthly Seasonality:** August emerged as the wettest month, followed by July and December, indicating distinct wet seasons. April, conversely, was the driest month.
*   **Regional Differences:** Mindanao generally experiences the highest average precipitation, followed by Luzon and then Visayas. This regional disparity highlights the influence of geographical factors on rainfall distribution.
*   **Missing Data:** A significant portion of precipitation data is missing across all regions, with Luzon having the highest percentage of missing records. This underscores a potential limitation in the dataset and the need for careful interpretation, especially for specific region-year combinations where data is entirely absent.
*   **Yearly Trends:** While overall yearly mean precipitation fluctuates, the regional yearly plots provided a more granular view, showing varying trends across Luzon, Visayas, and Mindanao over the years.

Overall, the analysis successfully identified significant precipitation patterns and variations. For future work, addressing the missing data through imputation techniques or exploring other data sources could enhance the robustness of the findings. Further visualization, perhaps using interactive maps, could also provide a more intuitive understanding of the spatial distribution of rainfall.
"""
