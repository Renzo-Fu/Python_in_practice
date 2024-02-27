import sys


def count_lines_words_chars(file_name=None):
    if file_name:
        try:
            with open(file_name, 'r') as file:
                content = file.read()
        except FileNotFoundError:
            print(f"File {file_name} not found.")
            return None
    else:
        content = sys.stdin.read()

    lines = content.splitlines()
    words = content.split()
    chars = len(content)
    return len(lines), len(words), chars


def wc(files):
    total_lines, total_words, total_chars = 0, 0, 0
    for file_name in files:
        counts = count_lines_words_chars(file_name)
        if counts:
            print(f"{counts[0]:7} {counts[1]:7} {counts[2]:7} {file_name}")
            total_lines += counts[0]
            total_words += counts[1]
            total_chars += counts[2]

    if len(files) > 1:
        print(f"{total_lines:7} {total_words:7} {total_chars:7} total")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        wc(sys.argv[1:])
    else:
        counts = count_lines_words_chars()  # Reading from stdin
        if counts:
            print(f"{counts[0]:7} {counts[1]:7} {counts[2]:7}")
