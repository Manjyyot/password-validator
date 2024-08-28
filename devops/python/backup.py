import os
import shutil
from datetime import datetime

# Function to append a timestamp to the filename for uniqueness
def append_timestamp(filename):
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    name, ext = os.path.splitext(filename)
    return f"{name}_{timestamp}{ext}"

# Function to perform the backup process
def backup(src, dest):
    # Replace backslashes with forward slashes in paths
    src = src.replace('\\', '/')
    dest = dest.replace('\\', '/')
    
    # Check if the source and destination paths exist
    if not os.path.exists(src):
        print(f"Error: Source '{src}' does not exist.")
        return
    
    if not os.path.exists(dest):
        print(f"Error: Destination '{dest}' does not exist.")
        return
    
    # If the source is a file, handle it directly
    if os.path.isfile(src):
        dest_file = os.path.join(dest, os.path.basename(src))
        if os.path.exists(dest_file):
            dest_file = append_timestamp(dest_file)
        shutil.copy2(src, dest_file)
        print(f"Copied: {src} -> {dest_file}")
    
    # If the source is a directory, iterate over its contents
    elif os.path.isdir(src):
        for filename in os.listdir(src):
            src_file = os.path.join(src, filename)
            dest_file = os.path.join(dest, filename)
            if os.path.isfile(src_file):
                if os.path.exists(dest_file):
                    dest_file = os.path.join(dest, append_timestamp(filename))
                shutil.copy2(src_file, dest_file)
                print(f"Copied: {src_file} -> {dest_file}")

if __name__ == "__main__":
    # Prompt the user for the source and destination paths
    src = input("Enter the source path (file or directory): ").replace('\\', '/')
    dest = input("Enter the destination directory path: ").replace('\\', '/')
    
    # Run the backup process
    backup(src, dest)
