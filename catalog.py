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

import sys


def main(directory_name: str):
    print(directory_name)


if __name__ == '__main__':
    main(sys.argv[1])
