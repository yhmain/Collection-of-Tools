#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import shutil
import collections
import pandas as pd
import json


class ToolFile:
    def __init__(self):
        self.test = 1  # It means nothing, just the test.

    '''
        Empty the old folder or create a new folder
    '''

    def create_plot_folder(self, plot_path):
        self.test = 1
        if os.path.exists(plot_path):
            print('The {0} folder is found to exist.'.format(plot_path))
            # os.removedirs(plot_path)              # You can delete a folder, but it fails when the folder is not empty
            shutil.rmtree(plot_path)
            print('The {0} folder was successfully deleted.'.format(plot_path))
            os.mkdir(plot_path)  # os.makedirs () creates multi-level directories
            print('The {0} folder was successfully created.'.format(plot_path))
        else:
            print('Found that the {0} folder does not exist.'.format(plot_path))
            os.mkdir(plot_path)
            print('The {0} folder was successfully created.'.format(plot_path))
        print()

    '''
        Get all files in the current directory (excluding folders)
        eg.  ["Test/pwd.txt"]   ["pwd"]
    '''

    def get_dir_files(self, source_dir):
        self.test = 1
        files = os.listdir(source_dir)  # Get the name list of all files in the folder
        list_files = []  # Path for storing files
        list_labels = []  # Store file name tags. Example:test.txt ===>test
        for file in files:
            path = os.path.join(source_dir, file)
            if not os.path.isdir(path):  # Determine if it is a folder
                list_files.append(path)
                list_labels.append(str(file).split('.')[0])
        return list_files, list_labels

    '''
        Count the number of lines in large text files
    '''

    def get_file_lines(self, filename):
        self.test = 1
        count = 0
        fp = open(filename, "rb")
        byte_n = bytes("\n", encoding="utf-8")
        while 1:
            buffer = fp.read(16 * 1024 * 1024)
            if not buffer:
                # count += 1          # contains the last empty line ''
                break
            count += buffer.count(byte_n)
        fp.close()
        return count

    '''
        Get the frequency or number of each character in the file
        val="NUMBER" or "FREQUENCY"
        decimal represents the exact decimal place
    '''

    def get_file_char(self, file, val='NUMBER', decimal=8):
        self.test = 1
        char_total = 0
        char_dict = {}
        # for c in range(48, 58):
        # char_dict[chr(c)] = 0
        for c in range(0, 26):
            char_dict[chr(c + 65)] = 0
            char_dict[chr(c + 97)] = 0
        specials = "`~!@#$%^&*()_-+={}[]|\\:;\"'<>,.?/"
        # for c in specials:
        # char_dict[c] = 0
        # print(len(char_dict))           # SIZE:94
        with open(file, 'r', encoding='utf-8-sig') as f:
            for line in f:
                line = line.strip(" \n")
                for c in line:
                    if c not in char_dict.keys():
                        pass
                        # print("Illegal char: ", c)
                    else:
                        char_total += 1
                        char_dict[c] += 1
        if val == "FREQUENCY":
            for k, v in char_dict.items():
                char_dict[k] = round(v / char_total, decimal)
        # print(char_dict)
        return char_total, char_dict

    '''
        A simple function of counting word frequency in text files
        val="NUMBER" or "FREQUENCY"
        decimal represents the exact decimal place
    '''

    def file_to_dict(self, file, val='NUMBER', decimal=8):
        self.test = 1
        total_num = 0
        word_freq = collections.defaultdict(int)
        print('-' * 10, 'Status: Start counting the word frequency of file {0}'.format(file), '-' * 10)
        with open(file, 'r', encoding='UTF-8') as f:
            for line in f:
                line = line.strip('\n')
                if line == '':
                    continue
                total_num += 1
                word_freq[line] += 1
        if val == "FREQUENCY":
            for k, v in word_freq.items():
                word_freq[k] = round(v / total_num, decimal)
        print('-' * 10, 'Status: Word frequency statistics of file {0} finished'.format(file), '-' * 10, '\n')
        return total_num, word_freq

    '''
        counting word frequency in text files
        the results are in json format
    '''
    def dict_to_json(self, data):
        self.test = 1
        json_data = json.dumps(data, ensure_ascii=False)
        return json_data

    '''
        counting word frequency in text files
        the results are in json format
    '''
    def json_to_file(self, data, file):
        self.test = 1
        with open(file, mode='w', encoding='utf-8') as f:
            json.dump(data, f)

    '''
        counting word frequency in text files
        the results are in json format
    '''
    def json_to_dict(self, file):
        self.test = 1
        with open(file, mode='r', encoding='utf-8') as f:
            file_dict = json.load(f)
        return file_dict

    '''
        Sort the dictionary in descending order by value
    '''
    def sort_dict_by_key(self, my_dict, n=0):
        self.test = 1
        if n == 0:
            n = len(my_dict)
        L = sorted(my_dict.items())
        L = L[:n]
        new_dict = {}
        for l in L:
            new_dict[l[0]] = l[1]
        return new_dict


    '''
        Sort the dictionary in descending order by value
    '''

    def sort_dict_by_val(self, my_dict, n=0):
        self.test = 1
        if n == 0:
            n = len(my_dict)
        L = sorted(my_dict.items(), key=lambda item: item[1], reverse=True)
        L = L[:n]
        new_dict = {}
        for l in L:
            new_dict[l[0]] = l[1]
        return new_dict

    '''
        Reorder the target dictionary according to the template dictionary
    '''

    def sort_dict_by_target(self, source_dict, target_dict):
        self.test = 1
        new_dict = {}
        for k in source_dict.keys():
            new_dict[k] = target_dict[k]
        return new_dict

    '''
        Dictionary converted to list
        return:
        list[0] = key list
        list[1] = value list
    '''

    def dict_to_list(self, my_dict):
        self.test = 1
        res = [list(my_dict.keys()), list(my_dict.values())]
        return res

    '''
        Find the reverse order number of two lists A and B.
    '''

    def get_inv_number(self, template, target):
        self.test = 1
        temp_dict = {}
        for i in range(len(template)):
            temp_dict[template[i]] = i
        ans = 0
        n = len(target)
        for i in range(n):
            for j in range(i):
                if target[i] not in temp_dict.keys() or target[j] not in temp_dict.keys():
                    # print('NOt in : ', target[i], target[j])
                    ans += 1
                else:
                    if temp_dict[target[j]] > temp_dict[target[i]]:
                        ans += 1
        return ans

    '''
        Read data from Excel
        And get inversion number
    '''

    def read_excel_data(self, file):
        self.test = 1
        df = pd.read_excel(file, engine='openpyxl')
        resolve_dict = {}
        for k, v in df.items():
            resolve_dict[k] = list(v)[:5]
        for temp_k in resolve_dict.keys():
            for target_k in resolve_dict.keys():
                print(temp_k, ' To  ', target_k, '  ',
                      self.get_inv_number(resolve_dict[temp_k], resolve_dict[target_k]))

