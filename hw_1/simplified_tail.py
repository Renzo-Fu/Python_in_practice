import sys


def tail(files, default_line_count=10):
    def print_tail(file_name=None, line_count=default_line_count):
        if file_name:
            try:
                with open(file_name, 'r') as file:
                    lines = file.readlines()
            except FileNotFoundError:
                print(f"File {file_name} not found.")
                return
        else:
            lines = sys.stdin.readlines()
            line_count = 17  # Override line_count for stdin

        for line in lines[-line_count:]:
            print(line, end='')

    if files:
        for i, file_name in enumerate(files):
            if len(files) > 1:  # If more than one file, print the file name
                print(f"==> {file_name} <==")
            print_tail(file_name=file_name)
            if i < len(files) - 1:  # Add a newline between files except for the last one
                print()
    else:
        # Call without file_name for stdin, using 17 lines by default
        print_tail(line_count=17)


if __name__ == "__main__":
    tail(sys.argv[1:])
