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
parser.add_argument('--jsondir', type=str, default=os.path.join(os.path.expanduser('~'), './color_data/'),
                    help='The directory location stored crawled data from google search')

AWS_ACCESS_KEY = os.environ['AWS_ACCESS_KEY'].replace('"', '')
AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY'].replace('"', '')

storage = s3.S3(AWS_ACCESS_KEY, AWS_SECRET_ACCESS_KEY)


class GoogleSaver:
    def __init__(self, directory):
        self.directory = directory

        if not os.path.exists(os.path.join(directory, 'temp')):
            os.mkdir(os.path.join(directory, 'temp'))

    def __save_image_to_storage(self, crawled_item):

        try:
            downloaded_file_name = self.__download_image(crawled_item['url'], crawled_item['product'])
            if downloaded_file_name is not None:
                key = os.path.join(os.path.join(AWS_DIR, crawled_item['color_name']), downloaded_file_name.split(sep='/')[-1])
                file_url = storage.upload_file_to_bucket(AWS_DATASET_BUCKET, downloaded_file_name, key, is_public=True)
                print(file_url)

                return file_url
        except Exception as ex:
            print(ex)

        return None

    def __crawl_from_google_images(self):
        crawled_data = []
        for color_item in COLOR_DATA:
            color_folder = os.path.join(os.path.join(self.directory, 'color'), color_item[0])
            if os.path.exists(color_folder):
                for file in os.listdir(color_folder):
                    if file == '.DS_Store':
                        continue
                    with open(os.path.join(color_folder, file), encoding='UTF-8') as f:
                        for line in f.readlines():
                            color_file_item = {
                                'url': line.strip(),
                                'product': file.split(sep='.')[0].lower(),
                                'color_name': color_item[0],
                                'color_code': color_item[1]
                            }
                            crawled_data.append(color_file_item)
        return crawled_data

    def __download_image(self, url, product):
        try:
            f = urllib.request.urlopen(url, timeout=30)
            with Image.open(f) as im:
                im.convert('RGB')
                if im is None:
                    print('%s is not image file.' % url)
                else:
                    im = im.resize((IMG_WIDTH, IMG_HEIGHT), Image.ANTIALIAS)
                    download_file_name = os.path.join(os.path.join(self.directory, 'temp'),
                                                      '%s_%s.jpg' % (product, str(uuid.uuid4())))
                    im.save(download_file_name)
        except Exception as e:
            print(e)

        return download_file_name

    def execute(self):
        api_instance = Colors()

        for crawled_item in self.__crawl_from_google_images():
            file_url = self.__save_image_to_storage(crawled_item)

            if file_url is None:
                continue

            color = {
                'file': file_url,
                'name': crawled_item['color_name'],
                'code': crawled_item['color_code']
            }

            api_response = api_instance.add_color(color)
            print(color, api_response)

if __name__ == '__main__':
    args = parser.parse_args()
    try:
        gs = GoogleSaver(directory=args.jsondir)
        gs.execute()
    except Exception as e:
        print("Exception when calling add_color: %s\n" % e)
