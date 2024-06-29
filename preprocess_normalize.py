import pandas as pd
from sklearn.preprocessing import StandardScaler


# Define the list of files and their labels
files_and_labels = {
    "Bing.csv": {"label": "Bing"},
    "Google.csv": {"label": "Google"},
    "Wikipedia.csv": {"label": "Wikipedia"},
    "Edge.csv": {"label": "Edge"},
    "Chrome.csv": {"label": "Chrome"},
    "Firefox.csv": {"label": "Firefox"},
    "MachineLearning.csv": {"label": "MachineLearning"},
    "DeepLearning.csv": {"label": "DeepLearning"},
    "Python.csv": {"label": "Python"},
    "QuantumComputing.csv": {"label": "QuantumComputing"},
    "Italy.csv": {"label": "Italy"}
}

# Define relevant fields
relevant_fields = ['tcp.stream', 'tcp.len', 'tcp.seq', 'tcp.ack', 'tcp.window_size', 'tcp.analysis.ack_rtt']

# Initialize an empty list to store processed dataframes
processed_dfs = []

for file, meta in files_and_labels.items():
    try:
        # Load the CSV file
        df = pd.read_csv(file)

        # Select relevant fields
        relevant_df = df[relevant_fields]

        # Calculate mean and standard deviation for each tcp.stream
        grouped_df = relevant_df.groupby('tcp.stream').agg(['mean', 'std']).reset_index()

        # Flatten the multi-index columns
        grouped_df.columns = ['_'.join(col).strip('_') for col in grouped_df.columns.values]

        # Add label columns
        grouped_df['label'] = meta['label']

        # Append the processed dataframe to the list
        processed_dfs.append(grouped_df)
    except Exception as e:
        print(f"Error processing file {file}: {e}")

# Combine all processed dataframes into a single dataframe
combined_df = pd.concat(processed_dfs, ignore_index=True)

# Normalize the data
scaler = StandardScaler()
numeric_columns = combined_df.select_dtypes(include=['float64', 'int64']).columns
combined_df[numeric_columns] = scaler.fit_transform(combined_df[numeric_columns])

# Add the class column based on the label
def determine_class(label):
    if label in ["Bing", "Google", "Wikipedia"]:
        return "website"
    elif label in ["Chrome", "Firefox", "Edge"]:
        return "browser"
    elif label in ["Italy", "Python", "MachineLearning", "DeepLearning", "QuantumComputing"]:
        return "query"

combined_df['class'] = combined_df['label'].apply(determine_class)


# Save the combined dataframe to a CSV file
combined_file_path = 'Processed_All_Files_Normalized_With_Class.csv'
combined_df.to_csv(combined_file_path, index=False)

print(f"Processed, normalized, and labeled data saved to {combined_file_path}")
