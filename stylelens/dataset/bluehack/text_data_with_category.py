from stylelens_dataset.texts import Texts

TEXT_DATASET_FILE = './text_data_with_category.txt'

text_api = Texts()

def add_text(text_code, keyword):
  text = {}
  text['text_code'] = text_code
  text['text'] = keyword

  try:
    print('')
    res = text_api.add_text(text)
  except Exception as e:
    print(e)

if __name__ == '__main__':
  try:
    text_dataset = open(TEXT_DATASET_FILE, 'r')
    texts = []
    for pair in text_dataset.readlines():
      map = pair.strip().split(':')
      tmp = map[1].strip().split(',')
      keywords = list(set(tmp))
      text_code = str(map[0])
      for keyword in keywords:
        print('' + text_code + ":" + keyword)
        add_text(text_code, keyword)
  except Exception as e:
    print(e)
