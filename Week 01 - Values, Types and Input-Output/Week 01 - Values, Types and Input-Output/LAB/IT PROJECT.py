"""
RECORD CHECK  -  my version
===========================

Name  :JOASH KABACHI
Lane  :   IT      (delete two)
Date  :9/27/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# mini - project - IT
hostname = input("enter hostname: ")
gb_used = float(input("enter gb used: "))
gb_total = float(input("enter gb total: "))

free_gb = gb_total - gb_used
percent_used = (gb_used/gb_total)*100
#useful because it shows the percentage of storage that is still free.

free_percent = (free_gb/gb_total)*100
print("="*34)
print(f" RECORD CHECK - {hostname} ")
print("=" *34)
print(f"gb used: {gb_used:10.2f} ")
print(f"gb total: {gb_total:10.2f} ")
print(f"free gb: {free_gb:+10.2f} ")
print(f"percent used: {percent_used:10.2f}% ")
print(f"free percent: {free_percent:10.2f}% ")
print("=" *34)