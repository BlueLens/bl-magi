#! /bin/bash

source activate bl-magi
export PYTHONPATH=$PYTHONPATH:`pwd`/../../tensorflow:`pwd`/../../tensorflow/slim:'pwd'/../../tensorflow/object_detection
export MODEL_BASE_PATH='/home/lion/dataset/object_3class/top_model'

python ./eval.py \
    --logtostderr \
    --pipeline_config_path=$MODEL_BASE_PATH/models/model/ssd_inception_v2_3class.config \
    --checkpoint_dir=$MODEL_BASE_PATH/models/model/train2 \
    --eval_dir=$MODEL_BASE_PATH/models/model/eval2
