import numpy as np
import matplotlib.pyplot as plt
from numpy import pi, sin, cos, array, exp, linspace

P = array([[3, -4],[-7,2]], dtype = float)
T = np.zeros((1,2),dtype = float)

plt.figure()

for i in range(101):
    t = float(i/100)
    T[0,0] =(1-t) * P[0,0]+t*P[1,0]
    T[0,1] =(1-t) * P[0,0]+t*P[1,1]
    plt.plot(T[0,0],T[0,1], 'r:*')
    plt.xlim(-10,6)
    plt.ylim(-7,4)
    plt.axis('off')
    plt.pause(0.5)
    plt.clf()
