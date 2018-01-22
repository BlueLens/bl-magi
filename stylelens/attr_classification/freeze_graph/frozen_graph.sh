#! /bin/bash

source activate bl-magi
export PYTHONPATH='pwd'/../../tensorflow:'pwd'/../../tensorflow/slim
echo $PYTHONPATH
export MODEL_BASE_PATH='/home/lion/attr_dataset/color_model'

python freeze_graph.py \
    --input_graph=inception_v3_inf_graph.pb \
    --input_checkpoint=/home/lion/attr_dataset/color_model/model/train2/model.ckpt-54229 \
    --input_binary=True \
    --output_graph=color_inference_graph.pb \
    --output_node_names=InceptionV3/Predictions/Reshape_1
