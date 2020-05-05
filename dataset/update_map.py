'''
Update annotation-image map after creating
new annotations.
Should not mess up with previous mapped images
since test/val data may become training data
'''

import sys
import os
import random

xml_dir = "Annotations"

p = "/projects/anidet/dataset"

train = open(os.path.join(p, "map_train.txt"), "r")
val = open(os.path.join(p, "map_val.txt"), "r")
test = open(os.path.join(p, "map_test.txt"), "r")
train_list = []
val_list = []
test_list = []
train_lines = train.readlines()
val_lines = val.readlines()
test_lines = test.readlines()
for line in train_lines:
    train_list.append(line.split(" ", 1)[0] )
for line in test_lines:
    test_list.append(line.split(" ", 1)[0] )
for line in val_lines:
    val_list.append(line.split(" ", 1)[0] )
# print(len(train_list))

train.close()
val.close()
test.close()

print(f"Before\ntrain:{len(train_list)} val:{len(val_list)} test:{len(test_list)} total:{len(train_list) + len(test_list) + len(val_list)}")





train = open(os.path.join(p, "map_train.txt"), "a+")
val = open(os.path.join(p, "map_val.txt"), "a+")
test = open(os.path.join(p, "map_test.txt"), "a+")

l = os.listdir(os.path.join(p, xml_dir))
random.shuffle(l)

print(f"old+new:\n{len(l)}")
seq = 1
for item in l:
    if item.endswith(".xml"):
        # print(item[:-4])
        if item[:-4] not in train_list and item[:-4] not in val_list and item[:-4] not in test_list:

            # print(item)
            seq+=1
            if seq % 7==0:
                val.write("{} -1\n".format(item[:-4]))
            elif seq % 7==1:
                test.write("{} -1\n".format(item[:-4]))

            else:
                train.write("{} -1\n".format(item[:-4]))
print(f"added {seq-1}")

train.close()
val.close()
test.close()