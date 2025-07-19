import os
import shutil

# Source and destination folders (relative to your current directory)
source_folder = "test_files"
destination_folder = "copied_files"

# Create destination folder if not exists
os.makedirs(destination_folder, exist_ok=True)

# Go through each file in source folder
for file_name in os.listdir(source_folder):
    if file_name.endswith(".txt") or file_name.endswith(".csv"):
        source_path = os.path.join(source_folder, file_name)
        destination_path = os.path.join(destination_folder, file_name)
        shutil.copy(source_path, destination_path)
        print(f"Copied: {file_name}")

print("✅ All eligible files copied.")
