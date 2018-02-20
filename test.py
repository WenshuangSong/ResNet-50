#coding=utf-8
import sys
sys.path.insert(0,'/home/user/swfcode/caffe/python')
import os
import caffe
import numpy as np
root='/home/user/swscode/datatest/'
deploy=root +'ResNet-50-deploy.prototxt'
caffe_model='/data1/swfdata/swfmodels/residualnet_imagenet/sws_1211resnet_50_iter_150000.caffemodel'
import os
import numpy as np
mylist=[]
dir = root+'val/'
filelist=[]
filenames = os.listdir(dir)
for fn in filenames:
    fullfilename = os.path.join(dir,fn)
    filelist.append(fullfilename)


net = caffe.Net(deploy,caffe_model,caffe.TEST)
    # img=root+‘data/DRIVE/test/60337.jpg‘
def Test(img, net):



    # transformer = caffe.io.Transformer({'data':net.blobs['data'].data.shape})
    transformer = caffe.io.Transformer({'data': net.blobs['data'].data.shape})
    transformer.set_transpose('data', (2,0,1))
    #transformer.set_mean(‘data‘, np.load(mean_file).mean(1).mean(1))
    transformer.set_raw_scale('data', 255)
    transformer.set_channel_swap('data', (2,1,0))
    im=caffe.io.load_image(img)
    net.blobs['data'].data[...] = transformer.preprocess('data',im)


    out = net.forward()
    labels = np.loadtxt(labels_filename, str, delimiter='\t')
    prob= net.blobs['prob'].data[0].flatten()
    print prob
    order=prob.argsort()[:3]
    return prob

    # print 'the class is:',labels[order]
   # f=file("/home/user/swfcode/caffe/label.txt","a+")
    #f.write(labels[order]+'\n')
labels_filename = root +'result.txt'
for i in range(0, len(filelist)):
    img= filelist[i]
    prob=Test(img ,net)
    np.argmax(prob)
    mylist.append(np.argmax(prob))

file=open('result.txt','w')
file.write(str(mylist))
file.close()


