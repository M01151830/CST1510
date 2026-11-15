"""
RECORD CHECK  -  my version
===========================

Name  :Joash kabachi
Lane  :   IT      (delete two)
Date  : 11/15/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""


# =================================================================== FUNCTIONS

def parse_line(raw_line):
    """Clean a raw server record and convert its values."""

    # Remove spaces from the beginning and end of the line
    # Convert all letters to lowercase so the data has the same format
    clean_line = raw_line.strip().lower()

    # Split the line at each comma to separate the server information
    fields = clean_line.split(",")

    # Get the server name from the first field and remove extra spaces
    server = fields[0].strip()

    # Split the second field at "=" and get the number after it
    # Remove extra spaces and convert the number from a string to an integer
    used = int(fields[1].split("=")[1].strip())

    # Split the third field at "=" and get the number after it
    # Remove extra spaces and convert the number from a string to an integer
    total = int(fields[2].split("=")[1].strip())

    # Store the cleaned information in a dictionary
    # Each value is stored using its own key
    record = {
        "server": server,
        "used": used,
        "total": total
    }

    # Return the completed dictionary
    return record


def status_of(record):
    """Check whether a server has exceeded its usage limit."""

    # Check if the used storage is greater than the total storage
    if record["used"] > record["total"]:

        # Return OVER LIMIT if the used storage exceeds the total
        return "OVER LIMIT"

    else:
        # Return OK if the server has not exceeded its limit
        return "OK"


# ====================================================================== INPUT

# Open the server records file in read mode
# Read all the lines from the file and store them in a list
with open("LAB/server_records.txt", "r") as file:
    raw_records = file.readlines()


# =============================================================== PROCESS + OUTPUT

# Create a variable to count how many servers are over their limit
flagged_count = 0

# Go through each raw record in the list one at a time
for raw_record in raw_records:

    # Call parse_line() to clean the raw record and create a dictionary
    record = parse_line(raw_record)

    # Call status_of() to check the server's storage status
    status = status_of(record)

    # Print the cleaned dictionary alongside its status
    print(record, status)

    # Check whether the server is over its storage limit
    if status == "OVER LIMIT":

        # Increase the flagged count by one
        flagged_count += 1


# Print the total number of records processed
print("Total records:", len(raw_records))

# Print the number of servers that exceeded their storage limit
print("Flagged records:", flagged_count)
