#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import tkinter as tk

keyboard_value = [
    [['Esc'], ['F1'], ['F2'], ['F3'], ['F4'], ['F5'], ['F6'], ['F7'], ['F8'], ['F9'], ['F10'], ['F11'], ['F12']],
    [['~', '`'], ['!', '1'], ['@', '2'], ['#', '3'], ['$', '4'], ['%', '5'], ['^', '6'], ['&', '7'], ['*', '8'], ['(', '9'], [')', '0'], ['_', '-'], ['+', '='], ['Back']],
    [['Tab'], ['Q'], ['W'], ['E'], ['R'], ['T'], ['Y'], ['U'], ['I'], ['O'], ['P'], ['{', '['], ['}', ']'], ['|', '\\']],
    [['Caps lock'], ['A'], ['S'], ['D'], ['F'], ['G'], ['H'], ['J'], ['K'], ['L'], [':', ';'], ['\"', ''], ['Enter']],
    [['Shift'], ['Z'], ['X'], ['C'], ['V'], ['B'], ['N'], ['M'], ['<', ','], ['>', '.'], ['?', '/'], ['Shift']],
    [['Ctrl'], ['Win'], ['Alt'], ['Long Space'], ['Alt'], ['Win'], ['R-clk'], ['Ctrl']]  # Mouse Right
]

key_offset = [
    [[40, 40], [40, 40], [40, 40], [40, 40], [40, 40], [40, 40], [40, 40], [40, 40], [40, 40], [40, 40], [40, 40], [40, 40], [40, 40]],
    [[40, 40], [40, 40], [40, 40], [40, 40], [40, 40], [40, 40], [40, 40], [40, 40], [40, 40], [40, 40], [40, 40], [40, 40], [40, 40], [85, 40]],
    [[75, 40], [40, 40], [40, 40], [40, 40], [40, 40], [40, 40], [40, 40], [40, 40], [40, 40], [40, 40], [40, 40], [40, 40], [40, 40], [50, 40]],
    [[80, 40], [40, 40], [40, 40], [40, 40], [40, 40], [40, 40], [40, 40], [40, 40], [40, 40], [40, 40], [40, 40], [40, 40], [85, 40]],
    [[97.5, 40], [40, 40], [40, 40], [40, 40], [40, 40], [40, 40], [40, 40], [40, 40], [40, 40], [40, 40], [40, 40], [107, 40]],
    [[75, 40], [40, 40], [50, 40], [270, 40], [50, 40], [40, 40], [40, 40], [40, 40]]
]


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Rectangle:
    def __init__(self, top_left, right_bottom, value):
        self.top_left = top_left
        self.right_bottom = right_bottom
        self.value = value


class Key:
    def __init__(self, kb, rect):
        self.kb = kb
        self.rect = rect

    def draw_key(self):
        self.kb.create_rectangle(self.rect.top_left.x, self.rect.top_left.y, self.rect.right_bottom.x, self.rect.right_bottom.y, fill='WhiteSmoke', outline='black', tag='kk')
        if len(self.rect.value) == 1:
            self.kb.create_text((self.rect.top_left.x + self.rect.right_bottom.x)//2, (self.rect.top_left.y + self.rect.right_bottom.y)//2, text=self.rect.value[0])
        else:
            self.kb.create_text(self.rect.top_left.x + 5, self.rect.top_left.y + 10, text=self.rect.value[0])
            self.kb.create_text((self.rect.top_left.x + self.rect.right_bottom.x)//2, (self.rect.top_left.y + self.rect.right_bottom.y)//2+5, text=self.rect.value[1])


class KeyBoard:
    def __init__(self):
        self.key_dict = {}
        # for i in range(len(keyboard_value)):
        #     for j in range(len((keyboard_value[i]))):
        #         for k in range(len(keyboard_value[i][j])):
        #             self.key_dict[keyboard_value[i][j][k]] = [i, j, k]

        self.window = tk.Tk()
        self.window.title('Soft Keyboard')
        self.window_width = 700
        self.window_height = 280
        # The first two parameters are the size of the window,
        # and the last two parameters are the position of the window.
        # Set the window to center
        screenwidth = self.window.winfo_screenwidth()
        screenheight = self.window.winfo_screenheight()
        self.window.geometry("%dx%d+%d+%d" % (self.window_width, self.window_height,
                                              (screenwidth - self.window_width) / 2,
                                              (screenheight - self.window_height) / 2))
        # create a new canvas
        self.keyboard = tk.Canvas(self.window, width=700, height=280, bg="white")

    def draw_keyboard(self, password=''):
        # First ,I draw the original keyboard
        start_y = 20
        for i in range(1, len(keyboard_value)):
            start_x = 20
            for j in range(len(keyboard_value[i])):
                p1 = Point(start_x, start_y)
                p2 = Point(start_x + key_offset[i][j][0], start_y + key_offset[i][j][1])
                rect = Rectangle(p1, p2, keyboard_value[i][j])
                Key(self.keyboard, rect).draw_key()
                start_x += key_offset[i][j][0]
                for k in range(len(keyboard_value[i][j])):
                    self.key_dict[keyboard_value[i][j][k]] = [p1, p2]
            start_y += key_offset[i][0][1]

        # Then, show the password on the keyboard
        x0 = -1
        y0 = -1
        for c in password.upper():
            if c not in self.key_dict.keys():
                # print('Illegal character.')
                pass
            else:
                p1 = self.key_dict[c][0]
                p2 = self.key_dict[c][1]
                px = (p1.x + p2.x) / 2
                py = (p1.y + p2.y) / 2
                if x0 == -1:
                    self.keyboard.create_oval(px - 1, py - 1, px + 1, py + 1, fill='red')
                else:
                    self.keyboard.create_line(x0, y0, px, py, fill='green', arrow='last')
                x0 = px         # update the previous point x
                y0 = py         # update the previous point y

        self.keyboard.pack()
        self.window.mainloop()


kb = KeyBoard()
kb.draw_keyboard('zxcvbn2345tgb')

