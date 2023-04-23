import sys
import pandas as pd

def parse_weblog(file_path, index, *fields):
    # Define the column names
    column_names = ["sip", "timestamp", "request", "status", "bytes", "referrer", "user_agent"]

    # Read the log file using pandas
    df = pd.read_csv(file_path, sep="|", header=None, names=column_names, on_bad_lines="skip")


    # Get the specified record by index
    record = df.loc[index]

    # Print the specified fields
    for field in fields:
        if field in column_names:
            print(f"{field}: {record[field]}")
        else:
            print(f"Field '{field}' not found in the schema")

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: script.py <log_file> <record_index> <field1> [<field2> ...]")
    else:
        file_path = sys.argv[1]
        index = int(sys.argv[2])
        fields = sys.argv[3:]
        parse_weblog(file_path, index, *fields)
