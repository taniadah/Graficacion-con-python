"""Concatenación de tres transformaciones"""

import matplotlib.pyplot as plt
import numpy as np
from numpy import  pi, sin, cos, exp, sqrt

P = np.array([[3,-4],[-7,2],[-6,-1],[9,5],[3,-4]])

sx = 2.5
sy = 0.75

th = pi/4

Sxy = np.array([[sx,0], [0, sy]])
Ry = np.array([[-1, 0],[0,1]])
R = np.array([[cos(th), sin(th)],[-sin(th), cos(th)]])

T = P@(Sxy@(Ry@R))
print("Matriz de transformación")
print(T)

plt.figure()
plt.plot(P[:,0],P[:,1])
plt.plot(T[:,0],T[:,1])
plt.grid()
plt.title("Figura 2.1.2 Concatenación de tres transformaciones")
plt.show()
