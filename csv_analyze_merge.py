import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


#Read the meta data file <website_behavior.csv> to identify the pcap_to_csv file name for each individual search
metadata_file_path = 'websites_behaviors.csv'
data = pd.read_csv(metadata_file_path)

# Extract relevant columns and generate the file list
file_list = []

for index, row in data.iterrows():
    browser = row['browser']
    website = row['website']
    query = row['query'].replace(' ', '')
    filename = f'{browser}_{website}_{query}.csv'
    file_list.append(filename)

# Display the list
print(file_list)



#Use this function to see the stats of each csv file in file list:
def read_csv_and_present_features(file_path):
    """
    Reads a CSV file and presents its features along with basic statistics.
    
    Parameters:
    file_path (str): The path to the CSV file.
    
    Returns:
    DataFrame: A pandas DataFrame with basic statistics for each feature.
    """
    # Read the CSV file
    df = pd.read_csv(file_path)
    
    # Get basic statistics for each feature
    feature_stats = df.describe(include='all').transpose()

    # Add data types to the feature statistics
    feature_stats['dtype'] = df.dtypes  

    return feature_stats




#Use this function to analyze each file in file_list
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
    browser, website, query = filename.replace('.csv', '').split('_')

    # Add these new columns to the dataframe
    result_final['browser'] = browser
    result_final['website'] = website
    result_final['query'] = query

    # Output file name
    output_file_name = f'{filename.replace(".csv", "")}_analyzed.csv'
    result_final.to_csv(output_file_name, index=False)
    
    return output_file_name


#Use this function to merge all the analyzed files
def merge_csv_files(filenames, output_file):
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


    #-----------------------------------------------------------------------

for filename in file_list:
    output_file = analyze_tcp_stream_data(filename)
    print(output_file)

# Generate the list of analyzed filenames
analyzed_file_list = [f'{filename.replace(".csv", "")}_analyzed.csv' for filename in file_list]

output_file = 'Merged_TCP_Stream_Analysis.csv'
merge_csv_files(analyzed_file_list, output_file)
