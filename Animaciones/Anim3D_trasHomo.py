import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from numpy import pi, sin, cos, exp, linspace, array

P = array([[0,0,0,1], [6,0,0,1], [6,0,3,1], [0,0,3,1], [0,0,0,1]])

plt.figure()

for i in range(20):
    h = 12+i
    j = -10+i
    k = 0

    T = array([[1,0,0,0], [0,1,0,0], [0,0,1,0], [h,j,k,1]])
    F = P@T
    plt.subplot(111, projection='3d')

    plt.xlim(-1,40)
    plt.ylim(-10,20)

    plt.plot(F[:,0], F[:,1], F[:,2])
    plt.title("Animacion 4.2.1 Traslación en 3D")
    plt.pause(0.5)

    if i != 19:
        plt.clf()
