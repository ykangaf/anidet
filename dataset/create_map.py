'''
Should only be used for making the annotation map
for the first time.
If some annotations are added, use update_map.py
to avoid mixing train/val/test


train : val : test = 5:1:1
'''

import sys
import os
import random

xml_dir = "Annotations"

p = "/projects/anidet/dataset"


train = open(os.path.join(p, "map_train.txt"), "w+")
val = open(os.path.join(p, "map_val.txt"), "w+")
test = open(os.path.join(p, "map_test.txt"), "w+")

l = os.listdir(os.path.join(p, xml_dir))


random.shuffle(l)

# print(l)
seq = 1
for item in l:
    if item.endswith(".xml"):
        # print(item[:-4])

        seq+=1
        if seq % 7==0:
            val.write("{} -1\n".format(item[:-4]))
        elif seq % 7==1:
            test.write("{} -1\n".format(item[:-4]))

        else:
            train.write("{} -1\n".format(item[:-4]))


train.close()
val.close()
test.close()