import numpy as np
import matplotlib.pyplot as plt
from numpy import pi, sin, cos, array, exp, linspace

P = np.array([[2, 2], [4, 2], [3,3],[2,3.5], [2,2]], dtype=float)

h = 2
k = 1

figure, ax = plt.subplots()
ax.plot(P[:,0], P[:,1])
ax.grid()
ax.set_title("Figura 1.1. Posición Original")

figure2, ax = plt.subplots()
ax.plot(P[:,0], P[:,1])
ax.plot(P[:,0]+h, P[:,1]+k)
ax.grid()
ax.set_title("Figura 1.1.3. TRASLACIÓN EN X E Y")

figure3, ax = plt.subplots()
ax.plot(P[:,0], P[:,1])
ax.plot(P[:,0]+h, P[:,1])
ax.grid()
ax.set_title("Figura 1.1.1. TRASLACIÓN EN X")

figure3, ax = plt.subplots()
ax.plot(P[:,0], P[:,1])
ax.plot(P[:,0], P[:,1]+k)
ax.grid()
ax.set_title("Figura 1.1.2 TRASLACIÓN EN Y")

plt.show()
