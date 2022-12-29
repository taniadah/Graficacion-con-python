"""Concatenación de escalamiento ejes x y"""
import matplotlib.pyplot as plt
import numpy as np
from numpy import  pi, sin, cos, exp, sqrt

P = np.array([[3,-4],[-7,2],[-6,-1],[9,5],[3,-4]])

sx=2.5
sy = 0.75

Sxy = np.array([[sx,0], [0, sy]])
Rx = np.array([[1,0],[0,-1]])

T = P@(Sxy@Rx)
print("Matriz de transformación")
print(T)

plt.figure()
plt.grid()
plt.plot(P[:,0], P[:,1])
plt.title("Figura 2.1. Figura original")

figure, ax = plt.subplots()
ax.plot(P[:,0], P[:,1])
ax.plot(T[:,0], T[:,1])
ax.grid()
ax.set_title("Figura 2.1.1. Concatenación de escalamiento y reflexión")
plt.show()
