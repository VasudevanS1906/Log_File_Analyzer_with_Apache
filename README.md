# Log File Analyzer with Apache
The provided Python script, `analyze_log_file.py`, is designed to analyze log files, specifically Apache web server log files. It extracts relevant information from the log file, such as IP addresses, requested pages, and status codes, and provides a summary of the top IP addresses, requested pages, and status code counts. Additionally, it displays the total number of 404 errors.

# Requirements

- Python 3.x

# Usage

1. Save the `analyze_log_file.py` script in your desired directory.

2. Open a terminal or command prompt and navigate to the directory where the script is saved.

3. Run the script with the log file path as an argument:

```
python analyze_log_file.py <log_file_path>
```

Replace `<log_file_path>` with the actual path to your Apache log file. For example:

```
python analyze_log_file.py /path/to/Apache_logs_1.txt
```

4. The script will analyze the log file and print the following information:
   - Top 5 IP addresses and their counts
   - Top 5 requested pages and their counts
   - Status code summary with counts
   - Total number of 404 errors
  
# Screenshot

The following screenshot signifies the successful completion of the above program through the display of output

![Screenshot] (apache_success_output.jpg)

