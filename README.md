# Excel and CSV Data Processor

## Overview

Excel and CSV Data Processor is a standalone application built with Python and Pandas to efficiently process and analyze large datasets from Excel or CSV files. It reads an `.xlsx` or `.csv` file, performs basic data analysis, and saves the processed data and analysis results to new files.

## Features

- Load Excel and CSV files
- Perform basic data analysis including:
  - Descriptive statistics
  - Data summarization
  - Missing values analysis
  - Data distribution (e.g., histograms for numeric data)
  - Correlation analysis
  - Value counts for categorical columns
- Save processed data and analysis results to new files

## Requirements

- Python 3.7+
- pandas
- openpyxl
- pyinstaller

## Installation

To set up the environment, install the necessary packages using the `requirements.txt` file:

```bash
pip install -r requirements.txt

# Usage

Place your Excel or CSV file in the same directory as data_processor.py.
Run the script with the following command:

```bash
python data_processor.py path_to_your_file

To create a standalone executable, use PyInstaller:
bash
Copy code
pyinstaller --onefile data_processor.py
The executable will be located in the dist directory. Run it with:

```
bash ./dist/data_processor path_to_your_file

# Example Usage
To process a file named sample.xlsx or sample.csv, use:

```bash
python data_processor.py sample.xlsx
python data_processor.py sample.csv
