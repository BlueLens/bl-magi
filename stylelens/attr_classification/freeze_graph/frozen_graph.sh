#! /bin/bash

source activate bl-magi
export PYTHONPATH='pwd'/../../tensorflow:'pwd'/../../tensorflow/slim
echo $PYTHONPATH
export MODEL_BASE_PATH='/home/lion/attr_dataset/category_model'

python freeze_graph.py \
    --input_graph=category_inception_v3_inf_graph.pb \
    --input_checkpoint=/home/lion/attr_dataset/category_model/model/train1/model.ckpt-786881 \
    --input_binary=True \
    --output_graph=category_inference_graph.pb \
    --output_node_names=InceptionV3/Predictions/Reshape_1
