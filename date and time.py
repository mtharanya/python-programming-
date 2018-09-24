from datetime import datetime

d1 = datetime.strptime("01:05:00.000", "%H:%M:%S.%f")
d2 = datetime.strptime("00:50:00.000", "%H:%M:%S.%f")

print (d1-d2)
