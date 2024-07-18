import pandas as pd
import os
from sklearn.preprocessing import StandardScaler

# Define the list of CSV files
csv_files = [
    'Bing.csv', 'Google.csv', 'Wikipedia.csv',
    'Firefox.csv', 'Edge.csv', 'Chrome.csv',
    'Italy.csv', 'QuantumComputing.csv', 'Python.csv',
    'DeepLearning.csv', 'MachineLearning.csv'
]

# Define a function to determine the class based on the label
def determine_class(label):
    if label in ['Bing', 'Google', 'Wikipedia']:
        return 'website'
    elif label in ['Firefox', 'Edge', 'Chrome']:
        return 'browser'
    elif label in ['Italy', 'QuantumComputing', 'Python', 'DeepLearning', 'MachineLearning']:
        return 'query'
    else:
        return 'unknown'

# Initialize an empty DataFrame to store the merged data
merged_df = pd.DataFrame()

# Loop through each file and append its data to the merged DataFrame
for file in csv_files:
    # Check if the file is empty
    if os.path.getsize(file) > 0:
        # Read the CSV file
        df = pd.read_csv(file)
        
        # Extract the label from the file name (without the .csv extension)
        label = os.path.splitext(file)[0]
        
        # Add the label column
        df['label'] = label
        
        # Determine the class and add the class column
        df['class'] = determine_class(label)
        
        # Append the current DataFrame to the merged DataFrame
        merged_df = pd.concat([merged_df, df], ignore_index=True)
    else:
        print(f"Skipping empty file: {file}")

# Reorder the columns to place 'class' first, 'label' second, and 'tcp.stream' third if it exists
if 'tcp.stream' in merged_df.columns:
    columns = ['class', 'label', 'tcp.stream'] + [col for col in merged_df.columns if col not in ['class', 'label', 'tcp.stream']]
else:
    columns = ['class', 'label'] + [col for col in merged_df.columns if col not in ['class', 'label']]
merged_df = merged_df[columns]

# Preserve only the specified columns
columns_to_preserve = ['class', 'label', 'tcp.stream', 'frame.number', 'tcp.len', 'tcp.window_size', 'frame.len', 'ip.len', 'ip.ttl']
filtered_df = merged_df[columns_to_preserve]
# Function to calculate mean and standard deviation for each TCP connection within each label
def calculate_stats(group):
    stats = group.groupby('tcp.stream').agg({
        'frame.number': ['mean', 'std'],
        'tcp.len':['mean', 'std'],
        'tcp.window_size': ['mean', 'std'],
        'frame.len': ['mean', 'std'],
        'ip.len': ['mean', 'std'],
        'ip.ttl':['mean', 'std']
    }).reset_index()
    stats.columns = ['tcp.stream'] + ['_'.join(col).strip() for col in stats.columns[1:]]
    stats['label'] = group['label'].iloc[0]
    stats['class'] = group['class'].iloc[0]
    # Reorder columns to have class, label, tcp.stream in the first three positions
    stats = stats[['class', 'label', 'tcp.stream'] + [col for col in stats.columns if col not in ['class', 'label', 'tcp.stream']]]
    return stats

# Apply the function to each label group
stats_df = filtered_df.groupby('label', group_keys=False).apply(calculate_stats)

# Save the merged DataFrame to a new CSV file
stats_df.to_csv('merged_data.csv', index=False)

# Print the first few rows of the merged DataFrame
print(stats_df.head())

#Normalize data
data = stats_df

# Identify numerical columns except 'tcp.stream'
numerical_columns = [col for col in data.columns if col not in ['tcp.stream', 'class', 'label']]

# Initialize the StandardScaler
scaler = StandardScaler()

# Normalize the numerical columns
data[numerical_columns] = scaler.fit_transform(data[numerical_columns])

# Display the first few rows of the normalized dataframe
print("Normalized Data:")
print(data.head())

# Save the normalized data to a new CSV file
data.to_csv('normalized_merged_data.csv', index=False)