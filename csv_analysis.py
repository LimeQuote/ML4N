"""
Title: TCP Stream Data Analysis Script

Description:
This Python script processes and analyzes TCP stream data extracted from network traffic captures stored in CSV files.
The script performs the following tasks:
- Reads the dataset from each CSV file.
- Calculates statistical metrics (mean and standard deviation) for various fields grouped by TCP stream.
- Counts the number of packets associated with each TCP stream.
- Determines the mode (most frequent value) for key fields such as source/destination IP addresses and ports.
- Counts the number of unique TCP flags within each stream.
- Merges all calculated metrics into a single dataframe.
- Adds contextual information (browser, website, query, and repetition ID) extracted from the filename.
- Saves the final processed data into a new CSV file.

The script is designed to automate the analysis of multiple CSV files, generating a comprehensive dataset for further analysis.

Author: Shaghayegh Samadzadeh
Date: July 2024

"""

import pandas as pd

def analyze_tcp_stream_data(filename):
   
    # Read the dataset
    data = pd.read_csv(filename)

    # Calculate the mean and standard deviation of numerical columns grouped by 'tcp.stream'
    grouped_data = data.groupby('tcp.stream').agg(
        frame_len_mean=('frame.len', 'mean'),
        frame_len_std=('frame.len', 'std'),
        tcp_len_mean=('tcp.len', 'mean'),
        tcp_len_std=('tcp.len', 'std'),
        tcp_window_size_value_mean=('tcp.window_size_value', 'mean'),
        tcp_window_size_value_std=('tcp.window_size_value', 'std'),
        tcp_seq_mean=('tcp.seq', 'mean'),
        tcp_seq_std=('tcp.seq', 'std'),
        ip_ttl_mean=('ip.ttl', 'mean'),
        ip_ttl_std=('ip.ttl', 'std'),
        tcp_ack_mean=('tcp.ack', 'mean'),
        tcp_ack_std=('tcp.ack', 'std')
    ).reset_index()

    # Add the number of packets for each stream
    packet_counts = data.groupby('tcp.stream').size().reset_index(name='packet_count')

    # Merge the packet count data with the grouped data
    result = pd.merge(grouped_data, packet_counts, on='tcp.stream')

    # Re-calculate the mode for the required columns and the count of unique TCP flags
    mode_data_selected = data.groupby('tcp.stream').agg(
        ip_src_mode=('ip.src', lambda x: x.mode().iloc[0]),
        ip_dst_mode=('ip.dst', lambda x: x.mode().iloc[0]),
        tcp_srcport_mode=('tcp.srcport', lambda x: x.mode().iloc[0]),
        tcp_dstport_mode=('tcp.dstport', lambda x: x.mode().iloc[0]),
        unique_tcp_flags=('tcp.flags', 'nunique')
    ).reset_index()

    # Select and merge the relevant columns
    result_final = result[['tcp.stream', 'frame_len_mean', 'frame_len_std', 'tcp_len_mean', 'tcp_len_std',
                           'tcp_window_size_value_mean', 'tcp_window_size_value_std', 'tcp_seq_mean', 
                           'tcp_seq_std', 'ip_ttl_mean', 'ip_ttl_std', 'tcp_ack_mean', 'tcp_ack_std', 
                           'packet_count']]

    result_final = result_final.merge(mode_data_selected, on='tcp.stream')

    # Split the filename to create new columns
    browser, website, query, repetition_id = filename.replace('.csv', '').split('_')

    # Add these new columns to the dataframe
    result_final['browser'] = browser
    result_final['website'] = website
    result_final['query'] = query
    result_final['repetition_id'] = repetition_id
    
    # Output file name
    output_file_name = f'{filename.replace(".csv", "")}.csv'
    result_final.to_csv(output_file_name, index=False)
    
    return output_file_name

#----------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------



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

# Output the generated list

for filename in file_list:
    output_file = analyze_tcp_stream_data(filename)
    print(output_file)

