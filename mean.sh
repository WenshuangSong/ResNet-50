#!/bin/bash
EXAMPLE=/home/user/swscode/build_lmdb/
DATA="./"
TOOLS=/home/user/swfcode/caffe/build/tools   
  
$TOOLS/compute_image_mean $EXAMPLE/train_lmdb \
  imagenet_mean.binaryproto  
    
  echo "Done."  
