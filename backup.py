import os
import shutil
import sys
from datetime import datetime

# Function to perform the backup
def backup_files(src_dir, dest_dir):
    # Check if both source and destination directories exist
    if not os.path.exists(src_dir) or not os.path.exists(dest_dir):
        print(f"Error: Check if both directories exist.")
        return
    
    # Iterate over all files in the source directory
    for filename in os.listdir(src_dir):
        src_file = os.path.join(src_dir, filename)
        dest_file = os.path.join(dest_dir, filename)

        # Proceed only if the current item is a file
        if os.path.isfile(src_file):
            # If the file exists in the destination, append a timestamp to its name
            if os.path.exists(dest_file):
                name, ext = os.path.splitext(filename)
                timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
                dest_file = os.path.join(dest_dir, f"{name}_{timestamp}{ext}")
            
            # Copy the file from the source to the destination directory
            shutil.copy2(src_file, dest_file)
            print(f"Copied: {src_file} -> {dest_file}")

if __name__ == "__main__":
    # Ensure the correct number of command-line arguments are provided
    if len(sys.argv) != 3:
        print("Usage: python backup.py /path/to/source /path/to/destination")
    else:
        # Run the backup process with the provided source and destination directories
        backup_files(sys.argv[1], sys.argv[2])
