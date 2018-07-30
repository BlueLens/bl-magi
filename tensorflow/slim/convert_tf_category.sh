#source activate bl-magi
export PYTHONPATH=$PYTHONPATH:`pwd`/../../tensorflow:`pwd`/../slim
export DATASET_PATH=/home/lion/attr_dataset/category_model/data/dataset1

echo $PYTHONPATH

python download_and_convert_data.py \
    --dataset_name=category\
    --dataset_dir=$DATASET_PATH
