from stylelens_dataset.categories import Categories

TEXT_DATASET_FILE = './list_category_apparel.txt'

category_api = Categories()

def add_category(name, class_code):

  category = {}
  category['name'] = name
  category['class_code'] = class_code

  try:
    res = category_api.add_category(category)
  except Exception as e:
    print("Exception when calling add_category: %s\n" % e)

if __name__ == '__main__':
  try:
    category_dataset = open(TEXT_DATASET_FILE, 'r')
    categories = []
    for pair in category_dataset.readlines():
      map = pair.strip().split()
      name = str(map[0])
      class_code = str(map[1])

      add_category(name, class_code)
  except Exception as e:
    print(e)
