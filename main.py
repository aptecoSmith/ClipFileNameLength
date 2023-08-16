import os
import argparse


def rename_files(folder_path, min_length):
    try:
        # Check if the folder path exists
        if not os.path.exists(folder_path):
            print("Folder path does not exist.")
            return

        # List all files in the folder
        files = os.listdir(folder_path)

        for file in files:
            file_path = os.path.join(folder_path, file)
            if os.path.isfile(file_path):
                # Check the character length of the file name
                if len(file) > min_length:
                    new_name = f"new_{file}"
                    new_file_path = os.path.join(folder_path, new_name)
                    os.rename(file_path, new_file_path)
                    print(f"Renamed: {file} -> {new_name}")

    except Exception as e:
        print(f"An error occurred: {e}")


def main():
    parser = argparse.ArgumentParser(
        description="Rename files in a folder with a character length over a given number.")
    parser.add_argument("folder_path", help="Path to the folder containing the files.")
    parser.add_argument("min_length", type=int, help="Minimum character length for renaming.")
    args = parser.parse_args()

    rename_files(args.folder_path, args.min_length)


if __name__ == "__main__":
    main()