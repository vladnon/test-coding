import os
import sys


def get_dir_path():
    path = sys.argv[1]
    return path

def check_if_its_python_file(file):
    return file.endswith(".py")

def count_lines(file):
    lines = 0
    print(file)
    f = open(file)
    for line in f:
        lines += 1
    f.close()
    return lines

def go_to_the_dir(path):
    os.chdir(path) 

def go_through_the_files(root, files):
    total_lines = 0
    for file in files:
        if check_if_its_python_file(file):
            file_path = os.path.join(root, file)
            total_lines += count_lines(file_path)
    return total_lines

def count_lines_in_dir():
    total_lines = 0
    for root, dirs, files in os.walk("."):
        total_lines += go_through_the_files(root, files)
    return total_lines

def main():
    print("                          ")
    print("--------------------------")
    print("                          ")
    print("This is utility for counting lines is in project. The path starts from $HOME/") 
    print("It will print all filles in dir: \n")
    path = get_dir_path()
    go_to_the_dir(path)     
    total_lines = count_lines_in_dir()
    print("                          ")
    print("--------------------------")
    print("                          ")
 
    print(f"In this project there are {total_lines} lines")
main()
