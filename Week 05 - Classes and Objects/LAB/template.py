"""
RECORD CHECK  -  my version
===========================

Name  : Joash Kabachi
Lane  : IT    
Date  : 10/25/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""
# create the record class
class Record:
    over_limit_count = 0

    def __init__(self, label, value, limit):
        """Store the record details."""
        #save the details for each record
        self.label = label
        self.value = value
        self.limit = limit

    def status(self):
        """Return the record status."""
        #check if the record has reached its limit
        if self.value >= self.limit:
            return "OVER LIMIT"
        elif self.value >= self.limit * 0.9:
            return "WARNING"
        else:
            return "OK"
def load_records(path):
    """Load records from a file."""
    #create an empty list for the three records
    records = []
    #open the file and reach each line
    with open(path, "r") as file:
        for line in file:
            parts = line.strip().split(",")
            record = Record(parts[0], float(parts[1]), float(parts[2]))
            records.append(record)
    return records
#create a record object using the file deatils
records = load_records("LAB/records.txt")
count = 0
for record in records:
    status = record.status()
    print()
    print("=" * 34)
    print(f"  RECORD CHECK - {record.label}")
    print("=" * 34)
    print("  GB used:", record.value)
    print("  GB total:", record.limit)
    print("  Status:", status)
    print("=" * 34)
    if status == "OVER LIMIT":
        count += 1
print()
print(count, "of", len(records), "records are OVER LIMIT")
