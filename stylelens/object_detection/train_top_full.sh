#! /bin/bash

source activate bl-magi
export PYTHONPATH=$PYTHONPATH:`pwd`/../../tensorflow:`pwd`/../../tensorflow/slim:'pwd'/../../tensorflow/object_detection
export MODEL_BASE_PATH='/home/lion/dataset/object_3class/top_full_model'

python ./train.py \
    --logtostderr \
    --num_clones 7 \
    --pipeline_config_path=$MODEL_BASE_PATH/models/model/ssd_inception_v2_3class.config \
    --train_dir=$MODEL_BASE_PATH/models/model/train
