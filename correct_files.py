#! /usr/bin/env python3

import os
import sys


mapreplace={
    ord('@'): 'at',
    ord('È'): 'E',
    ord(','): '.'
}

def correct_files (fullname, filename="."): # pathname is the absolute path
    print("IN CORRECT_FILES: filename="+filename+", fullname="+fullname)
    if os.path.isfile(fullname):
        print ("is file")
        return
    
    for fn in os.listdir(fullname): # listdir give the simple name of each file
        newFilename = fn.strip()
        newFilename = newFilename.translate(mapreplace)

        newFullname = fullname+os.path.sep+newFilename
        print("new filename :"+newFilename+", new fullname="+newFullname)
        os.rename(fullname+os.path.sep+fn, newFullname)

        correct_files(fullname=newFullname, filename=newFilename)



if __name__ == '__main__':
    fullname = os.path.abspath(".")
    arg = "."
    if len(sys.argv) >= 2:
        arg = sys.argv[1]
        fullname = os.path.abspath(arg)

    
    correct_files(filename=arg, fullname=fullname)