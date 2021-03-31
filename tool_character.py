#!/usr/bin/python
# -*- coding: UTF-8 -*-

from tool_file import ToolFile
from tool_plot import ToolPlot

tf = ToolFile()
list_files, list_labels = tf.get_dir_files("EN")      # We put all the data sets under this folder.

x_y_data = {}
size = len(list_labels)

char_total, source_dict = tf.get_file_char(list_files[0], "FREQUENCY")
new_dict = tf.sort_dict_by_val(source_dict)
new_list = tf.dict_to_list(new_dict)
x_y_data[list_labels[0]] = new_list

# a, b = tf.file_to_dict(list_files[0])
# print(a)
# print(tf.get_file_lines(list_files[0]))

for i in range(1, size):
    char_total, char_dict = tf.get_file_char(list_files[i], "FREQUENCY")
    n_dict = tf.sort_dict_by_target(new_dict, char_dict)
    n_list = tf.dict_to_list(n_dict)
    x_y_data[list_labels[i]] = n_list

tp = ToolPlot(list_labels, x_y_data)
tf.create_plot_folder(tp.save_path_dir)
tp.plot_on_single_file()

