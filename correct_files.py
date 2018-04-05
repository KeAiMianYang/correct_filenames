#! /usr/bin/env python3

import os
import sys


maptranslate={
    ord('@'): 'at',
    ord('È'): 'E',
    ord(','): '.',
    ord('#'): '_',
}

mapreplace={
    '..': ' ',
}

def correct_files (fullname, filename="."): # fullname is the absolute path
    print("IN: "+fullname)
    if os.path.isfile(fullname):
        return
    
    for fn in os.listdir(fullname): # listdir give the simple name of each file
        new_fn_ext = os.path.splitext(fn)
        newFilename = new_fn_ext[0].strip()+new_fn_ext[1] # strip outer spaces
        newFilename = newFilename.translate(maptranslate) # correct chars
        for old, new in mapreplace.items():
            newFilename = newFilename.replace(old, new)

        newFullname = fullname+os.path.sep+newFilename
        #print("new filename :"+newFilename+", new fullname="+newFullname)
        os.rename(fullname+os.path.sep+fn, newFullname)

        correct_files(fullname=newFullname, filename=newFilename)



if __name__ == '__main__':
#    fullname = os.path.abspath(".")
#    arg = "."
    if len(sys.argv) >= 2:
        arg = sys.argv[1].strip()
    else:
        print("needs to give the folder to correct in argument")
        exit()
        
    filename = arg.split("\\")[-1]
    fullname = "/".join(arg.split("\\"))
    print("filename: "+filename)
    print("fullname: "+fullname)
    answer = input("Do you want to renames the files inside the folder?\n(enter \"n\" if you want to cancel)\n")
    
    if answer != "n":
        correct_files(filename=filename, fullname=fullname)
