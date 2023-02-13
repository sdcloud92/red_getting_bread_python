#!/usr/bin/env python3.7

#import os module
import os

#set variable to get cwd
directory = os.getcwd()

#create empty list
files_list = []

for file_name in os.listdir(directory):
    
    for file_size in range(os.path.getsize(directory)):
        
        files_attr = {
    "name": file_name,
    "size": os.path.getsize(file_name)
}

    files_list.append(files_attr)

    print(files_attr)
    
    