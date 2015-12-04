#!/usr/bin/python

import subprocess
import os

files = []
os.chdir("info")
prevdir = os.getcwd()
pybench = "~/Documents/pybench/pybench.py"

for dirs in os.listdir(prevdir):
    os.chdir(os.getcwd() + "/" + dirs)
    prevdir2 = os.getcwd()
    for tests in os.listdir(prevdir2):
        os.chdir(os.getcwd() + "/" + tests)
        prevdir3 = os.getcwd()
        for test in os.listdir(prevdir3):
            os.system(pybench + " -s " + test + " >> " + dirs + tests +  "All.txt")   
        os.chdir("..");
    os.chdir("..");
