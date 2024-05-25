import os
import re


def camel_to_snake(camel_string):
    return re.sub(r'(?<!^)(?=[A-Z])', '_', camel_string).lower()


def rename_files_to_snake_case(directory):
    for root, dirs, files in os.walk(directory):
        for filename in files:
            old_path = os.path.join(root, filename)
            new_filename = camel_to_snake(filename)
            new_path = os.path.join(root, new_filename)

            if old_path != new_path:
                os.rename(old_path, new_path)
                print(f'Renamed: {old_path} -> {new_path}')


if __name__ == "__main__":
    target_directory = '.'  # Change this to your desired directory
    # target_directory = input("Enter the target directory path: ")
    # if target_directory == '':
    #     target_directory = '.'

    if os.path.exists(target_directory):
        rename_files_to_snake_case(target_directory)
        print("Renaming complete.")
    else:
        print("Directory not found.")
