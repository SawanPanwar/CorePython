import datetime

today = datetime.date.today()
future = today + datetime.timedelta(days=7)
past = today - datetime.timedelta(days=7)

print("7 days later:", future)
print("7 days ago:", past)