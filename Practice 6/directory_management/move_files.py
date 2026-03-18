import os
import shutil
from pathlib import Path
os.makedirs("project/src", exist_ok=True)
os.makedirs("project/docs", exist_ok=True)
os.makedirs("data/january", exist_ok=True)
os.makedirs("data/february", exist_ok=True)
os.makedirs("data/march", exist_ok=True)

Path("project/src/main.py").write_text("print('hello')")
Path("project/src/utils.py").write_text("def add(a, b): return a + b")
Path("project/docs/README.md").write_text("# Docs")
Path("data/january/sales.csv").write_text("date,amount\n01-01,1500")
Path("data/february/sales.csv").write_text("date,amount\n01-02,2100")
Path("data/march/sales.csv").write_text("date,amount\n01-03,1800")

# Exercise 4 - Move and copy files between folders
# shutil.copy - copy one file
os.makedirs("reports", exist_ok=True)
shutil.copy("data/january/sales.csv", "reports/january_sales.csv")
print("Copied: data/january/sales.csv -> reports/january_sales.csv")

# copy all csv files into reports/ with renamed files
print("\nCopying all csv files to reports/:")
for csv_file in Path("data").rglob("*.csv"):
    month = csv_file.parent.name
    dest  = Path("reports") / (month + "_sales.csv")
    shutil.copy(csv_file, dest)
    print(f"  {csv_file} -> {dest}")

# shutil.move - move a file (removes the original)
shutil.move("project/docs/README.md", "project/README.md")
print("\nMoved: project/docs/README.md -> project/README.md")
print("Original exists:", Path("project/docs/README.md").exists())
print("New path exists:", Path("project/README.md").exists())

# shutil.copytree - copy an entire folder
shutil.copytree("project/src", "project/src_backup")
print("\nFolder copied: project/src -> project/src_backup")
print("Files in src_backup:", os.listdir("project/src_backup"))

# shutil.move on a folder - moves whole folder
os.makedirs("archive", exist_ok=True)
shutil.move("project/src_backup", "archive/src_backup")
print("\nFolder moved: project/src_backup -> archive/src_backup")

print("\nFinal contents of reports/:")
for f in sorted(Path("reports").iterdir()):
    print(f"  {f.name}  ({f.stat().st_size} bytes)")


# Clean up
shutil.rmtree("project", ignore_errors=True)
shutil.rmtree("data", ignore_errors=True)
shutil.rmtree("reports", ignore_errors=True)
shutil.rmtree("archive", ignore_errors=True)