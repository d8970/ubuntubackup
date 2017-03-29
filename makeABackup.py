#!/usr/bin/python
from os import listdir
from os import walk
from os.path import isfile, join
from subprocess import call

def showDir(dirname):
     f=[]
     for (dirpath, dirnames, filenames) in walk(dirname):
        print dirname,'has following'
        print 'Directories',dirnames
        print 'Files',filenames
        f.extend(filenames)
        for item in dirnames:
           dirpath=dirname+'/'+item
           print dirpath
           showDir(dirpath)

#list through all the files and folders in the directory
with open('lookin.txt', 'r') as f:
   dest=f.readline()
   dest=dest.strip('\n')
   dest=dest.strip('\t')
   print 'Destination', dest
   for src in f:
      src=src.strip('\n')
      src=src.strip('\t')
      print 'Source', src
      cmd='cp -iruf %s %s' % (src, dest)
      print cmd
      call(['cp','--verbose', '-iruf', src, dest])
   #showDir(src)
