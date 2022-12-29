import numpy as np
import matplotlib.pyplot as plt
from numpy import pi, sin, cos, array, exp, linspace
import math as m
from matplotlib.widgets import Slider

class Brazo:
    def __init__(self):
        self.j1 = np.array([[0,0,1],[2,2,1],[0,0,1]])
        x1 = self.j1[0,0]
        y1 = self.j1[0,1]
        x2 = self.j1[1,0]
        y2 = self.j1[1,1]
        self.d = abs(m.sqrt(pow(x2-x1, 2) + pow(y2-y1,2)))
        pend = (y2-y1)/(x2-x1)
        th1 = m.atan(pend)
        th2 = np.radians(45)

        j2 = self.DenavitHartenberg(th1, th2, self.d)

        plt.figure(1)
        plt.ylim(-6,6)
        plt.xlim(-6,6)
        self.pj1, = plt.plot(self.j1[:,0], self.j1[:,1])
        self.pj2, = plt.plot(j2[:,0], j2[:,1])

        # #creación y posición del slider
        axSlider1 = plt.axes([0.1,0.05, 0.8, 0.01])
        self.slider1 = Slider(ax = axSlider1, label = "Theta1", valmin=-180, valmax=180, valinit=m.degrees(th1), valfmt='%1.2f', valstep=1,  closedmax = True, color = 'cyan')
        self.slider1.on_changed(self.val_update)
        #putSlider(m.degrees(th1))

        axSlider2 = plt.axes([0.1,.9, 0.8, 0.01])
        self.slider2 = Slider(ax = axSlider2, label = "Theta2", valmin=-180, valmax=180, valinit=m.degrees(th2), valfmt='%1.2f', valstep=1,  closedmax = True, color = 'cyan')
        self.slider2.on_changed(self.val_update2)
        #putSlider(m.degrees(th1))
        plt.show()

    def val_update(self,val):
        th1 = m.radians(val)
        co =( self.d * sin(th1))
        ca = (self.d * cos(th1))
        th2 = m.radians(self.slider2.val)
        self.j1 = np.array([[0,0,1],[ca,co,1],[0,0,1]])
        nj2 = self.DenavitHartenberg(th1, th2, self.d)
        self.pj1.set_data(self.j1[:,0], self.j1[:,1])
        self.pj2.set_data(nj2[:,0], nj2[:,1])


    def DenavitHartenberg(self,th1, th2, d):
        Rx =  np.array([[cos(th2), sin(th2), 0],[-sin(th2), cos(th2), 0],[0,0,1]])
        dRx = np.array([[self.d*cos(th1), self.d*sin(th1), 1]])
        nj2 = (self.j1@Rx) + dRx
        return nj2

    def val_update2(self,val):
        th1 = self.slider1.val
        th1 = m.radians(th1)
        th2 = m.radians(val)
        #j,k = pj1.get_data
        nj2 = self.DenavitHartenberg(th1, th2, self.d)
        self.pj2.set_data(nj2[:,0], nj2[:,1])


b1 = Brazo()
