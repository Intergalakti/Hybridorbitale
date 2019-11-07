# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 22:18:25 2019

@author: markz
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.special import sph_harm 
# nur fuer den Seiteneffekt: plt.gca(projection = '3d') funktioniert sonst nicht
from mpl_toolkits.mplot3d import Axes3D 
from matplotlib import cm

theta_1d = np.linspace(0,   np.pi,  91) # 2 GRAD Schritte
phi_1d   = np.linspace(0, 2*np.pi, 181) # 2 GRAD Schritte

theta_2d, phi_2d = np.meshgrid(theta_1d, phi_1d)
xyz_2d = np.array([np.sin(theta_2d) * np.sin(phi_2d),
                  np.sin(theta_2d) * np.cos(phi_2d),
                  np.cos(theta_2d)]) 

colormap = cm.ScalarMappable( cmap=plt.get_cmap("cool"))
colormap.set_clim(-.45, .45)
limit = .5

print("Hybridorbitale")

Ys=1/np.sqrt(4*np.pi)
Yx=np.sqrt(3/(4*np.pi))*np.sin(theta_2d)*np.cos(phi_2d)
Yy=np.sqrt(3/(4*np.pi))*np.sin(theta_2d)*np.sin(phi_2d)
Yz=np.sqrt(3/(4*np.pi))*np.cos(theta_2d)
sp_1 = (Ys+Yx) /np.sqrt(2)
sp_2 = (Ys-Yx) /np.sqrt(2)
sp2_1 = Ys/np.sqrt(3)+Yx/np.sqrt(6)+Yy/np.sqrt(2)
sp2_2 = Ys/np.sqrt(3)+Yx/np.sqrt(6)-Yy/np.sqrt(2)
sp2_3 = Ys/np.sqrt(3)-2*Yx/np.sqrt(6)
sp3_1 = (1/2)*(Ys+Yx+Yy+Yz)
sp3_2 = (1/2)*(Ys+Yx-Yy-Yz)
sp3_3 = (1/2)*(Ys-Yx+Yy-Yz)
sp3_4 = (1/2)*(Ys-Yx-Yy+Yz)

plt.figure()
ax = plt.gca(projection = "3d")
plt.title("First sp1 orbital")
r = np.abs(sp_1.real)*xyz_2d
ax.plot_surface(r[0], r[1], r[2], 
                facecolors=colormap.to_rgba(np.abs(sp_1)), 
                rstride=2, cstride=2)
ax.set_xlim(-limit,limit)
ax.set_ylim(-limit,limit)
ax.set_zlim(-limit,limit)
ax.set_aspect("equal")
plt.savefig('sp_1.pdf')
#ax.set_axis_off()

plt.figure()
ax = plt.gca(projection = "3d")
plt.title("Second sp1 orbital")
r = np.abs(sp_2.real)*xyz_2d
ax.plot_surface(r[0], r[1], r[2], 
                facecolors=colormap.to_rgba(np.abs(sp_2)), 
                rstride=2, cstride=2)
ax.set_xlim(-limit,limit)
ax.set_ylim(-limit,limit)
ax.set_zlim(-limit,limit)
ax.set_aspect("equal")
plt.savefig('sp_2.pdf')

plt.figure()
ax = plt.gca(projection = "3d")
plt.title("First sp2 orbital")
r = np.abs(sp2_1.real)*xyz_2d
ax.plot_surface(r[0], r[1], r[2], 
                facecolors=colormap.to_rgba(np.abs(sp2_1)), 
                rstride=2, cstride=2)
ax.set_xlim(-limit,limit)
ax.set_ylim(-limit,limit)
ax.set_zlim(-limit,limit)
ax.set_aspect("equal")
plt.savefig('sp2_1.pdf')

plt.figure()
ax = plt.gca(projection = "3d")
plt.title("Second sp2 orbital")
r = np.abs(sp2_2.real)*xyz_2d
ax.plot_surface(r[0], r[1], r[2], 
                facecolors=colormap.to_rgba(np.abs(sp2_2)), 
                rstride=2, cstride=2)
ax.set_xlim(-limit,limit)
ax.set_ylim(-limit,limit)
ax.set_zlim(-limit,limit)
ax.set_aspect("equal")
plt.savefig('sp2_2.pdf')

plt.figure()
ax = plt.gca(projection = "3d")
plt.title("Third sp2 orbital")
r = np.abs(sp2_3.real)*xyz_2d
ax.plot_surface(r[0], r[1], r[2], 
                facecolors=colormap.to_rgba(np.abs(sp2_3)), 
                rstride=2, cstride=2)
ax.set_xlim(-limit,limit)
ax.set_ylim(-limit,limit)
ax.set_zlim(-limit,limit)
ax.set_aspect("equal")
plt.savefig('sp2_3.pdf')

plt.figure()
ax = plt.gca(projection = "3d")
plt.title("First sp3 orbital")
r = np.abs(sp3_1.real)*xyz_2d
ax.plot_surface(r[0], r[1], r[2], 
                facecolors=colormap.to_rgba(np.abs(sp3_1)), 
                rstride=2, cstride=2)
ax.set_xlim(-limit,limit)
ax.set_ylim(-limit,limit)
ax.set_zlim(-limit,limit)
ax.set_aspect("equal")
plt.savefig('sp3_1.pdf')

plt.figure()
ax = plt.gca(projection = "3d")
plt.title("Second sp3 orbital")
r = np.abs(sp3_2.real)*xyz_2d
ax.plot_surface(r[0], r[1], r[2], 
                facecolors=colormap.to_rgba(np.abs(sp3_2)), 
                rstride=2, cstride=2)
ax.set_xlim(-limit,limit)
ax.set_ylim(-limit,limit)
ax.set_zlim(-limit,limit)
ax.set_aspect("equal")
plt.savefig('sp3_2.pdf')

plt.figure()
ax = plt.gca(projection = "3d")
plt.title("Third sp3 orbital")
r = np.abs(sp3_3.real)*xyz_2d
ax.plot_surface(r[0], r[1], r[2], 
                facecolors=colormap.to_rgba(np.abs(sp3_3)), 
                rstride=2, cstride=2)
ax.set_xlim(-limit,limit)
ax.set_ylim(-limit,limit)
ax.set_zlim(-limit,limit)
ax.set_aspect("equal")
plt.savefig('sp3_3.pdf')

plt.figure()
ax = plt.gca(projection = "3d")
plt.title("Fourth sp3 orbital")
r = np.abs(sp3_4.real)*xyz_2d
ax.plot_surface(r[0], r[1], r[2], 
                facecolors=colormap.to_rgba(np.abs(sp3_4)), 
                rstride=2, cstride=2)
ax.set_xlim(-limit,limit)
ax.set_ylim(-limit,limit)
ax.set_zlim(-limit,limit)
ax.set_aspect("equal")
plt.savefig('sp3_4.pdf')

        
plt.show()