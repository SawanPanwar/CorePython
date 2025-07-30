import datetime

today = datetime.date.today()

print("Without Formatted date:", today)

formatted = today.strftime("%d-%m-%Y")

print("Formatted date:", formatted)