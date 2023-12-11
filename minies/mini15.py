from copy import deepcopy as c
import matplotlib.pyplot as plt
import numpy as np
from time import time

def game(field, iter, mode):
    t = time()
    init_field = c(field) 
    for _ in range(iter):
        for i in range(len(field)):
            for j in range(len(field[i])):
                life = int(init_field[i][j])
                i_minus = i-1
                i_plus = i+1 if i+1 < len(field) else 0
                j_minus = j-1
                j_plus = j+1 if j+1 < len(field) else 0
                close = [init_field[i_minus][j_minus], init_field[i_minus][j], init_field[i_minus][j_plus], 
                        init_field[i][j_minus], init_field[i][j_plus], 
                        init_field[i_plus][j_minus], init_field[i_plus][j], init_field[i_plus][j_plus]]
                close = [int(e) for e in close]
                sum_of_life = sum(close)
                if life:
                    if sum_of_life < 2 or sum_of_life > 3:
                        field[i][j] = '0'
                else:
                    if sum_of_life == 3:
                        field[i][j] = '1'

        for i in range(len(field)):
            for j in range(len(field[i])):
                print(field[i][j], end='') if int(field[i][j]) else print('_', end='')
            print()
        # fig, ax = plt.subplots()
        # mat = ax.matshow(field)
        # plt.show()   
    t = time() - t
    match mode:
        case 't':
            return f'Time is {t}, lives is {sum(field)}'
    
        
init_field = np.random.choice(a=['0', '1'], size=(30, 30)).tolist()
print('Choose mode:')
print('1. Visual')
print('2. Time')
l = 128
mode = None
match input():
    case 1:
        mode = 'i'
    case 2:
        mode = 't'
t_py = game(init_field, l, mode)
t_np = game(init_field, l, mode)
print('Py:', t_py)
print('Numpy:', t_np)