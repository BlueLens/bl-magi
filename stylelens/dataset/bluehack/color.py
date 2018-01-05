import os
import uuid
import urllib.request
import argparse
from PIL import Image
from util import s3

from stylelens_dataset.colors import Colors

AWS_DATASET_BUCKET = 'stylelens-dataset'
AWS_DIR = 'bluehack/color'

IMG_WIDTH = 300
IMG_HEIGHT = 300

COLOR_DATA = [
    ('red', 'CCO2OO'),
    ('orange', 'FB930B'),
    ('yellow', 'FEFF00'),
    ('green', '00CC00'),
    ('mint', '00C1C6'),
    ('blue', '1700FF'),
    ('purple', '752CA7'),
    ('pink', 'FF98BF'),
    ('white', '000000'),
    ('gray', '999999'),
    ('black', 'FFFFFF'),
    ('brown', '885319')
]

parser = argparse.ArgumentParser(description='ArgParser')
parser.add_argument('--jsondir', type=str, default=os.path.join(os.path.expanduser('~'), 'Downloads/google/'),
                    help='The directory location stored crawled data from google search')

AWS_ACCESS_KEY = os.environ['AWS_ACCESS_KEY'].replace('"', '')
AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY'].replace('"', '')

storage = s3.S3(AWS_ACCESS_KEY, AWS_SECRET_ACCESS_KEY)


class GoogleSaver:
    def __init__(self, directory):
        self.directory = directory
        os.mkdir(os.path.join(directory, 'temp'))

    def __save_image_to_storage(self, crawled_item):
        downloaded_file_name = self.__download_image(crawled_item['url'])
        key = os.path.join(AWS_DIR, crawled_item['color_name'], downloaded_file_name + '.jpg')
        is_public = True
        file_url = storage.upload_file_to_bucket(AWS_DATASET_BUCKET, downloaded_file_name, key, is_public=is_public)
        return file_url

    def __crawl_from_google_images(self):
        crawled_data = []
        for color_item in COLOR_DATA:
            color_folder = os.path.join(os.path.join(self.directory, 'color'), color_item[0])
            if os.path.exists(color_folder):
                for file in os.listdir(color_folder):
                    with open(os.path.join(color_folder, file)) as f:
                        for line in f.readlines():
                            color_file_item = {
                                'url': line.strip(),
                                'color_name': color_item[0],
                                'color_code': color_item[1]
                            }
                            crawled_data.append(color_file_item)
        return crawled_data

    def __download_image(self, url):
        try:
            # f = urllib.urlopen(urllib.quote(image_path.encode('utf8'), '/:'))
            f = urllib.request.urlopen(url)
            im = Image.open(f).convert('RGB')
            im = im.resize((IMG_WIDTH, IMG_HEIGHT), Image.ANTIALIAS)
            download_file_name = os.path.join(os.path.join(self.directory, 'temp'), str(uuid.uuid4()) + '.jpg')
            im.save(download_file_name)
        except Exception as e:
            print(e)

        return download_file_name

    def execute(self):
        api_instance = Colors()

        for crawled_item in self.__crawl_from_google_images():
            file_url = self.__save_image_to_storage(crawled_item)

            color = {
                'file': file_url,
                'name': crawled_item['color_name'],
                'code': crawled_item['color_code']
            }

            api_instance.add_color(color)


if __name__ == '__main__':
    args = parser.parse_args()
    try:
        gs = GoogleSaver(directory=args.jsondir)
        gs.execute()
    except Exception as e:
        print("Exception when calling add_color: %s\n" % e)
