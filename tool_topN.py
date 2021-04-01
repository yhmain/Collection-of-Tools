#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os
from tool_file import ToolFile


def run_file(file, topN=0, mode='NUMBER'):
    tf = ToolFile()
    _, res_dict = tf.file_to_dict(file, mode)
    new_dict = tf.sort_dict_by_val(res_dict, topN)
    for k, v in new_dict.items():
        print(k, '{0}%'.format(round(v * 100, 4)))


if __name__ == '__main__':
    topN = 11
    mode = 'FREQUENCY'
    file = os.path.join('EN', 'Zoosk.txt')
    run_file(file, topN, mode)
