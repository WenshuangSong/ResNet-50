# -*- coding: utf-8 -*-
import shutil
import csv
s =0
diriq = {}
# with open('text.csv', 'r') as f:
Filenamelist =[]
labellist=[]
import csv
with open('text.csv') as csvfile:
     readCSV = csv.reader(csvfile, delimiter=',')
     for row in readCSV:
         print row
         print row[0].split()
         Filenamelist.append(row[0].split()[0])
         labellist.append(row[0].split()[1])
         # print row[1]
    # a1 = [row for row in DictReader(f)]
    # print "--->", type(a1)
    # print len(a1)
    # a2 = [row["2"] for row in DictReader(f)]
for a  in labellist :
    if a in diriq:
        diriq[a]+=1
    else:
        diriq[a]=1
count ={}
for file, idname in zip(Filenamelist,labellist):
    if count.has_key(idname):
        if count[idname] < diriq[idname]*0.8:
            print file
            count[idname]+=1
            shutil.copy(file,'/home/user/swscode/datatest/train/')
        else:
            shutil.copy(file,'/home/user/swscode/datatest/val/')
    else:
        count[idname]=1
        shutil.copy(file,'/home/user/swscode/datatest/train/')
