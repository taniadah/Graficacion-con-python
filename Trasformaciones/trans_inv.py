import numpy as np
import matplotlib.pyplot as plt
from numpy import pi, sin, cos, array, exp, linspace

#coordenadas homogeneas
P = array([[3,-4,1], [-7,2,1],[-6,-1,1], [9,5,1], [3, -4, 1]])
sx = 0.5
sy = 0.75

th = pi/6

Sxy = array([[sx, 0,0],[0,sy,0],[0,0,1]])
S_xy = array([[1/sx, 0,0],[0,1/sy,0],[0,0,1]])
Rx = array([[1,0,0], [0,-1,0],[0,0,1]])
R = array([[cos(th), sin(-th),0],[-sin(th), cos(th), 0], [0,0,1]])
Ri= array([[cos(-th), sin(-th),0],[-sin(-th), cos(-th), 0], [0,0,1]])

F = P@Rx
V = F@Rx

plt.figure()
plt.plot(P[:,0], P[:,1])
plt.title("Figura 3.1. Original")

plt.figure()
plt.plot(F[:,0], F[:,1])
plt.plot(V[:,0], V[:,1])
plt.grid()
plt.title("Figura 3.1.1 Inversa Reflexion")

F = P@Sxy
V = F@S_xy

plt.figure()
plt.plot(F[:,0], F[:,1])
plt.plot(V[:,0], V[:,1])
plt.grid()
plt.title("Figura 3.1.2 Inversa Escalamiento")

C = P@(Sxy@R)
V = C@(Ri@S_xy)
plt.figure()
plt.plot(C[:,0], C[:,1])
plt.plot(V[:,0], V[:,1])
plt.grid()
plt.title("Figura 3.1.3 Inversa Concatenacion Escalamiento-Rotación")
plt.show()
