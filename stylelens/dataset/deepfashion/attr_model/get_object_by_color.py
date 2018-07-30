from __future__ import print_function
from stylelens_dataset.colors import Colors 
from pprint import pprint
import os
import string
import time
import tensorflow as tf
import urllib.request as urllib
# import redis
# from bluelens_log import Logging

api_instance = Colors()

flags = tf.app.flags
flags.DEFINE_string('color_dataset_path', '', 'Path to color_dataset_path')
FLAGS = flags.FLAGS

'''
REDIS_SERVER = os.environ['REDIS_SERVER']
REDIS_PASSWORD = os.environ['REDIS_PASSWORD']
options = {
  'REDIS_SERVER': REDIS_SERVER,
  'REDIS_PASSWORD': REDIS_PASSWORD
}
log = Logging(options, tag='generate-color-classifier-dataset')
rconn = redis.StrictRedis(REDIS_SERVER, decode_responses=True, port=6379, password=REDIS_PASSWORD)
'''

def get_colors(classes):
  color_dataset_path = FLAGS.color_dataset_path
    
  try:
    for clazz in classes:
      color_name = clazz

      
      os.chdir(color_dataset_path)
      try:
        os.mkdir(color_name)
      except FileExistsError:
        pass
      os.chdir(color_name) 

      pprint('get_colors API... color : ' + color_name)
      
      offset = 0
      limit = 100
      i = 0
      while True:
        
        colors = api_instance.get_colors_by_name(color_name, offset=offset,
                limit=limit)

        for color in colors:
          _id = str(color['_id'])
          download_image_from_url(color['main_image'], _id + '.jpg')
        # pprint(color_object_list)

        if limit > len(colors):
          break
        else:
          offset += limit
        i += 1
        pprint('get_colors API... color : ' + color_name + ' / ' + str(i))

    pprint('get_colors API... color : ' + color_name + ' ALL Done !')

  except Exception as e:
    print("Exception when calling get_colors_by_name: %s\n" % e)

def get_color_classes():
  try:
    classes = api_instance.get_classes()
    return classes
  except Exception as e:
    print("Exception when calling get_color_classes: %s\n" % e)
    return None

def download_image_from_url(url, filename):
  try:
    urllib.urlretrieve(url, filename)
  except urllib.HTTPError:
    pass


def main(_):
  # log.info('Start generate-color-classifier-dataset')
  #classes = get_color_classes()
  color_list = ['Black', 'Gray', 'Purple', 'Blue', 'Brown','Green', 'Orange', 'Red', 'Pink', 'Yellow','White', 'Navy', 'Beige'] 
  classes = color_list
  #if classes:
  get_colors(classes)

if __name__ == '__main__':
  tf.app.run()
