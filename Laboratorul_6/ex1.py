import os
import sys
def read_file(directory_path, file_extension):
    try:
        if not os.path.exists(directory_path):
            raise FileNotFoundError(f"Path invalid: {directory_path}")

        if not os.path.isdir(directory_path):
            raise NotADirectoryError(f"{directory_path} nu este directory.")

        matching_files = [file for file in os.listdir(directory_path) if file.endswith(file_extension)]

        if not matching_files:
            print(f"Nu exista fisiere cu extensia '{file_extension}' in folderul '{directory_path}'")
            return

        for file_name in matching_files:
            file_path = os.path.join(directory_path, file_name)
            try:
                with open(file_path, 'r') as file:
                    contents = file.read()
                    print(f"Continutul fisierului: '{file_name}':\n{contents}\n")

            except FileNotFoundError:
                print(f"Fisierul '{file_name}' nu a fost gasit")

            except Exception as e:
                print(f"Eroarea la citirea fisierului '{file_name}': {e}")

    except Exception as e:
        print(f"Eroare: {e}")


if len(sys.argv) != 3:
    print("Comanda ar trebui sa fie: python ex1.py <directory_path> <file_extension>")
else:
    directory_path, file_extension = sys.argv[1], sys.argv[2]
    read_file(directory_path, file_extension)
