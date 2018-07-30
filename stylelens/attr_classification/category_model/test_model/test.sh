#! /bin/bash
source activate bl-magi
export PYTHONPATH=$PYTHONPATH:`pwd`/../../../tensorflow:`pwd`/../../../tensorflow/slim:
export MODEL_PATH='/home/lion/attr_dataset/category_model/model/train1/model.ckpt-769143'
export LABEL_PATH='/home/lion/attr_dataset/category_model/data/dataset/labels.txt'
export DATA_PATH='/home/lion/bl-magi/stylelens/attr_classification/category_model/test_images1/'

python test_category.py \
    --model_path=$MODEL_PATH \
    --model_name=inception_v3 \
    --label_path=$LABEL_PATH \
    --data_path=$DATA_PATH







