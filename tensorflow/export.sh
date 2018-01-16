#! /bin/bash

source activate bl-magi
#export PYTHONPATH=$PYTHONPATH:`pwd`/../../tensorflow:`pwd`/../../slim
export PYTHONPATH=$PYTHONPATH:./slim:'pwd'/object_detection
#export MODEL_BASE_PATH='gs://bluelens-style-model/object_detection'
echo $PYTHONPATH
export MODEL_BASE_PATH='/home/lion/dataset/deepfashion3'
export TRAIN_PATH=$MODEL_BASE_PATH/models/model/train/model.ckpt-$1

python object_detection/export_inference_graph.py \
    --input_type image_tensor \
    --pipeline_config_path $MODEL_BASE_PATH/models/model/ssd_inception_v2_3class.config \
    --trained_checkpoint_prefix ${TRAIN_PATH} \
    --output_directory output_inference_graph_$1.pb
