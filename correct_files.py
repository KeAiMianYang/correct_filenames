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

def correct_files (fullname, filename="."): # pathname is the absolute path
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
    fullname = os.path.abspath(".")
    arg = "."
#    if len(sys.argv) >= 2:
#        arg = sys.argv[1]
#        fullname = os.path.abspath(arg)

    
    correct_files(filename=arg, fullname=fullname)
