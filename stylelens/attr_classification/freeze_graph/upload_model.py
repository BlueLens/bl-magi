import os
from stylelens_s3.s3 import S3

AWS_ACCESS_KEY = os.environ['AWS_ACCESS_KEY']
AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']
RELEASE_MODE = os.environ['RELEASE_MODE']
FROZEN_GRAPH_PATH = '/home/lion/bl-magi/stylelens/object_detection/frozen_graph/top_full_output_inference_graph_100893.pb'
LABLE_MAP_PATH = '/home/lion/attr_dataset/color_model/data/dataset1/labels.txt'

AWS_BUCKET = 'bluelens-style-model'
AWS_BUCKET_FOLDER = 'classification'
MODEL_FILE = 'frozen_inference_graph.pb'

storage = S3(AWS_ACCESS_KEY, AWS_SECRET_ACCESS_KEY)

key = os.path.join(AWS_BUCKET_FOLDER, 'prod', 'top_full', 'top_full_model.ckpt-100893', MODEL_FILE)
label_key = os.path.join(AWS_BUCKET_FOLDER, 'color', 'dev', 'labels.txt')

try:
  storage.upload_file_to_bucket(AWS_BUCKET, FROZEN_GRAPH_PATH, key)
  storage.upload_file_to_bucket(AWS_BUCKET, LABLE_MAP_PATH, label_key)
except:
  print('upload error')
