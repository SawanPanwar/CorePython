import datetime

dob = datetime.date(2000, 7, 25)

today = datetime.date.today()

age = today.year - dob.year

if (today.month, today.day) < (dob.month, dob.day):
    age -= 1

print("Your age is:", age)