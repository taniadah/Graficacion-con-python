import numpy as np
import matplotlib.pyplot as plt
from numpy import pi, sin, cos, array, exp, linspace

P = np.array([[2, 3], [5, 2], [3, 3], [2, 3]], dtype=float)

print("Puntos a transformar")
print(P)

Rx = np.array([[1,0],[0,-1]])
Ry = np.array([[-1,0],[0,1]])

print("Matriz de Transformación")
print(Rx)
R = P@Rx
print("Puntos transformados para Reflexión en eje X")
print(R)

figure, ax = plt.subplots()
ax.plot(P[:,0], P[:,1])
ax.grid()
ax.set_title("Figura 1.2. Figura Original")

figure, ax = plt.subplots()
ax.plot(P[:,0], P[:,1])
ax.plot(R[:,0], R[:,1])
ax.grid()
ax.set_title("Figura 1.2.1 Reflexión ejes x")

print("Matriz de Transformación")
print(Ry)
R = P@Ry
print("Puntos transformados para Reflexión en eje y")
print(R)
figure, ax = plt.subplots()
ax.plot(P[:,0], P[:,1])
ax.plot(R[:,0], R[:,1])
ax.grid()
ax.set_title("Figura 1.2.2 Reflexión eje y")

R = R@Rx
print("Puntos transformados para Reflexión en eje x e y")
print(R)
figure, ax = plt.subplots()
ax.plot(P[:,0], P[:,1])
ax.plot(R[:,0], R[:,1])
ax.grid()
ax.set_title("Figura 1.2.3 Reflexión eje x e Y")
plt.show()
