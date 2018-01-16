#! /bin/bash
source activate bl-magi
export PYTHONPATH=$PYTHONPATH:`pwd`/../../../tensorflow:`pwd`/../../../tensorflow/slim:
export TRAIN_DIR_PATH='/home/lion/attr_dataset/color_model/model/train'
export EVAL_DIR_PATH='/home/lion/attr_dataset/color_model/model/eval'
export DATASET_DIR_PATH='/home/lion/attr_dataset/color_model/data/dataset'

python /home/lion/bl-magi/tensorflow/slim/eval_image_classifier.py \
    --alsologtostderr\
    --eval_dir=$EVAL_DIR_PATH\
    --checkpoint_path=$TRAIN_DIR_PATH\
    --dataset_dir=$DATASET_DIR_PATH\
    --dataset_name=color\
    --dataset_split_name=validation\
    --model_name=inception_v3
