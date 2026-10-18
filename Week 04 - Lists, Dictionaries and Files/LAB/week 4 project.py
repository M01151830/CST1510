"""
RECORD CHECK  -  my version
===========================

Name  :JOASH KABACHI
Lane  :   IT    
Date  : 10/18/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# load records from a file
def load_records(path):
    records = []
    with open(path) as f:
        for line in f:
            label, value, limit = line.strip().split(",")
            record = {
                "label": label,
                "value": float(value),
                "limit": float(limit)
            }
            records.append(record)
    return records

# check whether a record is over its limit
def check_record(record):
    if record["value"] > record["limit"]:
        return "OVER LIMIT"
    else:
        return "OK"


# print the record and its status
def print_report(record):
    """Print a record report."""
    status = check_record(record)
    print(record["label"] + ": " + status)
records = []
# trying to load records
try:
    records = records = load_records("records_sample.txt")
except FileNotFoundError:
    print("Error: records_sample.txt was not found.")
    records = []
# Start the over-limit count at zero
over_limit = 0
f = open("results.txt", "w")
for record in records:
    status = check_record(record)
    print_report(record)
    if status == "OVER LIMIT":
        over_limit = over_limit + 1
    # Write the label and status to the file
    f.write(record["label"] + "," + status + "\n")
# Close the results file
f.close()
print("Records over limit:", over_limit)

f = open("results.txt")
print(f.read())
f.close()




 