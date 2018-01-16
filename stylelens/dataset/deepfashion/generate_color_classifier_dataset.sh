#source activate bl-magi
export PYTHONPATH=$PYTHONPATH:`pwd`/../../tensorflow:`pwd`/../../slim
export DB_DATASET_HOST="35.187.193.199"
export DB_DATASET_NAME="bl-db-dataset"
export DB_DATASET_PORT="27017"
export REDIS_SERVER="bl-mem-store-index-prod.stylelens.io"
export REDIS_PASSWORD="BZ8oHd2pfD4j"
#export DATASET_PATH='gs://bluelens-style-model/object_detection'

echo $PYTHONPATH

python generate_color_classifier_dataset.py \
    --color_dataset_path=/home/lion/attr_dataset/color_model/data/images
