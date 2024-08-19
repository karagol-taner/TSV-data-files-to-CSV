import pandas as pd
import glob
import os

def process_file(file_path):
    try:
        df = pd.read_csv(file_path, sep='\t', quoting=3, on_bad_lines='warn')
        
        # Check if the dataframe has 11 columns 
        if len(df.columns) != 11:
            print(f"Warning: {file_path} has {len(df.columns)} columns instead of 11")
        
        return df
    except Exception as e:
        print(f"Error processing {file_path}: {str(e)}")
        return None

# Set the path to the folder containing your TSV files
path = r"/path/to/file"

all_files = glob.glob(os.path.join(path, "*.tsv"))

df_list = []
for file in all_files:
    df = process_file(file)
    if df is not None:
        df_list.append(df)

# Combine all dataframes
if df_list:
    combined_df = pd.concat(df_list, ignore_index=True)
    
    # Write to Excel
    combined_df.to_csv('combined_data.csv', index=False)
    print("Data written to combined_data.csv")
else:
    print("No data could be processed successfully.")
