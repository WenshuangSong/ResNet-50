
# Create the imagenet lmdb inputs
# N.B. set the path to the imagenet train + val data dirs
#lmdbdatapath=/data1/swf/data/lmdb
# lmdbdatapath=/home/user/swscode/build_lmdb
#TOOLS=/home/swf/work/caffe/build/tools/
TOOLS=/home/user/swfcode/caffe/build/tools/
EXAMPLE=/home/user/swscode/build_lmdb/
DATA=/home/user/swscode/datatest/
# DATA= /data2/swftrainingmodel/data/$1/


# TRAIN_DATA_ROOT=/home/user/swscode/datatest/train/
# VAL_DATA_ROOT=/home/user/swscode/datatest/val/
TRAIN_DATA_ROOT="/"
VAL_DATA_ROOT="/"
# TRAIN_DATA_ROOT=/data2/swftrainingmodel/data/$1/train
# VAL_DATA_ROOT=/data2/swftrainingmodel/data/$1/val

# Set RESIZE=true to resize the images to 256x256. Leave as false if images have
# already been resized using another tool.
RESIZE=true
if $RESIZE; then
  RESIZE_HEIGHT=256
  RESIZE_WIDTH=256
else
  RESIZE_HEIGHT=0
  RESIZE_WIDTH=0
fi

# if [ ! -d "$TRAIN_DATA_ROOT" ]; then
  # echo "Error: TRAIN_DATA_ROOT is not a path to a directory: $TRAIN_DATA_ROOT"
  # echo "Set the TRAIN_DATA_ROOT variable in create_imagenet.sh to the path" \
       # "where the ImageNet training data is stored."
  # exit 1
# fi

# if [ ! -d "$VAL_DATA_ROOT" ]; then
  # echo "Error: VAL_DATA_ROOT is not a path to a directory: $VAL_DATA_ROOT"
  # echo "Set the VAL_DATA_ROOT variable in create_imagenet.sh to the path" \
       # "where the ImageNet validation data is stored."
  # exit 1
# fi

echo "Creating train lmdb..."

    # --backend="leveldb"\
GLOG_logtostderr=1 $TOOLS/convert_imageset \
    --resize_height=$RESIZE_HEIGHT \
    --resize_width=$RESIZE_WIDTH \
    --shuffle \
    $TRAIN_DATA_ROOT \
    ./train.txt \
    $EXAMPLE/"patch"${1}"_train_lmdb"

echo "Creating val lmdb..."

    # --backend="leveldb"\
GLOG_logtostderr=1 $TOOLS/convert_imageset \
    --resize_height=$RESIZE_HEIGHT \
    --resize_width=$RESIZE_WIDTH \
    --shuffle \
    $VAL_DATA_ROOT \
    ./val.txt \
    $EXAMPLE/"patch"${1}"_val_lmdb"

echo "Done."
