#!/usr/bin/python

import os

os.chdir(os.getcwd() + "/allFiles")
curdir = os.getcwd()

for f in os.listdir(curdir):
    info = []
    info.append("minimum,average")
    with open(f, "r") as ins:
        array = []
        for line in ins:
            arr = " ".join(line.split())
            arr2 = arr.split(" ")
            if(arr2[0] == "Totals:"):
                info.append(arr2[1] + "," + arr2[2])

    namearr = f.split("A")

    with open(namearr[0] + "Info.csv", "w") as ins:
        for s in info:
            ins.write("%s\n" % s)

