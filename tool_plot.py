#!/usr/bin/env python

import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter


class ToolPlot:

    def __init__(self, list_labels, list_x_y_data, save_path_dir="Plot"):     # Initialize
        self.test = 1                                                               # It means nothing, just the test.

        # self.markers = ['o', 's', 'D', '^', 'v', '>']
        # self.line_styles = ['-', '-', '-', '-', '-', '-']         # Solid line or dotted line format
        # self.line_widths = {value: 4.0 for value in range(0, 6)}  # setting the width of each line to 4
        self.colors = ['red', 'limegreen', 'purple', 'blue', 'cyan', 'green']  # Line color
        self.titles = ['PCFG', 'Markov']                            # Picture title
        self.markers = ['s', 'o', 'v', '^', 'D', None]
        self.line_styles = ['--', '--', '-.', ':', 'dotted', '--']   # Solid line or dotted line format
        self.line_widths = {0: 1.5, 1: 1.5, 2: 1.5, 3: 1.5, 4: 1.5, 5: 1.5}
        self.font_size = 12

        self.list_labels = list_labels                              # Label list
        self.save_path_dir = save_path_dir                          # Image storage path
        self.x_y_data = list_x_y_data                               # eg. {"7k7k":[[key list], [value list]]}
        self.size = len(list_labels)
        # Format the picture (display grid)
        # plt.grid(linestyle='-')

    # Set the coordinate axis to be displayed as a percent sign
    def to_percent(self, temp, position):           # position cannot be deleted
        self.test = 1
        return '%1.0f' % temp + '%'

    def to_e_format(self, temp, position):
        self.test = 1
        return '' % temp

    # Draw multiple line charts in a picture
    def plot_on_single_file(self):
        plt.figure(figsize=(9.0, 4.8), dpi=100)             # Set the appropriate picture size and pixels
        la = self.x_y_data[self.list_labels[0]][0]

        index = 0
        for k, data in self.x_y_data.items():
            plt.scatter(data[0], data[1], color=self.colors[index], label=str(k), linewidth=self.line_widths[index],
                        marker=self.markers[index])
            index += 1
        plt.legend(loc='upper right', fancybox=True, frameon=True, edgecolor='black')   # Set the legend position

        # set x,y format
        plt.xticks([x for x in range(0, len(la))], la, rotation=0)
        plt.xlim(0, len(la))

        # y_text = ['0.1', '0.01', '1e-3', '1e-4', '1e-5', '1e-6', '1e-7', '1e-8']
        # y_text = ['1e-8', '1e-7', '1e-6', '1e-5', '1e-4', '1e-3', '0.01', '0.1']
        # plt.yticks(np.logspace(-6, 0, 7))
        # print(np.logspace(-6, 0, 7))
        # plt.ylim(10**(-6), 7)
        # plt.yscale('log')

        # Set title, label, etc.
        plt.xlabel('Characters')
        plt.ylabel('Occurrence Percentage')
        plt.savefig(os.path.join(self.save_path_dir, 'result.png'))                     # plot_path + 'result.png'
        print('Picture：', self.save_path_dir + '/result.png ', 'saved successfully.')
        plt.show()

