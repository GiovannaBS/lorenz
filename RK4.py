# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 20:16:55 2018

@author: alexa
"""
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

#definição das variáveis
to = 0 #tempo inicial
x = 0.1
y = 0.1
z = 1.7
dt = 0.01 #passo
ro = 10
beta = 20
sigma = 28
tf = 1000 #tempo final

#numero de passos de tempo:
n = int((tf-to)/dt)

#criar matriz para os resultados das variáveis x, y, z para os passos de tempo
matriz_x = np.zeros((1,n))
matriz_y = np.zeros((1,n))
matriz_z = np.zeros((1,n))

#para passo igual a to, a primeira coluna corresponde aos valores iniciais de x, y, z respectivamente
matriz_x[0,0] = x
matriz_y[0,0] = y
matriz_z[0,0] = z

#criar matriz k para os 4 coeficientes (inclinações) dadas as funções f1,f2,f3
#(em que se substitui os valores das variáveis x, y, z nas funções dadas as condições iniciais)
k = np.zeros((3,4))

#criar matriz para as variáveis x,y,z (contar os valores calculados para 4 k mais a condição inicial)
m_x = np.zeros((1,5))
m_y = np.zeros((1,5))
m_z = np.zeros((1,5))
#onde o primeiro elemento de cada uma das matrizes das variáveis x,y,z corresponde 
#aos respectivos valores das condições iniciais
m_x[0,0] = x
m_y[0,0] = y
m_z[0,0] = z


for i in np.arange (1,n,1):
    #resultados de x, y, z para cada passo de tempo ti (demais passos de tempo)
    for j in np.arange (0,4,1):
        k[0,j] = sigma*(m_y[0,j]-m_x[0,j])
        k[1,j] = m_x[0,j]*(ro-m_z[0,j])-m_y[0,j]
        k[2,j] = m_x[0,j]*m_y[0,j]-beta*m_z[0,j]
        m_x[0,j+1] = matriz_x[0,i-1]+(k[0,j]*dt/2)
        m_y[0,j+1] = matriz_y[0,i-1]+(k[1,j]*dt/2)
        m_z[0,j+1] = matriz_z[0,i-1]+(k[2,j]*dt/2)
            
        if j==2:
            k[0,j] = sigma*(m_y[0,j]-m_x[0,j])
            k[1,j] = m_x[0,j]*(ro-m_z[0,j])-m_y[0,j]
            k[2,j] = m_x[0,j]*m_y[0,j]-beta*m_z[0,j]
            m_x[0,j+1] = matriz_x[0,i-1]+(k[0,j]*dt)
            m_y[0,j+1] = matriz_y[0,i-1]+(k[1,j]*dt)
            m_z[0,j+1] = matriz_z[0,i-1]+(k[2,j]*dt)
        if j==3:
            k[0,j] = sigma*(m_y[0,j]-m_x[0,j])
            k[1,j] = m_x[0,j]*(ro-m_z[0,j])-m_y[0,j]
            k[2,j] = m_x[0,j]*m_y[0,j]-beta*m_z[0,j]
            m_x[0,j+1] = matriz_x[0,i-1]+((k[0,0]+(2*k[0,1])+(2*k[0,2])+k[0,3])*dt/6)
            m_y[0,j+1] = matriz_y[0,i-1]+((k[1,0]+(2*k[1,1])+(2*k[1,2])+k[1,3])*dt/6)
            m_z[0,j+1] = matriz_z[0,i-1]+((k[2,0]+(2*k[2,1])+(2*k[2,2])+k[2,3])*dt/6)
    matriz_x[0,i] =  m_x[0,j+1]
    matriz_y[0,i] =  m_y[0,j+1]
    matriz_z[0,i] =  m_z[0,j+1]
    #esse resultado corresponde à condição inicial da próxima iteração, logo:
    m_x[0,0] = matriz_x[0,i]
    m_y[0,0] = matriz_y[0,i]
    m_z[0,0] = matriz_z[0,i]
    """if i==1:
        print(matriz_x[0,i])"""
        
print ('n',n)
print ('matriz',matriz_x)
print (matriz_x.shape)
#criar grágico      
fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')
x,y,z = matriz_x,matriz_y,matriz_z

ax.plot_wireframe(x,y,z)
plt.show()




