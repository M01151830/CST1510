"""
RECORD CHECK  -  my version
===========================

Name  : JOASH KABACHI
Lane  : IT
Date  : 10/03/2026
"""
# IT MINI PROJECT  WEEK 2 
hostname = input("hostname:")
used= float(input("GB used:"))
total= float(input("GB total:"))
free_gb = total - used
percent = (used / total) * 100
if percent>=100:
    status = "over limit"
elif percent >=90:
    status = "warning"
else:
    status = "ok"
print("=" *34)
print(f"RECORD CHECK: {hostname}")
print("=" *34)
print(f"used:{used:.2f}")
print(f"total:{total:.2f}")
print(f"free:{free_gb:.2f}")
print(f"percent:{percent:.2f}%")
print(f"status: {status}")
print("=" *34)
over_limit_count=0
while True:
    hostname=input("hostname:")
    if hostname=="quit":
        break
    used= float(input("GB used:"))
    total= float(input("GB total:"))
    free_gb = total - used
    percent = (used / total) * 100
    if percent>=100:
        status = "over limit"
        over_limit_count += 1
    elif percent >=90:
        status = "warning"
    else:
        status = "ok"
    print("=" *34)
    print(f"RECORD CHECK: {hostname}")
    print("=" *34)
    print(f"used:{used:.2f}")
    print(f"total:{total:.2f}")
    print(f"free:{free_gb:.2f}")
    print(f"percent:{percent:.2f}%")
    print(f"status: {status}")
    print("=" *34)
    print("over limit count:",)
