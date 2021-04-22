#!/usr/bin/env python
# -*- coding: GBK -*-

from tool_file import ToolFile
from tool_similarity import Similarity
import copy
import pandas as pd

tf = ToolFile()
dire = 'Hack'
files, labels = tf.get_dir_files(dire)
dict_list = []
set_list = []
for file in files:
    _, file_dict = tf.file_to_dict(file)
    dict_list.append(file_dict)
    set_list.append(set(list(file_dict.keys())))

sim = Similarity()
n = len(files)

dataJS = [[0 for col in range(n)] for row in range(n)]
dataJDIS = [[0 for col in range(n)] for row in range(n)]

for i in range(n):
    tempJS = []
    tempJDIS = []
    for j in range(i, n):
        # A_dict = copy.deepcopy(dict_list[i])        # deepcopy
        # B_dict = copy.deepcopy(dict_list[j])        # deepcopy
        # for c in (set_list[i] | set_list[j]):
        #     if c not in set_list[i]:
        #         A_dict[c] = 0
        #     if c not in set_list[j]:
        #         B_dict[c] = 0
        # A_dict = tf.sort_dict_by_key(A_dict)
        # B_dict = tf.sort_dict_by_key(B_dict)
        #
        # A = list(A_dict.values())
        # B = list(B_dict.values())
        #
        # print('{0}和{1}余弦距离：'.format(labels[i], labels[j]), sim.cosine_distance(A, B), end=' ')
        # print('{0}和{1}余弦相似度：'.format(labels[i], labels[j]), sim.calculate())

        C = set_list[i]
        D = set_list[j]
        jdis = sim.jaccard_distance(C, D)*100
        print('{0}和{1}杰卡德距离: '.format(labels[i], labels[j]), jdis, end='=' * 30)
        js = sim.calculate()*100
        print('{0}和{1}杰卡德相似度: '.format(labels[i], labels[j]), js)
        dataJS[i][j], dataJS[j][i] = js, js
        dataJDIS[i][j], dataJDIS[j][i] = jdis, jdis
    #     tempJS.append(js*100)
    #     tempJDIS.append(jdis*100)
    # dataJS.append(tempJS)
    # dataJDIS.append(tempJDIS)

writer = pd.ExcelWriter('Jaccard.xlsx')
js = pd.DataFrame(dataJS, columns=labels, index=labels)
js.index.name = 'Dataset(%)'
jdis = pd.DataFrame(dataJDIS, columns=labels, index=labels)
jdis.index.name = 'Dataset(%)'
js.to_excel(writer, sheet_name='杰卡德相似度')
jdis.to_excel(writer, sheet_name='杰卡德距离')
writer.save()
