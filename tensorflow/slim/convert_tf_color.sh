#source activate bl-magi
export PYTHONPATH=$PYTHONPATH:`pwd`/../../tensorflow:`pwd`/../slim
export DATASET_PATH=/home/lion/attr_dataset/color_model/data/dataset

echo $PYTHONPATH

python download_and_convert_data.py \
    --dataset_name=color\
    --dataset_dir=$DATASET_PATH
