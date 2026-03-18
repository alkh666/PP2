import os
from pathlib import Path
# Exercise 1 - Create nested directories

# os.makedirs creates all folders in the path at once
# exist_ok=True means no error if folder already exists
os.makedirs("project/src/utils", exist_ok=True)
os.makedirs("project/tests",     exist_ok=True)
os.makedirs("project/docs",      exist_ok=True)
os.makedirs("data/2024/january", exist_ok=True)
os.makedirs("data/2024/february",exist_ok=True)

# pathlib way - same result, different style
Path("data/2024/march").mkdir(parents=True, exist_ok=True)

print("Folders created:")
for p in sorted(Path(".").rglob("*")):
    if p.is_dir():
        depth = len(p.parts) - 1
        print("  " + "  " * depth + p.name + "/")

# add some sample files
sample_files = [
    ("project/src/main.py",       "print('hello')"),
    ("project/src/utils/math.py", "def add(a, b): return a + b"),
    ("project/tests/test_main.py","import unittest"),
    ("project/docs/README.md",    "# Project Docs"),
    ("data/2024/january/data.csv","date,amount\n01-01,1500"),
    ("data/2024/february/data.csv","date,amount\n01-02,2100"),
    ("data/2024/march/data.csv",  "date,amount\n01-03,1800"),
]
for path, content in sample_files:
    Path(path).write_text(content)

# Exercise 2 - List files and folders

# os.listdir - shows direct children of a folder
print("\nos.listdir('project'):")
for item in sorted(os.listdir("project")):
    full = os.path.join("project", item)
    kind = "DIR " if os.path.isdir(full) else "FILE"
    print(" ", kind, item)

# os.walk - walks the full tree recursively
print("\nos.walk('project'):")
for root, dirs, files in os.walk("project"):
    depth = root.count(os.sep)
    indent = "  " * depth
    print(indent + os.path.basename(root) + "/")
    for name in sorted(files):
        print(indent + "  " + name)

# os.getcwd and os.chdir
print("\nos.getcwd():", os.getcwd())
os.chdir("project")
print("after chdir('project'):", os.getcwd())
os.chdir("..")
print("after chdir('..'):", os.getcwd())

# Exercise 3 - Find files by extension

# glob - search inside one folder only
print("\n.py files in project/src:")
for f in sorted(Path("project/src").glob("*.py")):
    print(" ", f)

# rglob - search recursively through all subfolders
print("\nAll .py files (rglob):")
for f in sorted(Path("project").rglob("*.py")):
    print(" ", f)

print("\nAll .csv files with sizes:")
for f in sorted(Path("data").rglob("*.csv")):
    print(f"  {f}  ({f.stat().st_size} bytes)")

# os.walk way - classic approach
print("\nAll .md files via os.walk:")
for root, dirs, files in os.walk("."):
    for name in sorted(files):
        if name.endswith(".md"):
            print(" ", os.path.join(root, name))

# group files by extension
from collections import defaultdict
groups = defaultdict(list)
for f in Path(".").rglob("*"):
    if f.is_file():
        groups[f.suffix].append(f.name)

print("\nAll files grouped by extension:")
for ext in sorted(groups):
    print(f"  {ext or '(none)'}: {sorted(groups[ext])}")


# Clean up for next exercise
import shutil
shutil.rmtree("project", ignore_errors=True)
shutil.rmtree("data", ignore_errors=True)