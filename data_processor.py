import pandas as pd
import sys
import os

def process_data(file_path):
    # Determine file type and read the file
    file_ext = os.path.splitext(file_path)[1].lower()
    
    if file_ext == '.csv':
        read_func = pd.read_csv
        output_file = "processed_data.csv"
    elif file_ext in ['.xls', '.xlsx']:
        read_func = pd.read_excel
        output_file = "processed_data.xlsx"
    else:
        print(f"Unsupported file type: {file_ext}")
        sys.exit(1)
    
    try:
        df = read_func(file_path)
        print(f"File '{file_path}' loaded successfully.")
    except Exception as e:
        print(f"Error loading file: {e}")
        sys.exit(1)

    try:
        # Descriptive Statistics
        print("\nDescriptive Statistics:")
        print(df.describe())

        # Data Summarization
        print("\nData Summarization:")
        print(f"Total number of rows: {df.shape[0]}")
        print(f"Total number of columns: {df.shape[1]}")
        print("\nPreview of the first 5 rows:")
        print(df.head())

        # Missing Values Analysis
        print("\nMissing Values Analysis:")
        missing_values = df.isnull().sum()
        print(missing_values[missing_values > 0])

        # Data Distribution (e.g., Histogram for numeric columns)
        print("\nData Distribution:")
        for column in df.select_dtypes(include=['float64', 'int64']).columns:
            print(f"Distribution for {column}:")
            print(df[column].value_counts(bins=10))

        # Correlation Analysis
        print("\nCorrelation Analysis:")
        print(df.corr())

        # Value Counts for Categorical Columns
        print("\nValue Counts for Categorical Columns:")
        for column in df.select_dtypes(include=['object']).columns:
            print(f"Value counts for {column}:")
            print(df[column].value_counts())

        # Save the processed data to a new file
        if file_ext == '.csv':
            df.to_csv(output_file, index=False)
        else:
            df.to_excel(output_file, index=False)

        print(f"\nProcessed data saved to '{output_file}'.")

    except Exception as e:
        print(f"Error processing data: {e}")
        sys.exit(1)

def main():
    if len(sys.argv) != 2:
        print("Usage: data_processor <path_to_file>")
        sys.exit(1)

    file_path = sys.argv[1]
    
    if not os.path.isfile(file_path):
        print(f"File '{file_path}' does not exist.")
        sys.exit(1)

    process_data(file_path)

if __name__ == "__main__":
    main()
