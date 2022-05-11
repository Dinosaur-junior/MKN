# -*- coding: utf-8 -*-
# String comparisons
#                __
#               / _)
#      _.----._/ /
#     /         /
#  __/ (  | (  |
# /__.-'|_|--|_|
# Written by Dinosaur
# ---------------------------------------------------------------------------------------------------------------------

# import libraries

import os
import random

import matplotlib.pyplot as plt
from config import max_n, repeat

# ---------------------------------------------------------------------------------------------------------------------
# configuration

# output file
path = os.path.dirname(os.path.realpath(__file__))
output_filename = 'output.txt'
output_file_path = os.path.join(path, output_filename)
f = open(output_file_path, 'w')
f.close()
output_file = open(output_file_path, 'a')


# ---------------------------------------------------------------------------------------------------------------------
# functions

# creating random string with n len
def create_string(n):
    random_list = [str(random.randint(0, 1)) for i in range(n)]
    return ''.join(random_list)


# searching for difference between two strings
def difference(word_one, word_two):
    return sum(l1 != l2 for l1, l2 in zip(word_one, word_two))


# creating the plot
def create_plot(data):
    ox = [i for i in data]
    oy = [data[i] for i in data]

    fig, ax = plt.subplots()
    plt.title('Зависимость количества зачеркиваний от длины строки')
    plt.plot(ox, oy)
    ax.set_xlabel('длина строки')
    ax.set_ylabel('количество зачеркиваний')

    plt.savefig('saved_figure.png')
    print('Plot saved', file=output_file)


# main function
def main():
    print('start\n', file=output_file)
    print('start')

    data = {}
    # enumeration of string len
    for n in range(max_n + 1):
        print(f'{n=}', file=output_file)
        print(f'{n=}')

        data[n] = []
        # repeats
        for i in range(repeat):
            string_1 = create_string(n)
            string_2 = create_string(n)
            diff = difference(string_1, string_2)
            print(f'    {i} -- {string_1=}, {string_2=} -- {diff=}', file=output_file)
            data[n].append(diff)
        print('\n', file=output_file)

    # getting the average value of difference
    for i in data:
        data[i] = sum(data[i]) / repeat

    print('result:', file=output_file)
    for i in data:
        print(f'n={i}: diff={data[i]}', file=output_file)

    print('', file=output_file)
    print('creating the plot', file=output_file)
    print('creating the plot')
    create_plot(data)
    print('End', file=output_file)
    print('End')


# ---------------------------------------------------------------------------------------------------------------------
# run method
if __name__ == '__main__':
    main()
