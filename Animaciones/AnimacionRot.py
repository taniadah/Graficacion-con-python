import numpy as np
import matplotlib.pyplot as plt
from numpy import pi, sin, cos, array, exp, linspace
import math as m
from matplotlib.widgets import Slider



P = array([[0,0], [3,7],[ 6,0], [0,0]])
P = np.array([[1, 1], [3, 2], [2, 2], [1, 1]])


plt.figure()

for i in range(50):
    th = i*pi/30
    #print(th)

    Rx = np.array([[cos(th), sin(th)], [-sin(th), cos(th)]])

    T = P@Rx
    plt.plot(T[:,0], T[:,1])
    plt.axis('off')
    plt.pause(0.001)
    plt.clf()
