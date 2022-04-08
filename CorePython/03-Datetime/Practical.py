from datetime import *

ints = date.today()
next_month = ints
for i in range(1,13):
    next_month = next_month + timedelta(days=30)
    print("Month = ",i,"Date = ",next_month)

