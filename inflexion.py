#!/usr/bin/env python3

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# Data for plotting
with open("inflexion.dat") as file:  
    data = file.readlines() 

n_vector=[]
real_vector=[]
user_vector=[]
sys_vector=[]

for line in data:
    if '#' not in line[0]:
        n,real,user,sys = line.split('\t')
        n_vector.append(int(n))
        real_vector.append(float(real))
        user_vector.append(float(user))
        sys_vector.append(float(sys))
    

t = np.arange(0.0, 2.0, 0.01)
s = 1 + np.sin(2 * np.pi * t)

fig, ax = plt.subplots()
ax.plot(t, s)

ax.set(xlabel='time (s)', ylabel='voltage (mV)',
       title='About as simple as it gets, folks')
ax.grid()

fig.savefig("test.png")
plt.show()
