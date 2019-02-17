import numpy as np
from scipy import signal

seed = 5093
#seed = 18
#seed = 42
width = 300
height = 300

def level(x, y):
    return ((((x + 10) * y + seed) * (x + 10)) % 1000 // 100) - 5

def grid():
    return np.fromfunction(level, (width, height))

def max_area_sum(matrix, area_width, area_height):
    mask = np.full((area_width, area_height) ,1)
    c = signal.convolve2d(matrix, mask, mode='valid')
    x, y = np.unravel_index(c.argmax(), c.shape)
    s = c[x, y]
    print(area_width, x, y, s)
    return x, y, s

def outputs(matrix):
    for size in range(1, 50):
        x, y, s = max_area_sum(matrix, size, size)
        yield {'size': size, 'coord': (x, y), 'sum': s}

matrix = grid()
print(max(outputs(matrix), key=lambda output: output['sum']))
