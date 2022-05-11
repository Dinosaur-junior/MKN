# -*- coding: utf-8 -*-
# Probabilities
#                __
#               / _)
#      _.----._/ /
#     /         /
#  __/ (  | (  |
# /__.-'|_|--|_|
# Written by Dinosaur
# ---------------------------------------------------------------------------------------------------------------------

# import libraries
import random

# ---------------------------------------------------------------------------------------------------------------------
# configuration

repeat = 1000000  # number of repetitions


# ---------------------------------------------------------------------------------------------------------------------
# functions

# Getting a random item out of the box
def box():
    return random.randint(1, 3)


# Opening 7 boxes and checking the receipt of the set
def open_boxes():
    dataset = len(set([box() for i in range(7)]))
    return True if dataset == 3 else False


# Getting statistics based on multiple repetition
def get_statistic():
    data = sum([open_boxes() for i in range(repeat)]) / repeat * 100
    return data


# ---------------------------------------------------------------------------------------------------------------------
# run method

if __name__ == '__main__':
    result = get_statistic()
    print(f'Вероятность выпадения сета составляет {result}%')
