from __future__ import print_function
from stylelens_dataset.objects import Objects
from pprint import pprint
import os
import time
import tensorflow as tf
import urllib.request as urllib

ATTR_CLOTH_FILE = './list_attr_cloth_fabric.txt'

api_instance = Objects()

flags = tf.app.flags
flags.DEFINE_string('fabric_dataset_path', '', 'Path to fabric_dataset_path')
FLAGS = flags.FLAGS

def get_attribute_clothes():
  attr_cloth = open(ATTR_CLOTH_FILE, 'r')
  attribute_clothes = []
  for pair in attr_cloth.readlines():
    map = pair.strip().rsplit(' ', 1)
    attr = {}
    attr['name'] = map[0].strip()
    attr['type'] = map[1]
    attribute_clothes.append(attr)
  return attribute_clothes


def download_image_from_url(url, filename):
  try:
    urllib.urlretrieve(url, filename)
  except urllib.HTTPError:
    pass


def main(_):
  fabric_dataset_path = FLAGS.fabric_dataset_path
  # time.sleep(7200)
  try:

    attrs = get_attribute_clothes()
    for attr in attrs:
      print(attr['name'])
      offset = 0
      limit = 100

      os.chdir(fabric_dataset_path)
      try:
        os.mkdir(attr['name'])
      except FileExistsError:
        pass
      os.chdir(attr['name'])
      

      while True:
        res = api_instance.get_objects_by_fabric(attr['name'], offset=offset, limit=limit)
        # save image by fabric attr
        for idx in range(len(res)):
          url =  res[idx]['url']
          _id = str(res[idx]['_id'])
          filename = _id + '.jpg'
          download_image_from_url(url, str(filename))
        if limit > len(res):
          break
        else:
          offset = offset + limit

  except Exception as e:
    print("Exception when calling get_images_by_source: %s\n" % e)

if __name__ == '__main__':
  tf.app.run()
