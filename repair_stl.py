import os
import sys
import trimesh

def repair_stl_file(file_path):
    print(f"Processing {file_path}")
    mesh = trimesh.load_mesh(file_path)

    if not mesh.is_watertight:
        print(f"Repairing {file_path}")
        mesh = mesh.fill_holes()
        mesh.export(file_path)

def process_directory(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.lower().endswith('.stl'):
                file_path = os.path.join(root, file)
                repair_stl_file(file_path)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script_name.py path/to/your/directory")
    else:
        directory_to_check = sys.argv[1]
        process_directory(directory_to_check)
