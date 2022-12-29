import matplotlib.pyplot as plt
import numpy as np
from numpy import  pi, sin, cos, exp, sqrt

#coordenadas homogenéneas
P = np.array([[3,-4,1], [-7,2,1], [-6,-1,1],[9,5,1], [3,-4,1]])

sx = 2.5
sy = .75

h = 5
k = -4

th = pi/4

Sxy = np.array([[sx,0,0],[0, sy, 0], [0,0,1]])
Rx = np.array([[1,0,0],[0,-1, 0],[0,0,1]])
R = np.array([[cos(th), sin(th), 0],[-sin(th), cos(th), 0],[0,0,1]])

print("Matriz de transformación")
F = P@(Sxy@(Rx@R))
print(F)

plt.figure()
plt.plot(P[:,0],P[:,1])
plt.plot(F[:,0],F[:,1])
plt.grid()
plt.title("Figura 2.2.1. Concatenación de coordenadas homogenéneas")
plt.show()
