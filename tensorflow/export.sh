#! /bin/bash
source activate bl-magi
export PYTHONPATH=$PYTHONPATH:./slim:'pwd'/object_detection
echo $PYTHONPATH
export MODEL_BASE_PATH='/home/lion/dataset/object_3class/top_full_model'
export TRAIN_PATH=$MODEL_BASE_PATH/models/model/train/model.ckpt-$1

python object_detection/export_inference_graph.py \
    --input_type image_tensor \
    --pipeline_config_path $MODEL_BASE_PATH/models/model/ssd_inception_v2_3class.config \
    --trained_checkpoint_prefix ${TRAIN_PATH} \
    --output_directory /home/lion/bl-magi/stylelens/object_detection/frozen_graph/top_full_output_inference_graph_$1.pb
