#! /bin/bash
source activate bl-magi
export PYTHONPATH=$PYTHONPATH:`pwd`/../../../tensorflow:`pwd`/../../../tensorflow/slim:
export TRAIN_DIR_PATH='/home/lion/attr_dataset/category_model/model/train1'
export DATASET_DIR_PATH='/home/lion/attr_dataset/category_model/data/dataset1'


python /home/lion/bl-magi/tensorflow/slim/train_image_classifier.py \
    --train_dir=$TRAIN_DIR_PATH \
    --dataset_dir=$DATASET_DIR_PATH \
    --dataset_name=category \
    --dataset_split_name=train \
    --num_clones=7 \
    --batch_size=42\
    --model_name=inception_v3 
