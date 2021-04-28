#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from tool_file import ToolFile
import os

tf = ToolFile()
source_dir = 'Hack'
json_dir = 'Json'
if not os.path.exists(json_dir):
    os.mkdir(json_dir)
    print('Create a new folder:{0}'.format(json_dir))
files, labels = tf.get_dir_files(source_dir)      # We put all the data sets under this folder.
size = len(files)

dict_list = []
for i in range(size):
    _, d = tf.file_to_dict(files[i])
    dict_list.append(d)
    tf.dict_to_file(d, os.path.join(json_dir, '{0}.json'.format(labels[i])))

# Verify
json_files, labels = tf.get_dir_files(json_dir)
for i in range(size):
    file_dict = tf.json_to_dict(json_files[i])
    # print(type(file_dict))
    # print(len(file_dict), len(dict_list[i]))
    # print(file_dict['123456'], end='    ')
    # print(dict_list[i]['123456'])
