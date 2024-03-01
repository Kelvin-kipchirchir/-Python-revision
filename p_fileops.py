#!/usr/bin/env python
import os
import glob
import pathlib
print("file operations")


#method 1
def list_files(dir_path):
    res = [] #stores the contents
    try:
        for file_path in os.listdir(dir_path):
            if os.path.isfile(os.path.join(dir_path,file_path)):
                res.append(file_path)
    except FileNotFoundError:
        print(f"The directory {dir_path} does not exist")
    except PermissionError:
        print(f"Permission denied to access the directory {dir_path}")
    except OSError as e:
        print(f"An OS error occured: {e}")
    return res


#directory/folder path
dir_path =r"C:\Users\Kelvin Walker\Desktop\backup"
files = list_files(dir_path)
print("All files present:",files)

print("*******using method 2************")
def get_files(path):
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path,file)):
            yield file

for file in get_files(r"C:\Users\Kelvin Walker\Desktop\Labs"):
    print(file)


print("************method 3****************")
dir_path =r"C:\Users\Kelvin Walker\Desktop\testdir"
res =os.listdir(dir_path)
print(res)

print("************method 4************")
#using the os.walk()
from os import walk
dir_path = r"C:\Users\Kelvin Walker\Desktop\audiofiles"
#list to store files name
res = []
for (dir_path,dir_names,file_names) in walk(dir_path):
    res.extend(file_names)
print(res)

print("**********method 5 get list of files in current directory******")
files = []
for file_path in os.listdir("."):
    if os.path.isfile(os.path.join(".",file_path)):
        files.append(file_path)

for file in files:
    print(file)


print("------------------method 6:using the scan dir() method---------")
dir_path = r"C:\Users\Kelvin Walker\Desktop\backup"
for path in os.scandir(dir_path):
    if path.is_file():
        print(path.name)

print("------------------method 7:listing files that follow specific direction--------------------")
#serch all files inside a specific folder
#*.* means file name with any extension
dir_path = r'C:\Users\Kelvin Walker\Desktop\backup\*.*'
res = glob.glob(dir_path)
print(res)

print("---------------method 8:listing recursively---------------")
dir_path = r'C:\Users\Kelvin Walker\Desktop\backup\**\*.*'
for file in glob.glob(dir_path,recursive=True):
    print(file)

print("----------------method 9:pathlib to list files in a directory---------------")
dir_path = r'C:\Users\Kelvin Walker\Desktop\backup'
res = []#to store filenames
d = pathlib.Path(dir_path)
for entry in d.iterdir():
    res.append(entry)
print(res)

