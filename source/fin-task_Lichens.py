# %% [markdown]
# ## Задание
# Разработайте клеточный автомат «Лишайники», поведение которого подчинено следующим правилам:
# 1) Клетка может находиться в активном или пассивном состоянии
# 2) Клетка становится активной, если в восьми соседних клетках находится $N_1$, $N_2$ или $N_3$ активных клеток
# 3) Если число активных клеток в окрестности не равно $N_1$, $N_2$ или $N_3$, то клетка становится пассивной

# %%
import numpy as np
import tkinter as tk

# %%
root = tk.Tk()
cs = tk.Canvas(root, width=500, height=500)
cs.pack()

# %%
box = 5 # Размер клетки
N = 100
m = np.zeros([N,N], dtype=int) # Матрица состояния клеток
new_m = np.zeros([N,N], dtype=int) # Матрица новых состояний

N1 = 2
N2 = 4
N3 = 6

len(m), len(m[0])

# %%
count_cells = 50
rand_x = np.random.randint(0, N, count_cells)
rand_y = np.random.randint(0, N, count_cells)
rand_x, rand_y

# %%
for i in range(count_cells):
    m[rand_x[i]][rand_y[i]] = 1

# %%
rect = []
for i in range(N):
    for j in range(N):
        if m[i,j]:
            col = 'red'
        else:
            col = 'white'
        rect.append(cs.create_rectangle(i * box, j * box, (i + 1) * box, (j + 1) * box, fill=col, outline=col))

# %%
def GameRule(sum_cell, new_m):
    # Правило игры
    if sum_cell in [N1, N2, N3]: 
        new_m[i][j] = 1
    else: 
        new_m[i][j] = 0

# %%
def UpdateScreen(m):
    for i in range(N):
        for j in range(N):
            if m[i][j] == 1:
                col = 'red'
            else: 
                col = 'white'
            cs.itemconfig(rect[i * N + j], fill=col, outline=col)

# %%
def life():
    for i in range(N):
        for j in range(N):
            global m, new_m
            left = i - 1
            right = i + 1
            up = j - 1
            bottom = j + 1

            if i == 0: left = N-1
            if i == N - 1: right = 0
            if j == 0: up = N - 1
            if j == N - 1: bottom = 0

            sum_cell =  m[left][up]     + m[i][up]     + m[right][up] + \
                        m[left][j]      + 0            + m[right][j] + \
                        m[left][bottom] + m[i][bottom] + m[right][bottom]

            if sum_cell in [N1, N2, N3]: 
                new_m[i][j] = 1
            else: 
                new_m[i][j] = 0
                
            if m[i][j]:
                col = 'green'
            else: 
                col = 'white'
            cs.itemconfig(rect[i * N + j], fill=col, outline=col)
        
    m = new_m.copy()
            
    root.after(300, life)


# %%
life()
root.mainloop()

# %%



