import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

x = [0.000, 1.250, 2.350, 3.000, 5.500] 
y = [3.000, -1.513, 2.872, -2.592, -2.813]

pointX = 1.963

origX = np.linspace(min(x), max(x), 1000)
origY = np.sin(origX) + 3 * np.cos(3 * origX)

indexes = [i for i in range(len(x))]

def func(baseX, baseY, index):
    if len(index) == 0:
        return 1
    if len(index) == 1:
        return baseY[index[0]]
    else:
        xTail = baseX[index[-1]]
        xHead = baseX[index[0]]
        value = (func(baseX, baseY, index[1:]) - func(baseX, baseY, index[:-1])) / (xTail - xHead)
        return value

def Newton(point):
    res = y[0]
    mul = 1.0
    for i in range(1, len(x)):
        mul *= (point - x[i - 1])
        res += mul * func(x, y, indexes[0 : i + 1])
    return res

def error(first, second, base):
    if second - first == 1:
        return base * 2 / np.abs(x[first] - x[second])
    else:
        return (error(first + 1, second, base) - error(first, second - 1, base)) / np.abs(x[second] - x[first])

def infilicity_error(baseX, base):
    res = base
    mul = 1
    for i in range(1, len(x)):
        mul *= np.abs(baseX - x[i - 1])
        res += mul * error(0, len(x) - 1, base)
    return res

def absolute_error(baseX, base):
    return infilicity_error(baseX, base) / Newton(baseX)

print("Infinilicty error " + str(infilicity_error(pointX, 5e-3)))
print("Absolute error " + str(absolute_error(pointX, 5e-3)))

#Original function
plt.plot(origX, origY, color = 'green', label = '1')

#Points
plt.scatter(x, y, color = 'red', label = '2')

#Newton
plt.plot(origX, [Newton(i) for i in origX], color = 'black', label = '3')

#point 'x'
plt.scatter(pointX, Newton(pointX), color = 'purple', marker = 'x', label = '4')

plt.grid()
plt.legend(["Original function", "Points", "Newtorn function", "point \'x\'"])
plt.show()