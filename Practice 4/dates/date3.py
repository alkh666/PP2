from datetime import datetime
now = datetime.now()
n = now.replace(microsecond=0)
print(n)