# TSV data files to CSV

This repository provides a Python script that combines multiple large TSV files into a single CSV file. It's particularly useful for datasets like AlphaMissense or other bioinformatics data that can span millions of rows across multiple files. The script handles potential issues like inconsistent row lengths, missing headers, and large data sizes that exceed typical spreadsheet limits.

Before you can use this script, ensure that you have the following installed:

```Python 3.x
pandas and openpyxl library```

```pip install pandas openpyxl```
