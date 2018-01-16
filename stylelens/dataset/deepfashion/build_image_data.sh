#source activate bl-magi
export PYTHONPATH=$PYTHONPATH:`pwd`/../../tensorflow:`pwd`/../../slim

echo $PYTHONPATH

python build_image_data.py \
    --train_directory=/home/lion/attr_dataset/fabric_dataset/TRAIN_DIR\
    --validation_directory=/home/lion/attr_dataset/fabric_dataset/VALIDATION_DIR\
    --output_directory=/home/lion/attr_dataset/fabric_model/data\
    --labels_file=/home/lion/attr_dataset/fabric_model/data/fabric_label.txt
