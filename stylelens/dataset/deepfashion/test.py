import os
import shutil

fabric_dataset_path = "/home/lion/attr_dataset/fabric_dataset/"
train_path = "/home/lion/attr_dataset/fabric_dataset/TRAIN_DIR"
eval_path = "/home/lion/attr_dataset/fabric_dataset/VALIDATION_DIR"
f = open("list_attr_cloth_fabric.txt", "r")

while True:
  line = f.readline()
  if not line: 
    break
  attr = line.split()
  a = ""
  for i in range(len(attr)-1):
    if len(attr) > 2 and i != 0:
      a += '_'
    a += attr[i]

  attr_path = os.path.join(fabric_dataset_path, a)
  try :
    flies = os.listdir(attr_path)
    file_count = len(flies)
    train_num = int(0.8 * file_count)
    test_num = file_count - train_num
    file_list = []
    for (dirpath, dirnames, filenames) in os.walk(attr_path):
      file_list.extend(filenames)
    t_path = os.path.join(train_path, a)
    e_path = os.path.join(eval_path, a)
    os.chdir(train_path)
    os.mkdir(a)
    os.chdir(eval_path)
    os.mkdir(a)

    for i in range(file_count):
      file_path = os.path.join(attr_path,file_list[i])
      if i < train_num:
        shutil.copy2(file_path, t_path)
      else:
        shutil.copy2(file_path, e_path)
    #print(attr[0],file_count)
  except OSError:
    pass
  
  #print(train_num, test_num)
f.close()

