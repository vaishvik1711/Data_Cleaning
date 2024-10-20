##Python Function to clean the data
##import
import pandas as pd
import os
##Global Variables
data_path = ''
data_name = ''

##Defning the function
def data_cleaning_master(data_path , data_name):
    if not os.path.exists(data_path):
        print("Please enter correct file")
    ## Print the file format
    else:
        if data_path.endswith('.csv'):
                print('Dataset is CSV File')
                print('\n')
                data = pd.read_csv(data_path, encoding_errors = 'ignore')
                
        elif data_path.endswith('.xlsx'):
                print('Dataset is excel File')
                print('\n')
                data = pd.read_excel(data_path)
        else:
            print("Unknown File Format")
    ## Print shape of the file
    print(f'Dataset contain {data.shape[0]} rows and {data.shape[1]} columns')
    print('\n')
    ## Find duplicates
    total_duplicates = data.duplicated().sum()
    
    if total_duplicates > 0:
        print(f'Total Duplicate values are {total_duplicates}')
        print('\n')
        data_duplicates = data[data.duplicated()]
        data_duplicates.to_excel(f'{data_name}_Duplicates.xlsx', index = None)
        data.drop_duplicates(inplace = True)
    else: 
        print('No Duplicates found')
        print('\n')
        
    total_duplicates = data.duplicated().sum()
    print(f'Now duplicate values are {total_duplicates}')
    print('\n')
   
    #########   find missing values     #########
    
    total_na_values = data.isnull().sum().sum()
    na_columns = data.isnull().sum()
    
    print(f'Data has total {total_na_values} NA Values')
    print('\n')
    columns = data.columns
    ## Remove NA Values and Alter int and float columns
    for col in columns:
        if data[col].dtype in (int, float):
            data[col].fillna(data[col].mean(), inplace = True)
        else:
            data.dropna(subset=col, inplace = True)
    ## save the file in excel
    print(f'Data is cleaned. Number of rows is {data.shape[0]} and columns are {data.shape[1]}')
    data.to_excel(f'cleaned_{data_name}.xlsx', index = None)
    print('\n')
    print('Data is saved')
## call the function
if __name__ == "__Clean_data_function__":
    data_path = input("Please enter Dataset Path:")
    data_name = input("Please enter Dataset Name:")
    
    data_cleaning_master(data_path, data_name)




