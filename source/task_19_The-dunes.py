"""19. Разработайте клеточный автомат «Дюны», поведение которого подчинено следующим правилам: 
1) клетка может находиться в активном и пассивном («спрятанном») состоянии; 
2) если клетка была активна и из восьми соседних клеток более N активны, то клетка «прячется». 
3) Время нахождения в «спрятанном» состоянии равно W тактов; 4) если время «прятания» закончилось 
    и в окрестности не более М активных клеток, то клетка вновь становится активной.
"""

import numpy as np
import tkinter as tk


# Создаём окно через tkinter
root = tk.Tk()
root.title("The dunes")
cs = tk.Canvas(root, width=500, height=500)
cs.pack()


# Функция создания цвета в формате RGB 
def rgb_color(color):
    return '#%02x%02x%02x' % color

# Пусть клетка будет активной, если её значение будет равно 0 
# и она будет находиться в спрятаном состоянии, если её значение равно [1, W]

# Зададим константы из условия (значения случайные)
N = 4
W = 5
M = 3

box = 5 # Размер клетки
COUNT = 100 # Размер поля в клетках

m = np.full((COUNT, COUNT), W, dtype=int) # Матрица состояния клеток (создадим двумерный массив размером [N, N], те все клетки спрятаны)
new_m = np.full((COUNT, COUNT), W, dtype=int) # Матрица новых состояний

# "Пробудим" случайные клетки на поле
count_cells = 5000
rand_x = np.random.randint(0, COUNT, count_cells)
rand_y = np.random.randint(0, COUNT, count_cells)
rand_x, rand_y

for i in range(count_cells):
    m[rand_x[i]][rand_y[i]] = 0
    

# Функция получения цвета для клетки
def cell_color(value):
    # Разные цвета для спящих клеток
        if value > 0:
            col = rgb_color((0, value * 15 % 255, value * 15 % 255))
        else:
            col = 'red' # Активные клетки будут красного цвета
            
        return col
    
# Создадим массив прямоугольников на экране, которые будут играть роль клеток
rect = []
for i in range(COUNT):
    for j in range(COUNT):
        col = cell_color(m[i][j])
        rect.append(cs.create_rectangle(i * box, j * box, (i + 1) * box, (j + 1) * box, fill=col, outline=col))

# Обновляем цвета клеток на экране
def UpdateScreen():
    for i in range(COUNT):
        for j in range(COUNT):
            col = cell_color(m[i][j])
            cs.itemconfig(rect[i * COUNT + j], fill=col, outline=col)
            
# Получаем состояние клетки по её занчению
def cell_condition(value):
    if value > 0: # Если клетка спит, то возвращаем 0
        return 0
    else: # Если клетка активна, то возвращаем 1
        return 1
            
# Основная функция в которой идёт логика автомата
def life():
    for i in range(COUNT):
        for j in range(COUNT):
            global m, new_m
            left = i - 1
            right = i + 1
            up = j - 1
            bottom = j + 1

            # Замыкаем поле, чтобы не работать с границами
            if i == 0: left = COUNT - 1
            if i == COUNT - 1: right = 0
            if j == 0: up = COUNT - 1
            if j == COUNT - 1: bottom = 0

            sum_cell = cell_condition(m[left][up]) +cell_condition(m[i][up]) +cell_condition(m[right][up]) + \
                        cell_condition(m[left][j]) + 0 +cell_condition(m[right][j]) + \
                        cell_condition(m[left][bottom]) +cell_condition(m[i][bottom]) +cell_condition(m[right][bottom])
            
            # Правила автомата
            # Если клетка в спрятаном состоянии, убавляем её значение
            if m[i][j] > 0:
                new_m[i][j] = m[i][j] - 1
            # Если количество активных соседей клетки больше N, то клетка засыпает
            elif sum_cell > N: 
                new_m[i][j] = W
            # Если количество соседей меньше M, то клетка становиться активной
            elif sum_cell < M: 
                new_m[i][j] = 0

                
    
    UpdateScreen() # Вызываем функцию обновления данных на экране
    m = new_m.copy() # Обновляем массив состояний клеток
            
    root.after(300, life) # Запускаем функцию life через 300 милисекунд


life()
root.mainloop()