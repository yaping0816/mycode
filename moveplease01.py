#!/usr/bin/env python3

import shutil
import os


def main():
   #move to this dir 
    os.chdir('/home/student/mycode/')
   #move file raynor to ceph dir
    shutil.move('raynor.obj', 'ceph_storage/')

    xname = input('What is the new name for kerrigan.obj? ')
    #mvoe file kerrigan to ceph dir and rename it to the user input
    shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/'+xname)


main()
