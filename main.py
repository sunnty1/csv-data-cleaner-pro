import os
import pandas as pd


print("=" * 40)
print("CSV DATA CLEANER PRO")
print("=" * 40)


# Dosya al
while True:
    file = input("\nEnter CSV file name: ").strip()

    if os.path.exists(file):
        break

    print("❌ File not found. Try again.")


try:
    df = pd.read_csv(file)

except Exception as e:
    print(f"\nError reading CSV: {e}")
    exit()


before = len(df)

print("\nCleaning started...\n")


# Duplicate temizle
duplicates = df.duplicated().sum()
df = df.drop_duplicates()


# Sütun kontrolü
if "Age" in df.columns:
    df["Age"] = df["Age"].fillna("Unknown")

if "Email" in df.columns:
    df["Email"] = (
        df["Email"]
        .fillna("missing@email.com")
        .astype(str)
        .str.lower()
    )

if "Name" in df.columns:
    df["Name"] = (
        df["Name"]
        .astype(str)
        .str.strip()
        .str.title()
    )

if "Country" in df.columns:
    df["Country"] = (
        df["Country"]
        .astype(str)
        .str.strip()
        .str.title()
    )


after = len(df)


# Çıkış dosyası
output_file = "cleaned_" + os.path.basename(file)

df.to_csv(
    output_file,
    index=False
)


# Rapor
report = f"""
CSV CLEAN REPORT
================

Input File:
{file}

Output File:
{output_file}

Rows Before:
{before}

Rows After:
{after}

Duplicates Removed:
{duplicates}

Success:
YES
"""


with open(
    "report.txt",
    "w",
    encoding="utf-8"
) as f:
    f.write(report)


print("\nSUCCESS")
print("-" * 20)

print(f"Input: {file}")
print(f"Output: {output_file}")
print(f"Rows Before: {before}")
print(f"Rows After: {after}")
print(f"Duplicates Removed: {duplicates}")

print("\nFiles created:")
print(f"✔ {output_file}")
print("✔ report.txt")