import os
import shutil
import zipfile
from collections import defaultdict

def organize_files(directory):
    stl_dir = os.path.join(directory, "STL Files")
    zip_dir = os.path.join(directory, "ZIP Files")
    threemf_dir = os.path.join(directory, "3MF Files")

    os.makedirs(stl_dir, exist_ok=True)
    os.makedirs(zip_dir, exist_ok=True)
    os.makedirs(threemf_dir, exist_ok=True)

    file_types = defaultdict(list)

    # Traverse the directory hierarchy and collect all file paths
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_type = get_file_type(file_path)

            # Add the file path to the list of its corresponding file type
            file_types[file_type].append(file_path)

    # Move or copy files to the corresponding directories based on their type
    for file_type, file_paths in file_types.items():
        if file_type == "stl":
            for file_path in file_paths:
                shutil.move(file_path, stl_dir)
        elif file_type == "zip":
            for file_path in file_paths:
                extract_zip_file(file_path, zip_dir)
        elif file_type == "3mf":
            for file_path in file_paths:
                shutil.move(file_path, threemf_dir)

def get_file_type(file_path):
    # Determine the file type based on its extension
    _, extension = os.path.splitext(file_path)
    if extension.lower() == ".stl":
        return "stl"
    elif extension.lower() == ".zip":
        return "zip"
    elif extension.lower() == ".3mf":
        return "3mf"
    else:
        return "other"

def extract_zip_file(zip_file_path, output_dir):
    # Open the ZIP file and get a list of its contents
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_contents = zip_ref.namelist()

        # Extract each file in the ZIP archive if it doesn't already exist in the output directory
        for file_name in zip_contents:
            extracted_file_path = os.path.join(output_dir, file_name)
            if not os.path.exists(extracted_file_path):
                zip_ref.extract(file_name, output_dir)

if __name__ == "__main__":
    directory_to_organize = "path/to/your/directory"
    organize_files(directory_to_organize)