import os
import sys

def get_total_size(directory_path):
    try:
        if not os.path.isdir(directory_path):
            raise FileNotFoundError(f"Path Invalid: {directory_path}")

        total_size = 0

        for dirpath, dirnames, filenames in os.walk(directory_path):
            for filename in filenames:
                file_path = os.path.join(dirpath, filename)
                try:
                    if not os.path.islink(file_path):
                        total_size += os.path.getsize(file_path)
                except Exception as e:
                    print(f"Eroare in accesarea fisierului '{file_path}': {e}")

        print(f"Dimenisiune totala a '{directory_path}': {total_size} bytes")
    except Exception as e:
        print(f"Eroate: {e}")

if len(sys.argv) != 2:
    print("Comanda: python script.py <directory_path>")
else:
    directory_path = sys.argv[1]
    get_total_size(directory_path)
