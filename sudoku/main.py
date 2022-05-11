# -*- coding: utf-8 -*-
# Sudoku solver
#                __
#               / _)
#      _.----._/ /
#     /         /
#  __/ (  | (  |
# /__.-'|_|--|_|
# Written by Dinosaur
# ---------------------------------------------------------------------------------------------------------------------

# import libraries

import tkinter as tk
from tkinter import *
import os

# ---------------------------------------------------------------------------------------------------------------------
# configuration

# statistic config
# output file
path = os.path.dirname(os.path.realpath(__file__))
output_filename = 'output.txt'
output_file_path = os.path.join(path, output_filename)
f = open(output_file_path, 'w')
f.close()
output_file = open(output_file_path, 'a')


# ---------------------------------------------------------------------------------------------------------------------
# sudoku colver functions

# check if input sudoku is correct
def check(grid):
    print('Checking sudoku', file=output_file)
    print('Checking sudoku')

    # check in rows
    rows = [grid[x] for x in range(9)]
    for row in rows:
        for elem in row:
            if elem > 0:
                if row.count(elem) != 1:
                    print('Input sudoku is incorrect', file=output_file)
                    print('Input sudoku is incorrect')
                    return False

    # check in columns
    columns = [[grid[x][y] for x in range(9)] for y in range(9)]
    for column in columns:
        for elem in column:
            if elem > 0:
                if column.count(elem) != 1:
                    print('Input sudoku is incorrect', file=output_file)
                    print('Input sudoku is incorrect')
                    return False

    # check in squares 3x3
    squares = [[[] for y in range(3)] for x in range(3)]
    for x in range(9):
        for y in range(9):
            if grid[x][y] != 0:
                squares[x // 3][y // 3].append(grid[x][y])
    for row in squares:
        for square in row:
            for elem in square:
                if square.count(elem) != 1:
                    print('Input sudoku is incorrect', file=output_file)
                    print('Input sudoku is incorrect')
                    return False

    print('Input sudoku is correct', file=output_file)
    print('Input sudoku is correct')
    return True


# check if num in (row, col) is approach
def solve(grid, row, col, num):
    for x in range(9):
        if grid[row][x] == num:
            print(f"{row=} {col=}, {num=} -- is'not approach", file=output_file)
            return False

    for x in range(9):
        if grid[x][col] == num:
            print(f"{row=} {col=}, {num=} -- is'not approach", file=output_file)
            return False

    startRow = row - row % 3
    startCol = col - col % 3
    for i in range(3):
        for j in range(3):
            if grid[i + startRow][j + startCol] == num:
                print(f"{row=} {col=}, {num=} -- is'not approach", file=output_file)
                return False

    print(f'{row=} {col=}, {num=} -- is approach', file=output_file)
    return True


# main solving sudoku function
def sudoku(grid, row, col):
    M = 9
    if row == M - 1 and col == M:
        return True
    if col == M:
        row += 1
        col = 0
    if grid[row][col] > 0:
        print(f"{row=} {col=} -- at this point isn't empty", file=output_file)
        return sudoku(grid, row, col + 1)
    for num in range(1, M + 1, 1):
        if solve(grid, row, col, num):
            grid[row][col] = num
            if sudoku(grid, row, col + 1):
                return True
        grid[row][col] = 0
    return False


# ---------------------------------------------------------------------------------------------------------------------
# Sudoku classes

# Input Button
class InputButton(tk.Button):
    def __init__(self, apps, x, y):
        super().__init__()
        self.text = 0
        self.x = x
        self.y = y
        self.app = apps[self.x // 3][self.y // 3]
        self.button = Button(self.app, text='-', font=('Arial', 24), bg='grey', command=self.clicked)
        self.button.grid(column=x, row=y, padx=5, pady=5)

    # click the button
    def clicked(self):
        self.text = self.text + 1
        if self.text > 9:
            self.text = 0
            self.button.config(text='-')
        else:
            self.button.config(text=self.text)

        print(f'Set {self.text} on ({self.x}, {self.y})', file=output_file)
        self.button.update()


# Result label
class ResultLabel(tk.Label):
    def __init__(self, apps, x, y, grid):
        super().__init__()
        self.x = x
        self.y = y
        self.app = apps[self.x // 3][self.y // 3]
        self.label = Label(self.app, text=grid[self.x][self.y], font=('Arial', 32))
        self.label.grid(column=x, row=y, padx=5, pady=5)


# ---------------------------------------------------------------------------------------------------------------------
# Tkinter app class

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Судоку")
        self.main_frame = tk.Frame()
        self.create_input_page()

    # create sudoku grid
    def create_sudoku(self):
        self.main_frame.destroy()  # clear main frame
        self.main_frame = tk.Frame(master=self, width=200, height=200, relief=tk.RAISED, borderwidth=3)  # create main frame
        self.sudoku_frame = tk.Frame(master=self.main_frame, width=150, height=150, relief=tk.RAISED, borderwidth=3)  # create sudoku frame
        self.main_frame.grid()

        # create 3x3 sudoku frames
        self.frames = [ [tk.Frame(master=self.sudoku_frame, width=50, height=50, relief=tk.RAISED, borderwidth=2) for x in range(3)] for y in range(3)]
        [[self.frames[x][y].grid(column=x, row=y, padx=5, pady=5) for y in range(3)] for x in range(3)]
        self.sudoku_frame.grid()

    # create input page (with buttons)
    def create_input_page(self):
        self.create_sudoku()
        self.buttons = [[InputButton(self.frames, x, y) for y in range(9)] for x in range(9)]  # create buttons
        self.submit = Button(self.main_frame, text='Решить', font=('Arial', 24), bg='grey', command=self.solve)  # solve button
        self.submit.grid()

    # solve input sudoku
    def solve(self):
        grid = [[button.text for button in y] for y in self.buttons]
        print(f'Input sudoku: {grid}', file=output_file)
        print('\nStart solving', file=output_file)
        print('\nStart solving')

        if check(grid):  # checking sudoku
            print('Searching for answer', file=output_file)
            print('Searching for answer')
            res = sudoku(grid, 0, 0)  # solving sudoku
        else:
            res = False

        self.create_sudoku()
        self.labels = [[ResultLabel(self.frames, x, y, grid) for y in range(9)] for x in range(9)]

        if not res:
            print('There is no answer', file=output_file)
            print('There is no answer')

            label = tk.Label(master=self.main_frame, text="У данного судоку нет решения", font=('Arial', 24))
            label.grid()

        else:
            print(f'Answer: {grid}', file=output_file)
            print(f'Answer: {grid}')

        self.retry = Button(self.main_frame, text='Заново', font=('Arial', 24), bg='grey', command=self.create_input_page)
        self.retry.grid()
        print('\n', file=output_file)
        print('\n')


# ---------------------------------------------------------------------------------------------------------------------
# run method

if __name__ == "__main__":
    print('Program was started', file=output_file)
    print('Program was started')
    window = MainWindow()
    window.mainloop()
