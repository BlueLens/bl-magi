#source activate bl-magi
export PYTHONPATH=$PYTHONPATH:`pwd`/../../../tensorflow:`pwd`/../../../tensorflow/slim
export AWS_SECRET_ACCESS_KEY="7NFxpVlVQjABUXv3j3BCvayc6sgRwwXzHMl+iSJ8"
export AWS_ACCESS_KEY="AKIAIWSVDY3WRWCMFRJQ"
export RELEASE_MODE="prod"

echo $PYTHONPATH

python upload_model.py \
