# Data_Cleaning
This repository features a Python function, `data_cleaning_master`, for cleaning CSV and Excel datasets using Pandas. It removes duplicates, fills missing values, and outputs the cleaned data to a new file. This tool simplifies data preparation for analysts, making it easier to ensure data integrity and readiness for analysis.


**Data Cleaning Function in Python**
This repository contains a Python function for cleaning datasets in CSV and Excel formats using Pandas. The data_cleaning_master function performs the following tasks:

Loads datasets from specified file paths.
Identifies and reports duplicate records, saving them to a separate Excel file if found.
Detects and handles missing values by filling numerical columns with the mean and dropping rows in categorical columns.
Outputs the cleaned dataset to a new Excel file.
Features
Supports both CSV and Excel file formats.
Outputs summary statistics for duplicates and missing values.
Saves cleaned data to a new file for easy access.
Usage
Simply call the data_cleaning_master function with the appropriate dataset path and name.
