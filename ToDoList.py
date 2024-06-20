import pandas as pd

# Creating the to-do list as a dictionary
todo_list = {
    "Step": [
        "1.1 Simulation of Browsing Sessions with Selenium",
        "1.1 Simulation of Browsing Sessions with Selenium",
        "1.1 Simulation of Browsing Sessions with Selenium",
        "1.1 Simulation of Browsing Sessions with Selenium",
        "1.1 Simulation of Browsing Sessions with Selenium",
        "1.1 Simulation of Browsing Sessions with Selenium",
        "1.2 Data Recording with Tshark",
        "1.2 Data Recording with Tshark",
        "1.2 Data Recording with Tshark",
        "1.3 Extracting TCP Statistics",
        "1.3 Extracting TCP Statistics",
        "1.3 Extracting TCP Statistics",
        "1.4 Data Preprocessing",
        "1.4 Data Preprocessing",
        "2.1 Dimensionality Reduction",
        "2.1 Dimensionality Reduction",
        "2.2 Clustering Algorithms",
        "2.2 Clustering Algorithms",
        "2.2 Clustering Algorithms",
        "2.3 Anomaly Detection",
        "2.3 Anomaly Detection",
        "3.1 Cross-Validation Setup",
        "3.1 Cross-Validation Setup",
        "3.2 Classification",
        "3.2 Classification",
        "3.2 Classification",
        "3.2 Classification",
        "3.3 Interpretation of Results",
        "3.3 Interpretation of Results"
    ],
    "Task": [
        "Install Selenium Library",
        "Setup Web Browsers",
        "Write Scripts for Simulation",
        "Automate Repetition",
        "Log Metadata",
        "Create CSV file to log metadata",
        "Install Tshark",
        "Capture Traffic Data",
        "Ensure Clean Data",
        "Install Tstat",
        "Extract TCP Statistics",
        "Select Relevant Data",
        "Normalize Data",
        "Label Dataset",
        "Principal Component Analysis (PCA)",
        "Visualization",
        "Apply Clustering - K-Means",
        "Apply Clustering - Hierarchical",
        "Evaluate Clusters",
        "Isolation Forest for Anomaly Detection",
        "Re-evaluate Clusters",
        "Split Dataset",
        "Divide data into training and validation sets",
        "Train Classifiers - Random Forest",
        "Train Classifiers - SVM",
        "Evaluate Performance",
        "Report performance metrics",
        "Feature Importance Analysis",
        "Discuss classifier effectiveness"
    ]
}

# Converting to DataFrame
todo_df = pd.DataFrame(todo_list)

# Saving to CSV
file_path = 'todo_list_project_steps.csv'
todo_df.to_csv(file_path, index=False)

print(f"To-Do List has been saved to {file_path}")
