import os
from dotenv import load_dotenv
print("Starting ETL Pipeline...\n")

extract = os.system("python extract.py")

if extract == 0:
    print("✓ Extraction completed successfully.\n")
else:
    print("✗ Extraction failed.")
    exit()

transform = os.system("python transform.py")

if transform == 0:
    print("✓ Transformation completed successfully.\n")
else:
    print("✗ Transformation failed.")
    exit()

load = os.system("python load.py")

if load == 0:
    print("✓ Data loaded into PostgreSQL successfully.\n")
else:
    print("✗ Loading failed.")
    exit()

print("=" * 50)
print("🎉 ETL Pipeline completed successfully!")
print("=" * 50)