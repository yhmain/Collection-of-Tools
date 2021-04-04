#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Reference
# A Large-Scale Empirical Analysis of Chinese Web Passwords
# url:https://www.usenix.org/conference/usenixsecurity14/technical-sessions/presentation/li_zhigong

# 3 Types
# Same Row: The same row passwords are formed by a consecutive sequence of
# characters in the same row on keyboard, e.g., asdfhj.

# Zig Zag: The zig-zag passwords are formed by a sequence of characters,
# where each key is adjacent to the next one but not in the same row, e.g., qawsxd.

# Snake: The snake passwords consist of a sequence of characters whose keys
# are adjacent on keyboards yet they are neither in the Same Row or Zig Zag,e.g., zxcfgh.


from tool_file import ToolFile


KEYBOARD = [
    [['Esc'], ['F1'], ['F2'], ['F3'], ['F4'], ['F5'], ['F6'], ['F7'], ['F8'], ['F9'], ['F10'], ['F11'], ['F12'], ['pause'], ['sysrq']],
    [['~', '`'], ['!', '1'], ['@', '2'], ['#', '3'], ['$', '4'], ['%', '5'], ['^', '6'], ['&', '7'], ['*', '8'], ['(', '9'], [')', '0'], ['_', '-'], ['+', '='], ['Back']],
    [['Tab'], ['Q'], ['W'], ['E'], ['R'], ['T'], ['Y'], ['U'], ['I'], ['O'], ['P'], ['{', '['], ['}', ']'], ['|', '\\']],
    [['Caps lock'], ['A'], ['S'], ['D'], ['F'], ['G'], ['H'], ['J'], ['K'], ['L'], [':', ';'], ['\"', "'"], ['Enter']],
    [['LShift'], ['Z'], ['X'], ['C'], ['V'], ['B'], ['N'], ['M'], ['<', ','], ['>', '.'], ['?', '/'], ['RShift']],
    [['LCtrl'], ['Win'], ['Alt'], ['Long Space'], ['Alt Gr'], ['Win'], ['R-clk'], ['RCtrl']]  # R-clk Mouse Right
]


KEYMAP = {
    # It will be initialized in the program
}


def init_map():
    for i in range(len(KEYBOARD)):
        for j in range(len(KEYBOARD[i])):
            for k in range(len(KEYBOARD[i][j])):
                KEYMAP[KEYBOARD[i][j][k]] = [j, i]


def is_adjacent(p1, p2):
    if p1 not in KEYMAP.keys() or p2 not in KEYMAP.keys():
        return 99
    c1 = KEYMAP[p1]
    c2 = KEYMAP[p2]
    return abs(c1[0]-c2[0]) + abs(c1[1]-c2[1]) <= 1


def is_same_row(p1, p2):
    if p1 not in KEYMAP.keys() or p2 not in KEYMAP.keys():
        return False
    c1 = KEYMAP[p1]
    c2 = KEYMAP[p2]
    return c1[1] == c2[1]


def identify_keyboard_pattern(password):
    len_pwd = len(password)
    if len_pwd < 4:
        return 'NO_PATTERN'
    same_row = True
    zigzag = True
    password = password.upper()
    for i in range(1, len_pwd):
        pos1 = password[i-1]
        pos2 = password[i]
        if is_adjacent(pos1, pos2):
            same_row = same_row and is_same_row(pos1, pos2)
            zigzag = zigzag and not (is_same_row(pos1, pos2))
        else:
            return 'NO_PATTERN'
    if same_row:
        return 'SAME_ROW'
    if zigzag:
        return 'ZIG_ZAG'
    return 'SNAKE'


def identify_file_pattern(file):
    ans = {'NO_PATTERN': 0, 'SAME_ROW': 0, 'ZIG_ZAG': 0, 'SNAKE': 0}
    cnt = 0
    with open(file, 'r', encoding='utf-8') as f:
        for line in f:
            cnt += 1
            line = line.strip(" \n")
            # print(line)
            ans[identify_keyboard_pattern(line)] += 1
    for k, v in ans.items():
        ans[k] = '{0}%'.format(round(100 * v/cnt, 3))
    return ans


if __name__ == '__main__':
    init_map()
    my_dir = 'Hack'
    tf = ToolFile()
    files, _ = tf.get_dir_files(my_dir)
    for file in files:
        ans_dict = identify_file_pattern(file)
        print(file, '-----: ', ans_dict)
    # pwd = 'asdfhj'
    # print(identify_keyboard_pattern(pwd))
    # print(KEYMAP)
