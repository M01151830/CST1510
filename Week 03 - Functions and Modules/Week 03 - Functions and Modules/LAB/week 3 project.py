"""
RECORD CHECK  -  my version
===========================

Name  : Joash Kabachi
Lane  :   IT      
Date  :10/11/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# =================================================================== FUNCTIONS
def status_of(percent):
    """Return the status based on the percentage."""
    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= 75:
        return "WARNING"
    else:
        return "OK"


def check(value, limit):
    """Calculate and return the difference and percentage."""
    difference = limit - value
    percent = value / limit * 100
    return difference, percent


def print_report(label, value, limit, difference, percent, status):
    """Print the record details in a bordered report."""
    print()
    print("=" * 34)
    print(f"record check-{label}")
    print("=" * 34)
    print(f"Used     : {value:>8.2f}")
    print(f"Total    : {limit:>8.2f}")
    print(f"Free     : {difference:>8.2f}")
    print(f"Percent  : {percent:>8.2f} %")
    print(f"Status   : {status:>8}")
    print("=" * 34)
over_count = 0
while True:
    label = input("\nLabel (or quit): ")

    if label.lower() == "quit":
        break

    value = float(input("Value: "))
    limit = float(input("Limit: "))
# ===================================================== PROCESS
    difference, percent = check(value, limit)
    status = status_of(percent)
    # ===================================================== OUTPUT
    print_report(label, value, limit, difference, percent, status)

    if status == "OVER LIMIT":
        over_count += 1
print()
print("Number of records OVER LIMIT:", over_count)



