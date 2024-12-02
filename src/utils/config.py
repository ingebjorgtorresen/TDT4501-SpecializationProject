import os

# Base directory (project root) - Adjusted to point to the correct location
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # One level up to project root

# Data directory
DATA_PATH = os.path.join(BASE_DIR, "data")

# Full path to the CSV file
DATA_FILE = os.path.join(DATA_PATH, "all.csv")

# Print paths for debugging (optional, but helpful)
print("Base directory:", BASE_DIR)
print("Data path:", DATA_PATH)
print("CSV file path:", DATA_FILE)
