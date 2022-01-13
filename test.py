import os
from pathlib import *
import sys
import argparse

detect_language = lambda file: PurePath(file).suffix # Returns language file extension

is_text_file = lambda file: False if detect_language(file) == "" else True # Check if file is text file or not 


def count_blank_lines(file):
    blank_lines = 0
    with open(file,"r", errors="ignore") as f:
        for line in f.readlines():
            if line.isspace():
                blank_lines += 1
    return blank_lines

def count_loc(file):
    count = 0
    with open(file, "r", errors="ignore") as f:
        for line in f.readlines():
            if  len(line.strip()) > 0:
                count += 1
    return count

def countlines(dir: Path, lines=0,begin_start=None): 
    # file = thing
    exts = [".py", ".c", ".cpp"]

    for file in dir.rglob("*"):
        file = os.path.join(dir, file)
        if is_text_file(file):
            if file.endswith(exts[2]):
                blank_lines = count_blank_lines(file)
                lines_with_code = count_loc(file)
                total = count_loc(file) + blank_lines
                
                if begin_start != None:
                    reldir_of_thing = "." + file.replace(begin_start, "")
                else:
                    reldir_of_thing = "." + file.replace(str(dir), "")

                print("{:>10} |{:>10} |{:>10} | {:<20}".format(
                        lines_with_code,blank_lines, total, reldir_of_thing))
    #for thing in os.listdir(dir):
    for file in dir.rglob("*"):    
        #thing = os.path.join(dir, thing)
        file = os.path.join(dir, file)
        if os.path.isdir(file):
            lines = countlines(file, lines,begin_start=dir)


print("{:>10} |{:>10} |{:>10} | {:<20}".format("FULL LINES","BLANK", "TOTAL", "FILE"))
print("{:->11}|{:->11}|{:->20}".format("", "", ""))

parser = argparse.ArgumentParser()

parser.add_argument(
    "directory", help="Name of folder or directory u wish to scan")
# parser.add_argument(
#     "-e", nargs='+', help="Extensions u wish to scan for", required=False)

args = parser.parse_args()
countlines(Path(args.directory))