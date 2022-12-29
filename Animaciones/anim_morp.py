import numpy as np
import matplotlib.pyplot as plt
from numpy import pi, sin, cos, array, exp, linspace

A = np.array([[0,0],[0,4],[1.5,5],[3,4],[3,0], [2,0],[2,1],[1,1],[1,0],[0,0]])
B = np.array([[8,2],[8,4],[6,4],[6,5],[8.5,5],[11,5],[11,4],[9,4],[9,2],[8,2]])

T = np.zeros((10,2))

for i in range(11):
    t = float(i/10)
    T[:,0] = (1-t)*A[:,0]+t*B[:,0]
    T[:,1] = (1-t)*A[:,1]+t*B[:,1]

    plt.plot(T[:,0], T[:,1])
    plt.xlim(-1,13)
    plt.ylim(-1,10)
    plt.axis('off')
    plt.pause(.0200)
    plt.clf()

plt.pause(1)

plt.figure()
plt.plot(A[:,0], A[:,1])

plt.figure()
plt.plot(B[:,0], B[:,1])
plt.show()
