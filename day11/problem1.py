import numpy as np
from scipy import signal

seed = 5093
#seed = 18
#seed = 42
width = 300
height = 300

# For example, to find the power level of the fuel cell at 3,5 in a grid with serial number 8:
#
# The rack ID is 3 + 10 = 13.
# The power level starts at 13 * 5 = 65.
# Adding the serial number produces 65 + 8 = 73.
# Multiplying by the rack ID produces 73 * 13 = 949.
# The hundreds digit of 949 is 9.
# ubtracting 5 produces 9 - 5 = 4.
#

def level(x, y):
    return ((((x + 10) * y + seed) * (x + 10)) % 1000 // 100) - 5

def grid():
    return np.fromfunction(level, (width, height))

matrix = grid()
mask = np.full((3,3) ,1)

c = signal.convolve2d(matrix, mask)

x, y = np.unravel_index(c.argmax(), c.shape)
x -= 2
y -= 2

print(x, y)
