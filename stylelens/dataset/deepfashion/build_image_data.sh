#source activate bl-magi
export PYTHONPATH=$PYTHONPATH:`pwd`/../../tensorflow:`pwd`/../../slim
# export DB_DATASET_HOST="35.187.193.199"
# export DB_DATASET_NAME="bl-db-dataset"
# export DB_DATASET_PORT="27017"
# export DATASET_PATH='gs://bluelens-style-model/object_detection'

echo $PYTHONPATH

python build_image_data.py \
    --train_directory=/home/lion/attr_dataset/fabric_dataset/TRAIN_DIR\
    --validation_directory=/home/lion/attr_dataset/fabric_dataset/VALIDATION_DIR\
    --output_directory=/home/lion/attr_dataset/fabric_model/data\
    --labels_file=/home/lion/attr_dataset/fabric_model/data/fabric_label.txt
