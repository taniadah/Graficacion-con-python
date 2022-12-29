import numpy as np
import matplotlib.pyplot as plt
from numpy import pi, sin, cos, array, exp, linspace
import math as m

P = array([[0,0], [3,7],[ 6,0], [0,0]])
ang = 0

print("Puntos a transformar")
print(P)

plt.figure()

for i in range(7):
    ang+=60
    grados = m.radians(ang)

    print("angulo: ", ang)

    Rxy = np.array([[cos(grados), sin(grados)], [-sin(grados), cos(grados)]])

    print("Matriz de transformación")
    print(Rxy)

    R = P@Rxy
    print("Puntos de transformación")
    print(R)
    plt.plot(R[:,0], R[:,1])
    plt.title("Figura 1.3.{} Rotacion de {}°".format(i+1, ang) )

    plt.axis('off')
    plt.pause(3)
    plt.clf()

plt.figure()
plt.plot(P[:,0], P[:,1])
plt.title("Figura 1.3 Triangulo Original")
plt.show()
