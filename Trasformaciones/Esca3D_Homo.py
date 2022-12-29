import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from numpy import pi, sin, cos, exp, linspace, array

P = array([[0,0,0,1], [6,0,0,1], [6,0,3,1], [0,0,3,1], [0,0,0,1]])
sx = 0.5
sy = 0.5
sz = 0.5
S = array(([[sx,0,0,0], [0,sy,0,0], [0,0,sz,0], [0,0,0,1] ]))
E = P@S

plt.figure()
plt.subplot(111, projection='3d')
plt.xlabel('Eje x')
plt.ylabel('Eje y')
plt.title("Figura 4.2.3 Escalamiento en el plano 3D")
plt.plot(P[:,0], P[:,1], P[:,2])
plt.plot(E[:,0], E[:,1], E[:,2])
plt.show()

fig2 = plt.figure()
for i in range (5):
    sx -= 0.1
    sy -= 0.1
    sz -= 0.1

    S = array(([[sx,0,0,0], [0,sy,0,0], [0,0,sz,0], [0,0,0,1] ]))
    E = P@S

    ax=fig2.add_subplot(111, projection="3d")
    ax.plot(E[:,0], E[:,1], E[:,2])
    plt.xlim(-4,6)
    plt.ylim(-4,6)
    plt.title("Animación 4.2.3 Escalamiento en el plano 3D")
    plt.axis('off')
    plt.pause(0.5)
    plt.clf()
