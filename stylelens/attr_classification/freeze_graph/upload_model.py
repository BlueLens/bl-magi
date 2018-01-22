import os
from stylelens_s3.s3 import S3

AWS_ACCESS_KEY = os.environ['AWS_ACCESS_KEY']
AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']
RELEASE_MODE = os.environ['RELEASE_MODE']

AWS_BUCKET = 'bluelens-style-model'
AWS_BUCKET_FOLDER = 'classification/color'
MODEL_FILE = 'color_classification_model.pb'

storage = S3(AWS_ACCESS_KEY, AWS_SECRET_ACCESS_KEY)

file = os.path.join(os.getcwd(), MODEL_FILE)
key = os.path.join(AWS_BUCKET_FOLDER, RELEASE_MODE, MODEL_FILE)

print(file)
print(key)

try:
  storage.upload_file_to_bucket(AWS_BUCKET, file, key)
except:
  print('upload error')
