import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.decomposition import PCA

# Path to the raw CSV file
raw_file_path = 'mergedData.csv'
processed_file_path = 'processed_data.csv'

# Step 1: Read the CSV file
data = pd.read_csv(raw_file_path)

# Step 2: Handle missing values
# Drop columns with too many missing values or irrelevant information
data_cleaned = data.dropna(axis=1, how='any')

# Fill remaining missing values with the mean of each column
data_filled = data_cleaned.fillna(data_cleaned.mean())

# Step 3: Extract and encode labels
label_column = 'browser'  # Replace with the actual label column name if different
labels = data_filled[label_column]
features = data_filled.drop(columns=[label_column])

# Encode labels
label_encoder = LabelEncoder()
encoded_labels = label_encoder.fit_transform(labels)

# Step 4: Remove non-numeric columns
numeric_features = features.select_dtypes(include=[float, int])

# Step 5: Normalize numerical features
scaler = StandardScaler()
normalized_features = scaler.fit_transform(numeric_features)

# Step 6: Reduce dimensionality with PCA
pca = PCA(n_components=2)  # Adjust number of components as needed
reduced_features = pca.fit_transform(normalized_features)

# Step 7: Combine reduced features with labels
processed_data = pd.DataFrame(reduced_features, columns=['PC1', 'PC2'])
processed_data['Label'] = encoded_labels

# Step 8: Save the processed data to a new CSV file
processed_data.to_csv(processed_file_path, index=False)

# Step 9: Display the first few rows of the processed data
print(processed_data.head())
