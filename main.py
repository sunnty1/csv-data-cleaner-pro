import os
import pandas as pd

print("CSV Cleaner Pro Started")

file = input(
    "Enter CSV file name: "
)

while True:
    file = input(
        "Enter CSV file name: "
    )

    if os.path.exists(file):
        break

    print(
        "File not found. Try again."
    )
df = pd.read_csv(file)

before = len(df)

# duplicate sil
df = df.drop_duplicates()

# boş yaş
df["Age"] = df["Age"].fillna("Unknown")

# boş email
df["Email"] = df["Email"].fillna("missing@email.com")

# isim düzelt
df["Name"] = df["Name"].str.title()

# ülke düzelt
df["Country"] = df["Country"].str.title()

after = len(df)

df.to_csv(
  output_file = "cleaned_" + file  df.to_csv(
    output_file,
    index=False
)

report = f"""
Rows before: {before}
Rows after: {after}
Removed: {before-after}
"""

with open(
    "report.txt",
    "w"
) as f:
    f.write(report)

print("CSV cleaned successfully!")
print("Report generated.")
print("Saved:")
print("- cleaned_customers.csv")
print("- report.txt")
print()
print("Summary:")
print(f"Rows before: {before}")
print(f"Rows after: {after}")
print(f"Removed: {before-after}")