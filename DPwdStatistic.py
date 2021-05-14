#!/usr/bin/python
# -*- coding: UTF-8 -*-


import os
import re
import pandas as pd


class Item:
    def __init__(self):
        self.dataSetName = ''
        self.total = 0
        self.unique = set()         # 注意此处使用set记录唯一口令
        self.hasDigit = 0
        self.onlyDigit = 0
        self.singleDigit = 0
        self.data = ['']*6  # 实际上，我不用对应变量记录上述6个值，而是用列表记录
        # self.data = ['', 0, set(), 0, 0, 0]     # 实际上，我不用对应变量记录上述6个值，而是用列表记录


class DPS:
    def __init__(self):
        self.test = 1
        self.items = []
        self.encoding = 'UTF-8'         # 设置文件编码
        self.decimal = 4                # 运算保留4位小数
        self.output = 'Result.xlsx'     # 结果输出目录

    def get_files(self, source_dir):
        self.test = 1
        files = os.listdir(source_dir)  # Get the name list of all files in the folder
        list_files = []                 # Path for storing files
        list_labels = []                # Store file name tags. Example:test.txt ===>test
        for file in files:
            path = os.path.join(source_dir, file)
            if not os.path.isdir(path):  # Determine if it is a folder
                list_files.append(path)
                list_labels.append(str(file).split('.')[0])
        return list_files, list_labels

    def write_dict_excel(self, resDict):
        writer = pd.ExcelWriter(self.output)
        ds = pd.DataFrame(resDict)
        ds.to_excel(writer, sheet_name='数字口令统计表', encoding=self.encoding)
        writer.save()

    def analyze_file(self, file):
        item = Item()
        item.dataSetName = file.split('\\')[-1].split('.')[0]       # 提取出数据集的文件名，去掉后缀.txt
        with open(file, 'r', encoding=self.encoding) as f:
            for line in f:
                line = line.strip('\n')
                if line == '':          # 避免空行
                    continue
                item.total += 1
                item.unique.add(line)               # 集合set对于重复元素自动过滤
                d = re.findall('(\d+)', line)
                if len(d) > 0:                      # 此时表示口令中包含数字
                    item.hasDigit += 1              # 包含数字的口令数量加1
                    if len(d) == 1:                 # 有2种情况，可能是纯数字的口令123456，也有可能是包含一个数字串的口令wang123456!
                        if len(d[0]) == len(line):  # 长度相等说明是纯数字
                            item.onlyDigit += 1
                        else:
                            item.singleDigit += 1
                    else:                           # 否则一定是是包含一个数字串的口令
                        item.singleDigit += 1
        item.data[0] = item.dataSetName
        item.data[1] = format(item.total, ',')
        item.data[2] = format(len(item.unique), ',')
        item.data[3] = '{0}({1}%)'.format(format(item.hasDigit, ','), round(item.hasDigit/item.total*100, self.decimal))
        item.data[4] = '{0}({1}%)'.format(format(item.onlyDigit, ','), round(item.onlyDigit/item.hasDigit*100, self.decimal))
        item.data[5] = '{0}({1}%)'.format(format(item.singleDigit, ','), round(item.singleDigit/item.hasDigit*100, self.decimal))
        self.items.append(item.data)
        print('文件 {0} 分析完毕.'.format(file))

    def run(self, path, mode='DIR'):            # 两种输入模式DIR或者FILE ，即表示输入是文件还是目录
        if mode == 'DIR':
            files, _ = self.get_files(path)
            for f in files:
                self.analyze_file(f)
        elif mode == 'FILE':
            self.analyze_file(path)
        columns = ['数据集', '总口令条数', '唯一口令条数', '含有数字的口令条数占总口令条数比例', '只有数字的口令条数占含有数字的口令条数比例', '包含单个数字串的口令条数占含有数字的口令条数比例']
        resDict = dict()
        for c in columns:
            resDict[c] = list()
        for d in self.items:
            for i in range(len(columns)):
                resDict[columns[i]].append(d[i])
        self.write_dict_excel(resDict)


dps = DPS()
dps.run('Hack', 'DIR')
