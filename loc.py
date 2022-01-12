from pathlib import *
from collections import Counter
import sys

Language = str

detect_language = lambda file: PurePath(file).suffix # Returns language file extension

is_text_file = lambda file: False if detect_language(file) == "" else True # Check if file is text file or not 

def count_loc(file: Path) -> int:
    count = 0
    with open(file, "r", errors="ignore") as f:
        for line in f.readlines():
            if len(line.strip()) > 0:
                count += 1
    return count


def main(directory: Path) -> dict[Language, int]:
    counts = Counter() # New empty counter is made

    assert directory.is_dir() # Exception is raised if directory is not directory or folder


    if "-e" in sys.argv:
        indx = (sys.argv.index("-e"))
        exts = sys.argv[indx+1::]
        for ext in exts:
            for file in directory.rglob("*"):
                if not is_text_file(file):
                    continue
                language = ext
                if language is None:
                    continue
                counts[language] += count_loc(file)
        x = counts 
    else:
        for file in directory.rglob("*"):
            if not is_text_file(file):
                continue
            language = detect_language(file)
            if language is None:
                continue
            # Counts for each detected language from detect_language() function + count lines of code per file
            counts[language] += count_loc(file)

        x = counts

    for i in x:
        print(i , "->", x[i])

