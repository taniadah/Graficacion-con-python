#!/usr/bin/env/ python3
# -*- coding: utf-8 -*-

"""
UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO

UA: GRAFICACION
Profesor: Manuel Almeida Vazquez
    
Alumno: Sanchez Alanis Jose Antonio

Tema: Coordenadas homogeneas en el plano 3D
Descripción: 

@author: Antonio
Created on Fri Sep  3 12:57:49 2021
"""

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from numpy import pi, sin, cos, exp, linspace, array

P = array([[0,0,0,1], [6,0,0,1], [6,0,3,1], [0,0,3,1], [0,0,0,1]])

plt.figure()

for i in range(20):
    h = 12+i
    j = -10+i
    k = 0
    
    T = array([[1,0,0,0], [0,1,0,0], [0,0,1,0], [h,j,k,1]])
    
    F = P@T
    
    plt.subplot(111, projection='3d')
    #plt.xlabel("Ejex")
    #plt.ylabel("Ejey")
    plt.xlim(-1,40)
    plt.ylim(-10,20)
    
    plt.plot(P[:,0], P[:,1], P[:,2])
    plt.plot(F[:,0], F[:,1], F[:,2])
    
    plt.pause(0.01)
    
    if i != 19:
        plt.clf()
