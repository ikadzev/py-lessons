from copy import deepcopy as c
import matplotlib.pyplot as plt
import numpy as np
from time import time

def game(field, iter):
    t = 0
    init_field = c(field)
    _, ax = plt.subplots()
    plt.ion()
    for _ in range(iter):
        now = time()
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
                        field[i][j] = False
                else:
                    if sum_of_life == 3:
                        field[i][j] = True
        t += time() - now
        ax.clear()
        ax.matshow(field)
        plt.show()
        plt.pause(0.05)
        init_field = c(field)
    plt.close()
    return t
    
iters = 128
init_field = np.random.choice(a=[False, True], size=(100, 100), p=[0.3, 0.7])
t_py = game(init_field.tolist(), iters)
t_np = game(init_field, iters)
print('Py:', t_py)
print('Numpy:', t_np)