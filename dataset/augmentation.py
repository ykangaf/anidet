'''
This is not used since TF provides
random horizontal flip option
in config files

'''







import sys
import os
from PIL import Image
from PIL import ImageOps
import xml.etree.ElementTree as ET

xml_dir = "Annotations"
img_dir = "JPEGImages"
IMG_RES = 512

p = "/projects/anidet/dataset"
l = os.listdir(os.path.join(p, xml_dir))

count = 0
for i in l:

    # if count >0:
    #     break

    if i.endswith(".xml") and not i.startswith("f"):

        # xml_original = open( os.path.join(p, xml_dir, i) , "r")
        xml_flip_name = "f" + i[: -4] + ".xml"


        tree = ET.parse(os.path.join(p, xml_dir, i))
        root = tree.getroot()
        for x in root.findall('path'):
            # print(x.text)
            id1 = x.text.find(img_dir) + 11
            x.text  = x.text[:id1] + "f" + x.text[id1:]
            print(x.text)

        for x in root.findall('object/bndbox/xmin'):
            # print(x.text)
            offset = int(x.text)
            offset = IMG_RES - 1 - offset
            x.text = str(offset)
            # print(x.text)

        for x in root.findall('object/bndbox/xmax'):
            # print(x.text)
            offset = int(x.text)
            offset = IMG_RES - 1 - offset
            x.text = str(offset)
            # print(x.text)

    
        tree.write( os.path.join(p, xml_dir, xml_flip_name) , encoding='utf8')

        img_name = i[: -4] + ".jpg"
        img_flip_name = "f" + i[: -4] + ".jpg"
        im = Image.open(os.path.join(p, img_dir, img_name))
        im = ImageOps.mirror(im)
        im.save(os.path.join(p, img_dir, img_flip_name) )


        # xml_flip = open( os.path.join(p, xml_dir, xml_flip_name) , "w+")
        # img_flip = open( os.path.join(p, img_dir, img_flip_name) , "w+")

        # content = xml_original.readlines()
        # for line in content:
        #     id1 = line.find("xmin")
        #     if id1 >=0:

    count +=1
