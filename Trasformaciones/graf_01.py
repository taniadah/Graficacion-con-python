import numpy as np
import  matplotlib.pyplot as plt
from numpy import linspace, sin , cos, pi, array, exp

t = linspace(0,1,10)

h=3
k=-4

P = np.array([[0,0],[3,-6],[4,5],[-2,-6], [0,0]], dtype=float)
print(P)

figure, ax = plt.subplots()
ax.plot(P[:,0], P[:,1])
#ax.plot(T[:,0], T[:,1])
ax.grid()
ax.set_title("Figura")

figure2, ax = plt.subplots()
ax.plot(P[:,0], P[:,1])
ax.plot(P[:,0]+h, P[:,1]+k)
#ax.plot(T[:,0], T[:,1])
ax.grid()
ax.set_title("TRASLACIÓN EN X E Y")

figure3, ax = plt.subplots()
ax.plot(P[:,0], P[:,1])
ax.plot(P[:,0]+h, P[:,1])
#ax.plot(T[:,0], T[:,1])
ax.grid()
ax.set_title("TRASLACIÓN EN X")

figure3, ax = plt.subplots()
ax.plot(P[:,0], P[:,1])
ax.plot(P[:,0], P[:,1]+k)
#ax.plot(T[:,0], T[:,1])
ax.grid()
ax.set_title("TRASLACIÓN EN Y")

plt.show()
