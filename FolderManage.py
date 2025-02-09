import os
import shutil

# Define the source and destination directories
source_dir = "path"
video_dir = "path"
zip_dir = "path"
doc_dir = "path"
pic_dir = "path"
prog_dir = "path"
code_dir = "path"

# Create destination folders if they don't already exist
os.makedirs(video_dir, exist_ok=True)
os.makedirs(zip_dir, exist_ok=True)
os.makedirs(doc_dir, exist_ok=True)
os.makedirs(pic_dir, exist_ok=True)
os.makedirs(prog_dir, exist_ok=True)

# Define file type mappings
extensions_map = {
    pic_dir: [".png", ".jpg", ".jpeg"],
    video_dir: [".mp4", ".mkv", ".avi"],
    zip_dir: [".zip", ".rar", ".7z"],
    doc_dir: [".pdf", ".docx", ".xlsx", ".txt", ".doc", ".pptx", ".xls"],
    prog_dir: [".exe", ".msi"],
    code_dir: [".c", ".py", ".java"]
}

# Iterate over the files in the source directory
for entry in os.scandir(source_dir):
    # Skip directories to avoid unnecessary errors
    if entry.is_dir():
        continue

    # Get the file extension
    _, ext = os.path.splitext(entry.name)

    # Move files based on their extension
    for target_dir, extensions in extensions_map.items():
        if ext.lower() in extensions:
            shutil.move(entry.path, os.path.join(target_dir, entry.name))
            break
