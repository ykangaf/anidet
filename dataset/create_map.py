import sys
import os

xml_dir = "Annotations"

p = "/projects/anidet/dataset"


train = open(os.path.join(p, "map_train.txt"), "w+")
val = open(os.path.join(p, "map_val.txt"), "w+")

l = os.listdir(os.path.join(p, xml_dir))

# print(l)
seq = 1
for item in l:
    if item.endswith(".xml"):
        # print(item[:-4])

        seq+=1
        if seq % 7==0:
            val.write("{} -1\n".format(item[:-4]))
        else:
            train.write("{} -1\n".format(item[:-4]))


train.close()