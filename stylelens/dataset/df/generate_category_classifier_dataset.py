from __future__ import print_function
from stylelens_dataset.categories import Categories
from stylelens_dataset.objects import Objects
from pprint import pprint
import os
import urllib.request as urllib

# create an instance of the API class
category_api = Categories()
object_api = Objects()

def download_image_from_url(url, filename):
    try:
        urllib.urlretrieve(url, filename)
    except urllib.HTTPError:
        pass

def get_objects_with_category_name(category_name):
    try:
        offset = 0
        limit = 100
        i = 0

        while True:
            res = object_api.get_objects_by_category_name(category_name, offset=offset, limit=limit)
            for object in res:
                download_image_from_url(object['url'], str(object['_id']) + '.jpg')
                i += 1

            if limit > len(res):
                break
            else:
                offset = offset + limit

        pprint(category_name + ' : ' + str(i))

    except Exception as e:
        print("Exception when calling get_objects_by_category_name: %s\n" % e)

def get_category_classes():
    try:
        offset = 0
        limit = 10

        categories = []
        while True:
            res = category_api.get_categories(offset=offset, limit=limit)
            if limit > len(res):
                break
            else:
                offset = offset + limit

            for cate in res:
                categories.append(cate)
        return categories

    except Exception as e:
        print("Exception when calling add_category: %s\n" % e)
        return None


def make_category_dataset():
    dataset_path = '/Users/daesubkim/Desktop/Python/py-example'

    categories = get_category_classes()
    if categories:
        for category in categories:
            category_name = category["name"]
            os.chdir(dataset_path)
            try:
                os.mkdir(category_name)
            except FileExistsError:
                pass
            os.chdir(category_name)
            get_objects_with_category_name(category_name)

def start():
  try:
    make_category_dataset()
  except Exception as e:
    pprint(e)
    # log.error(str(e))

if __name__ == '__main__':
  try:
    start()
  except Exception as e:
    pprint(e)
