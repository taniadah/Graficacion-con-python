import numpy as np
import matplotlib.pyplot as plt
from numpy import pi, sin, cos, array, exp, linspace

P = array([[3,-4], [-7,2], [6,5], [3,-4]], dtype=float)

T = np.zeros((4,2),dtype=float)
h = 8
k = 5

plt.figure()
for i in range(51):
    t = float(i/50)
    T[:,0] =(1-t) * (P[:,0])+t*(P[:,0]+h)
    T[:,1] =(1-t) * (P[:,1])+t*(P[:,1]+k)
    plt.plot(T[:,0], T[:,1])
    plt.xlim(-10,16)
    plt.ylim(-10,14)
    plt.axis('off')
    plt.pause(0.01)
    plt.clf()
