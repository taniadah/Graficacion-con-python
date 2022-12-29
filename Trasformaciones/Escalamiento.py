import numpy as np
import matplotlib.pyplot as plt
from numpy import pi, sin, cos, array, exp, linspace

P = np.array([[1, 1], [3, 1], [2, 2], [1.5, 3], [1, 1]])

sx = 2
sy = 0.5

plt.figure()
plt.grid()
plt.plot(P[:,0], P[:,1])
plt.title("Figura 1.4. Original")

Sxy = np.array([[sx,0], [0,sy]])
print("Matriz de transformación")
print(Sxy)
S = P@Sxy
print("Puntos transformados")
print(S)

figure, ax = plt.subplots()
ax.grid()
ax.plot(P[:,0], P[:,1])
ax.plot(S[:,0], S[:,1])
ax.set_title("Figura 1.4.1 Escalamiento Sx>1")

sx = 0.7
sy = 0.5

Sxy = np.array([[sx,0], [0,sy]])
print("Matriz de transfromación")
print(Sxy)
S = P@Sxy
print("Puntos transformados")
print(S)
figure, ax = plt.subplots()
ax.grid()
ax.plot(P[:,0], P[:,1])
ax.plot(S[:,0], S[:,1])
ax.set_title("Figura 1.4.2 Escalamiento 0<Sx<1")

sx = 0
sy = 0.5

Sxy = np.array([[sx,0], [0,sy]])
print("Matriz de transfromación")
print(Sxy)
S = P@Sxy
print("Puntos transformados")
print(S)
figure, ax = plt.subplots()
ax.grid()
ax.plot(P[:,0], P[:,1])
ax.plot(S[:,0], S[:,1])
ax.set_title("Figura 1.4.3 Escalamiento Sx=0")
plt.show()
