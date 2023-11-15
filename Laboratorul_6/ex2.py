import os
import sys

def rename_files(directory_path):
    try:

        if not os.path.isdir(directory_path):
            raise FileNotFoundError(f"Path invalid: {directory_path}")

        files = os.listdir(directory_path)

        if not files:
            print(f"The directory '{directory_path}' is empty.")
            return

        files.sort()
        for i, file_name in enumerate(files, start=1):

            old_path = os.path.join(directory_path, file_name)
            file_extension = os.path.splitext(file_name)[1]
            new_name = f"file{i}{file_extension}"

            new_path = os.path.join(directory_path, new_name)
            os.rename(old_path, new_path)
            print(f"Redenumire '{file_name}' la '{new_name}'")

        print("Toate fisierele au fost redenumite!")
    except Exception as e:
        print(f"Eroare in denumirea fisierului: {e}")


if len(sys.argv) != 2:
    print("Comanda: python script.py <directory_path>")
else:
    directory_path = sys.argv[1]
    rename_files(directory_path)
