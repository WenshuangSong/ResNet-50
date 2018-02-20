# -*- coding: utf-8 -*-
import csv
import os
import numpy as np
def IsSubString(SubStrList,Str):
    '''''
    #判断字符串Str是否包含序列SubStrList中的每一个子字符串
    #>>>SubStrList=['F','EMS','txt']
    #>>>Str='F06925EMS91.txt'
    #>>>IsSubString(SubStrList,Str)#return True (or False)
    '''
    flag=True
    for substr in SubStrList:
        if not(substr in Str):
            flag=False
    return flag
#~ #----------------------------------------------------------------------
def GetFileList(FindPath,FlagStr=[]):
    FileList=[]
    FileNames=os.listdir(FindPath)
    if (len(FileNames)>0):
        for fn in FileNames:
            if (len(FlagStr)>0):
                #返回指定类型的文件名
                if (IsSubString(FlagStr,fn)):
                    fullfilename=os.path.join(FindPath,fn)
                    FileList.append(fullfilename)
            else:
                #默认直接返回所有文件名
                fullfilename=os.path.join(FindPath,fn)
                FileList.append(fullfilename)
        #对文件名排序
    if (len(FileList)>0):
         FileList.sort()
    return FileList
if __name__=="__main__":
    FileNameList=GetFileList("/home/user/swscode/datatest/train/",[])
    print FileNameList
# fileObject = open('val.txt', 'w')
data = np.array([FileNameList, ])
labellist = []
for ip in FileNameList:
    print ip
    # fileObject.write(ip)
    # fileObject.write('\n')
    iq=ip.split('/')[-1].split("_")[0]
    iq = int(iq)
    iq = iq-2
    iq=str(iq)
    labellist.append(iq)
with open('train.csv', 'w') as f:
    print "test"
    writer = csv.writer(f, delimiter='\t')
    writer.writerows(zip(FileNameList,labellist))
# fileObject.close()

