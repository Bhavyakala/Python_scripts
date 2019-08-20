# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 23:01:11 2019

@author: Bhavya Kala
"""

import os
root_dir = input("Path of root directory: ")
max_size = 0
for root,dirs,files in os.walk(root_dir):
    for f in files:
        path = os.path.join(root,f)
        temp = os.stat(path).st_size
        if max_size<=temp:
            max_size=temp
            max_size_file=path
print("File with maximum size in root directory is : {}, file size : {} Bytes"
      .format(root_dir,max_size_file,max_size))