#! /bin/bash
source activate bl-magi
export PYTHONPATH=$PYTHONPATH:`pwd`/../../../tensorflow:`pwd`/../../../tensorflow/slim:
export MODEL_PATH='/home/lion/attr_dataset/color_model/model/train2/model.ckpt-54229'
export LABEL_PATH='/home/lion/attr_dataset/color_model/data/dataset1/labels.txt'
export DATA_PATH='/home/lion/bl-magi/stylelens/attr_classification/color_model/test/'

python test_color.py \
    --model_path=$MODEL_PATH \
    --model_name=inception_v3 \
    --label_path=$LABEL_PATH \
    --data_path=$DATA_PATH







