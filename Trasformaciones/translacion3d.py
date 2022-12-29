import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

P = np.array([[3,-4,-3], [-7,2,5], [-6,-1,4], [9,5,-1], [3,-4,-3]])
Rx = np.array([[1,0,0], [0,-1,0], [0,0,1]])

F = P@Rx

fig = plt.figure()
ax = fig.add_subplot(projection = "3d")
ax.plot(P[:,0], P[:,1], P[:,2])
ax.plot(F[:,0], F[:,1], F[:,2])
plt.show()
