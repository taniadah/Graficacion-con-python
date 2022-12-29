import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from numpy import pi, sin, cos, array, exp, linspace
P=array([[0,0,0,1],
		[3,0,0,1],
		[3,0,4,1],
		[0,0,4,1],
		[0,0,0,1]])
h=12
j=-10
k=10
T=array([[1,0,0,0],[0,1,0,0],[0,0,1,0],[h,j,k,1]])
F=P@T
fig=plt.figure()
ax=fig.add_subplot(projection='3d')
plt.xlabel('eje x')
plt.ylabel('eje y')

ax.plot(P[:,0],P[:,1],P[:,2])
ax.plot(F[:,0],F[:,1],F[:,2])
plt.show()
