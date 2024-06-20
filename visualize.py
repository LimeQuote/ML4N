import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Function to visualize the processed data
def visualize_processed_data(file_path):
    # Step 1: Read the processed CSV file
    data = pd.read_csv(file_path)

    # Step 2: Create a scatter plot for the first two principal components
    plt.figure(figsize=(10, 6))
    sns.scatterplot(
        x='PC1', y='PC2',
        hue='Label',
        palette=sns.color_palette("hsv", len(data['Label'].unique())),
        data=data,
        legend="full",
        alpha=0.6
    )

    # Step 3: Customize the plot
    plt.title('PCA of Processed Data')
    plt.xlabel('Principal Component 1')
    plt.ylabel('Principal Component 2')
    plt.legend(title='Browser Labels')
    plt.show()

# Example usage
processed_file_path = 'processed_data.csv'
visualize_processed_data(processed_file_path)
