import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from numpy import pi, sin, cos, exp, linspace, array


P = array([[0,0,0,1], [6,0,0,1], [6,0,3,1], [0,0,3,1], [0,0,0,1]])


h = 12
j = -10
k = 10


T = array([[1,0,0,0], [0,1,0,0], [0,0,1,0],[h,j,k,1]])

F = P@T
plt.figure()
plt.subplot(111, projection ='3d')
plt.xlabel('Eje x')
plt.ylabel('Eje y')
plt.title("Figura 4.2.1. Traslacion en el plano 3D")
plt.plot(P[:,0], P[:,1], P[:,2])
plt.plot(F[:,0], F[:,1], F[:,2])
plt.show()
