"""
Calculate the size of all files in the directory and any subdirectories
Print the value

Bonus:
Use python's ArgParser to set flags with special behavior
eg
    print max depth
    print number of files and total size
    print full file structure diagram
        - top directory
            - file one
            - file two
            - directory
                - file one
                - file two
"""
import os
import sys


def main(directory_name: str):
    value = calculate_size(directory_name)

    # TODO: Format output
    # TODO: Convert to MB
    print(value)


def validate_input():
    if len(sys.argv) < 2:
        print("gotta type something after catalog, bro.")
        sys.exit(1)
    if not os.path.isdir(sys.argv[1]):
        print(f"\"{sys.argv[1]}\" is not a valid directory.")
        sys.exit(1)


def calculate_size(directory: str):
    print(f"Checking directory \"{directory}\"...")
    contents = os.listdir(directory)
    cumulative_size = 0

    for item in contents:
        full_path = os.path.join(directory, item)
        if os.path.isfile(full_path):
            cumulative_size += os.path.getsize(full_path)
        elif os.path.isdir(full_path):
            cumulative_size += calculate_size(full_path)
        else:
            print(f"skipping voodoo item {full_path}")
    return cumulative_size


if __name__ == '__main__':
    validate_input()
    main(sys.argv[1])
