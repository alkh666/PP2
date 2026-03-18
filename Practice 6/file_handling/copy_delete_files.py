import os
import shutil
from pathlib import Path

# create a file to work with
with open("report.txt", "w") as f:
    f.write("Sales Report\n")
    f.write("January:  15000\n")
    f.write("February: 18000\n")
    f.write("March:    21000\n")
# Exercise 4 - Copy and back up files with shutil
# copy file to same folder
shutil.copy("report.txt", "report_copy.txt")
print("Copied: report.txt -> report_copy.txt")

# copy to a backup folder (copy2 also keeps metadata)
os.makedirs("backups", exist_ok=True)
shutil.copy2("report.txt", "backups/report_backup.txt")
print("Backup saved: backups/report_backup.txt")

# copy an entire folder
shutil.copytree("backups", "backups_archive")
print("Folder copied: backups -> backups_archive")

print("\nContents of backups/:")
for name in os.listdir("backups"):
    print(" ", name)

# Exercise 5 - Delete files safely
# method 1: check first with os.path.exists
if os.path.exists("report_copy.txt"):
    os.remove("report_copy.txt")
    print("Deleted: report_copy.txt")

# method 2: try/except handles missing file gracefully
try:
    os.remove("ghost.txt")
except FileNotFoundError:
    print("ghost.txt not found - skipped")

# method 3: pathlib with missing_ok - cleanest way
Path("ghost.txt").unlink(missing_ok=True)
print("unlink(missing_ok=True) - no error raised")

# delete a folder and everything inside it
shutil.rmtree("backups_archive")
print("Deleted folder: backups_archive")


# Clean up
Path("report.txt").unlink(missing_ok=True)
shutil.rmtree("backups", ignore_errors=True)