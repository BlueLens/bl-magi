import os

f = open("list_attr_cloth_fabric.txt", "r")
f1 = open("fabric_label.txt", "a")

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
  f1.write(a + '\n')

  
f.close()
f1.close()
