import os
import sys

def count_files_by_extension(directory_path):
    if not os.path.exists(directory_path):
        print(f"The directory '{directory_path}' does not exist.")
        return

    if not os.access(directory_path, os.R_OK):
        raise PermissionError(f"You don't have permission to access '{directory_path}'.")

    try:
        files = os.listdir(directory_path)

        if not files:
            print(f"The directory '{directory_path}' is empty.")
            return

        extension_count = {}
        for file_name in files:
            if os.path.isfile(os.path.join(directory_path, file_name)):
                file_extension = os.path.splitext(file_name)[1]
                extension_count[file_extension] = extension_count.get(file_extension, 0) + 1

        if not extension_count:
            print(f"No files with extensions found in '{directory_path}'")
            return

        print("File extensions count:")
        for ext, count in extension_count.items():
            print(f"{ext}: {count}")


    except PermissionError as e:
        print(f"Permission Error: {e}")

    except OSError as e:
        print(f"Error occurred: {e}")


if len(sys.argv) != 2:
    print("Usage: python script_name.py <directory_path>")
else:
    directory_path = sys.argv[1]
    count_files_by_extension(directory_path)
