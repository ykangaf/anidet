python .\extra\create_pascal_tf_record_new.py --label_map_path=.\dataset\pascal_label_map.pbtxt --data_dir=.\dataset --year=VOC2012 --set=train --output_path=.\dataset\pascal_train.record


python .\extra\create_pascal_tf_record_new.py --label_map_path=.\dataset\pascal_label_map.pbtxt --data_dir=.\dataset --year=VOC2012 --set=val --output_path=.\dataset\pascal_val.record

# python object_detection/dataset_tools/create_pascal_tf_record.py \
#     --label_map_path=object_detection/data/pascal_label_map.pbtxt \
#     --data_dir=VOCdevkit --year=VOC2012 --set=val \
#     --output_path=pascal_val.record

# map_train.txt