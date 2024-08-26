"""
Title: Final Dataset Generation Script

Description:
This Python script automates the process of merging multiple analyzed TCP stream CSV files into a single comprehensive dataset. 
The script reads a list of CSV files corresponding to various browsing sessions, concatenates them into a single dataframe, 
and saves the resulting merged dataset as a new CSV file. This final dataset integrates the results from all the individual sessions, 
providing a unified structure for further analysis and modeling.

Key Steps:
- Define the components (browser, website, query, repetition ID) that make up the file names.
- Generate a list of CSV file names based on these components.
- Read each CSV file into a pandas dataframe.
- Concatenate all dataframes into a single dataframe.
- Save the merged dataframe to a specified output file.

Author: Shaghayegh Samadzadeh
Date: July 2024

"""


import pandas as pd

def merge_csv_files(file_list, output_file):
    """
    Reads multiple CSV files and merges them into a single CSV file.
    
    Parameters:
    file_list (list of str): List of paths to CSV files to be merged.
    output_file (str): Path to the output CSV file.
    """
    # List to store individual dataframes
    dataframes = []
    
    for file in file_list:
        # Read each CSV file
        df = pd.read_csv(file)
        # Append the dataframe to the list
        dataframes.append(df)
    
    # Concatenate all dataframes
    merged_df = pd.concat(dataframes, ignore_index=True)
    
    # Save the merged dataframe to the specified output file
    merged_df.to_csv(output_file, index=False)
    print(f'Merged data saved to {output_file}')

#--------------------------------------------------------------------------------------

# Define the components for the file names
browsers = ['Chrome', 'Edge', 'Firefox']
websites = ['Wikipedia', 'Google', 'Bing']
queries = ['MachineLearning', 'DeepLearning', 'Python', 'QuantumComputing', 'Italy']
repetition_ids = [100]

# Generate the list of CSV files to process
file_list = []

for browser in browsers:
    for website in websites:
        for query in queries:
            for repetition_id in repetition_ids:
                file_name = f"{browser}_{website}_{query}_{repetition_id}.csv"
                file_list.append(file_name)


final_output_file = f'Merged_TCP_Stream_Analysis_{repetition_id}.csv'
merge_csv_files(file_list, final_output_file)