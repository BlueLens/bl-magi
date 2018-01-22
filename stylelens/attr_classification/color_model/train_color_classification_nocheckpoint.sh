#! /bin/bash
source activate bl-magi
export PYTHONPATH=$PYTHONPATH:`pwd`/../../../tensorflow:`pwd`/../../../tensorflow/slim:
export TRAIN_DIR_PATH='/home/lion/attr_dataset/color_model/model/train2'
export DATASET_DIR_PATH='/home/lion/attr_dataset/color_model/data/dataset1'


python /home/lion/bl-magi/tensorflow/slim/train_image_classifier.py \
    --train_dir=$TRAIN_DIR_PATH \
    --dataset_dir=$DATASET_DIR_PATH \
    --dataset_name=color \
    --dataset_split_name=train \
    --num_clones=2 \
    --batch_size=30 \
    --learning_rate=0.01 \
    --model_name=inception_v3 \
    --max_num_of_steps=1000000  
