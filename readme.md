# Jeweler Directory Extraction

A Python crawler that extracts jeweler directory information from the National Association of Jewellers (NAJ) website and saves it in both CSV and JSON formats.

## Description

This tool searches for jewelers within a specified radius of Birmingham, UK (by default), focusing on "Designer craftsperson" jewelers that target consumers. The crawler all the results and saves them to timestamped files in a `data` directory.

## Installation

1. Clone this repository to your local machine:
   ```
   git clone https://github.com/yourusername/jeweler-directory-extraction.git
   cd jeweler-directory-extraction
   ```

2. Create a virtual environment (optional but recommended):
   ```
   # On Windows
   python -m venv venv
   venv\Scripts\activate

   # On macOS/Linux
   python -m venv venv
   source venv/bin/activate
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

To run the crawler, simply execute the main script:

```
python src\jeweler_crawler.py
```

The crawler will:
1. Connect to the NAJ website API
2. Fetch jeweler data based on the predefined search criteria
3. Process the data
4. Save the results in both CSV and JSON formats in the `data` directory

## Output

The crawler generates two output files with timestamps in the filename:
- `data\jeweler_data_YYYYMMDD_HHMMSS.csv` - CSV format
- `data\jeweler_data_YYYYMMDD_HHMMSS.json` - JSON format

The console will display messages confirming the successful creation of these files, including their file paths.

## Requirements

- Python 3.6+
- requests
- Other dependencies listed in requirements.txt
