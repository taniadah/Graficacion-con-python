import numpy as np
import matplotlib.pyplot as plt
from numpy import pi, sin, cos, array, exp, linspace

P = array([[3,-4], [-7,2], [6,5], [3,-4]], dtype=float)
Q = array([[-3,-5], [9,2], [-2,5], [-3,-5]], dtype=float)
T = np.zeros((4,2),dtype=float)

plt.figure()
plt.figure()
for i in range(51):
    q = float(4*i*pi)/100
    T[:,0] = pow(sin(q),2)*P[:,0]+pow(cos(q), 2)*Q[:,0]
    T[:,1] = pow(sin(q),2)*P[:,1]+pow(cos(q), 2)*Q[:,1]
    plt.plot(T[:,0], T[:,1])
    plt.xlim(-10,16)
    plt.ylim(-10,14)
    plt.axis('off')
    plt.pause(0.01)
    plt.clf()

plt.pause(1.5)
