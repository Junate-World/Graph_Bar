import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load your data
file_path = 'Escalation matrix.xlsx'  # Replace with your actual file path
data = pd.read_excel(file_path, header=1)  # Adjust as necessary

# Trim whitespace from column names if necessary
data.columns = data.columns.str.strip()

# Define the IHS Site IDs you want to plot
ihs_site_ids_to_plot = input("Enter the IHS Site IDs to plot, separated by spaces and all uppercase: ").split()

# Filter the DataFrame for the specified IHS Site IDs
filtered_data = data[data['IHS Site ID (updated)'].isin(ihs_site_ids_to_plot)]

# Check if any data was found
if filtered_data.empty:
    print("No data found for the specified IHS Site IDs.")
else:
    # Now plot the filtered data
    plt.figure(figsize=(12, 6))

    plt.bar(filtered_data['IHS Site ID (updated)'], filtered_data['Tower Height'], color='blue')
    plt.title(f'Selected IHS Site IDs and Tower Heights')
    plt.xlabel('IHS Site ID', fontsize=5)
    plt.ylabel('Tower Height', fontsize=10)
    

     # Adjust the y-ticks
    max_height = filtered_data['Tower Height'].max()  # Get the maximum height for scaling
    interval = 2  # Set your desired interval
    y_ticks = np.arange(0, max_height + interval, interval)
    plt.yticks(y_ticks)

    plt.xticks(rotation=45, fontsize=6)
    plt.show()
