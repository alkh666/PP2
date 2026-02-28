from datetime import datetime
d1 = datetime(2026, 2, 28, 12, 0, 0)
d2 = datetime(2026, 3, 1, 14, 30, 0)
d= d2 - d1
sec = d.total_seconds()
print(int(sec))