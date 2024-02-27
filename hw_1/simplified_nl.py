import sys


def number_lines(file=None):
    if file:
        try:
            with open(file, 'r') as f:
                for i, line in enumerate(f, 1):
                    print(f"{i}\t{line}", end='')
        except FileNotFoundError:
            print(f"File {file} not found.")
    else:
        for i, line in enumerate(sys.stdin, 1):
            print(f"{i}\t{line}", end='')


if __name__ == "__main__":
    if len(sys.argv) > 1:
        number_lines(sys.argv[1])
    else:
        number_lines()
