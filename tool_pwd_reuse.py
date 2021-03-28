#!/usr/bin/env python

from tool_file import ToolFile


def Levenshtien(s1, s2):
    m = len(s1)
    n = len(s2)
    LD = [[0 for col in range(n)] for row in range(m)]
    for i in range(m):
        for j in range(n):
            if i == 0 and j == 0:
                LD[i][j] = 0
            elif i != 0 and j == 0:
                LD[i][j] = i
            elif i == 0 and j != 0:
                LD[i][j] = j
            else:
                LDi = LD[i - 1][j] + 1
                LDj = LD[i][j - 1] + 1
                LDS = LD[i - 1][j - 1] if s1[i] == s2[j] else LD[i - 1][j - 1] + 1
                LD[i][j] = min(LDi, LDj, LDS)
    return 1 - LD[m-1][n-1]/max(m, n)


tf = ToolFile()
list_files, list_labels = tf.get_dir_files("Hack")
s1 = open(list_files[0], 'r', encoding='utf-8').readlines()
s2 = open(list_files[1], 'r', encoding='utf-8').readlines()
print(Levenshtien(s1, s2))

# a = {'x': 1, 'y': 2, 'z': 3}
# b = {'x': 1, 'w': 11, 'z': 12}
#
# print(a.keys() & b.keys())
# print(a.keys() ^ b.keys())
# print(a.keys() - b.keys())
#
# print(a.items() & b.items())

