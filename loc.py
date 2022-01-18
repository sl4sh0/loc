import os
from pathlib import *
import sys
from collections import Counter

detect_language = lambda file: PurePath(file).suffix # Returns language file extension

is_text_file = lambda file: False if detect_language(file) == "" else True # Check if file is text file or not


def count_blank_lines(file):
    blank_lines = 0
    with open(file, "r", errors="ignore") as f:
        for line in f.readlines():
            if line.isspace():
                blank_lines += 1
    return blank_lines


def count_loc(file):
    count = 0
    with open(file, "r", errors="ignore") as f:
        for line in f.readlines():
            if len(line.strip()) > 0:
                count += 1
    return count


def count_lines_for_ext(dir):
    counts = Counter()

    if "-e" in sys.argv:
        indx = (sys.argv.index("-e"))
        exts = sys.argv[indx+1::]

    for file in dir.rglob("*"):
        file = os.path.join(dir, file)
        if is_text_file(file):
            for ext in exts:
                if file.endswith(ext):
                    blank_lines = count_blank_lines(file)
                    lines_with_code = count_loc(file)
                    total = count_loc(file) + blank_lines
                    
                    counts[ext] += total

                    reldir_of_thing = "." + file.replace(str(dir), "")

                    print("{:>10} |{:>10} |{:>10} | {:<20}".format(
                        lines_with_code, blank_lines, total, reldir_of_thing))
                        
    for i in counts:
        print("{} {} LINES TOTAL".format(i, counts[i]))

    c = 0
    for i in counts:
        c += counts[i]
    print(f"TOTAL LINES: {c}")


print("{:>10} |{:>10} |{:>10} | {:<20}".format(
    "FULL LINES", "BLANK", "TOTAL", "FILE"))
print("{:->11}|{:->11}|{:->20}".format("", "", ""))
