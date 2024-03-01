#!/usr/bin/env python
import os
from os import walk
def get_files(path):
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path,file)):
            yield file

for file in get_files(r"C:\Users\Kelvin Walker\Desktop\backup"):
    print(file)

print('The current working directory is: {0}'.format(os.getcwd()))
#change directory
os.chdir('C:/Users/Kelvin Walker/Desktop/backup')
print('The current working directory now is: {0}'.format(os.getcwd()))
try:
    res = []
    cur_dir = os.getcwd()
    for(dir_path,dir_names,file_names) in walk(cur_dir):
        res.extend(dir_names)
        print(res)
       #os.rmdir('newdir')

        if 'newdir' in res:
            os.chdir("newdir")
            print(os.getcwd())
            
            files = []
            for file_path in os.listdir("."):
                if os.path.isfile(os.path.join(".",file_path)):
                    files.append(file_path)

            for file in files:
                print(file)
                if 'hot.txt' in files:
                    print("file already exists")
                    my_file = open("hot.txt","r+")
                    print("output of the file contents are:")
                    print(my_file.readline())
                    print(my_file.read())
                    print(my_file.read(10))
                    my_file.close()
                else:
                    print("file absent")
                    with open("hot.txt","x") as file:
                        l = ['Hello there this is kevin walker\n','currently doing some scripting in python language\n','It is fun\n']
                        file.write("wow that lady looks hot who is she\n")
                        file.writelines(l)
                        file.flush()
                        file.close()

        else:
            os.mkdir("newdir")
except OSError as error:
    print(error)


